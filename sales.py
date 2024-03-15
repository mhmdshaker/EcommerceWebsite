"""
sales.py
--------

This module contains functions related to the sales and payment history operations.

"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import pymysql
from models import Customer, Goods, db, Payment_History




#Display available goods:
def display_available_goods():
    """
    Display the available goods.

    Retrieves all available goods from the database and returns a JSON
    response containing the details of each available good.

    Returns:
        Response: A JSON response containing the details of available goods.
    """
    goods = Goods.query.all()
    # Convert the list of customers to a list of dictionaries to be used for the json file
    goods_list = [
        {
            'Name': good.Name,
            'Category': good.Category,
            'Price_per_item': good.Price_per_item,
            'Description': good.Description,
            'Count_of_available_items': good.Count_of_available_items,
        }
        for good in goods
    ]

    return jsonify({"goods": goods_list}), 200




#Get goods details: This API should return full information related to a specific good:
def good_details():
    """
    Get details of a specific good.

    Retrieves the details of a specific good based on the provided 'Name'.
    Returns a JSON response containing the details of the requested good.

    Returns:
        Response: A JSON response containing the details of the requested good.
    """
    data = request.get_json()

    # Check if 'good' is provided in the JSON data
    if 'Name' not in data:
        return jsonify({"error": "Name of good is required in the request"}), 400

    good = Goods.query.filter_by(Name=data['Name']).first()

    # if not found
    if good is None:
        return jsonify({"error": "Good name is not found"}), 404
    
    try:
        good_data = {
            'Name': good.Name,
            'Category': good.Category,
            'Price_per_item': good.Price_per_item,
            'Description': good.Description,
            'Count_of_available_items': good.Count_of_available_items,
        }
        return jsonify({"Good ": good_data}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500




#Make a buyment from a customer to a good, and add it to the payment history:
def make_sale():
    """
    Make a sale transaction.

    Processes a sale transaction by deducting the purchased item's price from
    the customer's wallet, reducing the available quantity of the item, and
    adding the transaction to the payment history.

    Returns:
        Response: A JSON response indicating the success or failure of the sale.
    """
    data = request.get_json()
    if 'Name' not in data or 'Username' not in data:
        return jsonify({"error": "Name of good and Username are required"}), 400

    good = Goods.query.filter_by(Name=data['Name']).first()
    customer = Customer.query.filter_by(Username=data['Username']).first()
    payment_history = Payment_History.query.filter_by(customer_username=data['Username']).first()
    if not good or not customer:
        return jsonify({"error": "Good or customer not found"}), 404

    if good.Count_of_available_items <= 0:
        return jsonify({"error": "Good is out of stock"}), 400

    if good.Price_per_item > customer.wallet:  # Assuming wallet is a field in Payment_History
        return jsonify({"error": "Insufficient funds"}), 400

    good.Count_of_available_items -= 1
    customer.wallet -= good.Price_per_item  # Deduct the price from the customer's wallet
    good.payment_history_user = payment_history
    
    db.session.add(good)
    db.session.add(customer)
    db.session.commit()

    return jsonify({"message": "Sale completed successfully"}), 200




#Display the payment history of a user:
def get_payment_history():
    """
    Display the payment history of a user.

    Retrieves the payment history of a user based on the provided 'Username'.
    Returns a JSON response containing the names of the goods bought by the user.

    Returns:
        Response: A JSON response containing the names of goods bought by the user.
    """
    data = request.get_json()
    if 'Username' not in data:
        return jsonify({"error": "Username is required"}), 400

    payment_history = Payment_History.query.filter_by(customer_username=data['Username']).first()
    if not payment_history:
        return jsonify({"error": "Payment history not found"}), 404

    # Assuming you want to list the names of the goods bought by the user
    bought_goods = [good.Name for good in payment_history.goods]

    return jsonify({"bought_goods": bought_goods}), 200
