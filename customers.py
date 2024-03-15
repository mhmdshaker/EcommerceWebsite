"""
customers.py
-------------

This module contains functions related to customer operations.

"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import pymysql
from models import Customer, db, Payment_History
from decimal import Decimal




#add customer to DB:
def create_customer():
    """
    Add a new customer to the database.

    Returns:
        jsonify: JSON response indicating success or error.

    """
    data = request.get_json()
    try:
        if "wallet" not in data:
            data['wallet'] = 0.00
            
        new_customer = Customer(
            Fullname=data['Fullname'],
            Username=data['Username'],
            Password=data['Password'],
            Age=data['Age'],
            Address=data['Address'],
            Gender=data['Gender'],
            MaritalStatus=data['MaritalStatus'],
            wallet = data['wallet']
        )

        db.session.add(new_customer)
        
        new_payment_history = Payment_History(customer_username=data['Username'])
        db.session.add(new_payment_history)
        db.session.commit()

        return jsonify({"message": "Customer created successfully"}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400




#delete a customer from the database:
def delete_customer():
    """
    Deletes customer from database.
    Input: Username
    Returns:
        jsonify: JSON response indicating success or error.

    """
    data = request.get_json()
    # Check if 'Username' is provided in the JSON data
    if 'Username' not in data:
        return jsonify({"error": "Username is required in the request"}), 400
    
    to_be_deleted = Customer.query.filter_by(Username=data['Username']).first()
    #if not found:
    if to_be_deleted is None:
        return jsonify({"error": "Customer not found"}), 404
    
    db.session.delete(to_be_deleted)
    db.session.commit()
    return jsonify({"message": "Customer deleted successfully"}), 200




#update customer info:
def update_customer_info():
    """
    Updates customer info in database.
    Input: Username
    Returns:
        jsonify: JSON response indicating success or error.

    """
    data = request.get_json()

    # Check if 'Username' is provided in the JSON data
    if 'Username' not in data:
        return jsonify({"error": "Username is required in the request"}), 400

    to_be_updated = Customer.query.filter_by(Username=data['Username']).first()

    # if not found
    if to_be_updated is None:
        return jsonify({"error": "Customer not found"}), 404

    # Update customer information based on the provided data
    if 'Fullname' in data:
        to_be_updated.Fullname = data['Fullname']
    if 'Username' in data:
        to_be_updated.Username = data['Username']
    if 'Password' in data:
        to_be_updated.Password = data['Password']
    if 'Age' in data:
        to_be_updated.Age = data['Age']
    if 'Address' in data:
        to_be_updated.Address = data['Address']
    if 'Gender' in data:
        to_be_updated.Gender = data['Gender']
    if 'MaritalStatus' in data:
        to_be_updated.MaritalStatus = data['MaritalStatus']
    if 'wallet' in data:
        to_be_updated.wallet = data['wallet']

    db.session.commit()
    return jsonify({"message": "Customer information updated successfully"}), 200




# Get all customers from the database
def get_all_customers():
    """
    Returns:
        jsonify: JSON with all customers in database indicating success or error.

    """
    try:
        customers = Customer.query.all()

        # Convert the list of customers to a list of dictionaries
        customers_list = [
            {
                'Fullname': customer.Fullname,
                'Username': customer.Username,
                'Password': customer.Password,
                'Age': customer.Age,
                'Address': customer.Address,
                'Gender': customer.Gender,
                'MaritalStatus': customer.MaritalStatus,
                'wallet' : Customer.wallet
            }
            for customer in customers
        ]

        return jsonify({"customers": customers_list}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500




# Get a customer by username
def get_customer_by_username():
    """
    Input: Username
    Returns:
        jsonify: JSON response indicating success or error.

    """
    data = request.get_json()

    # Check if 'Username' is provided in the JSON data
    if 'Username' not in data:
        return jsonify({"error": "Username is required in the request"}), 400

    customer = Customer.query.filter_by(Username=data['Username']).first()
    # if not found
    if customer is None:
        return jsonify({"error": "Customer not found"}), 404

    try:
        customer_data = {
            'Fullname': customer.Fullname,
            'Username': customer.Username,
            'Password': customer.Password,
            'Age': customer.Age,
            'Address': customer.Address,
            'Gender': customer.Gender,
            'MaritalStatus': customer.MaritalStatus,
            'wallet': customer.wallet
        }

        return jsonify({"customer": customer_data}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500




#add money to the wallet:
def charge_wallet():
    """
    Charges customer's wallet in database.
    Input: Username
    Returns:
        jsonify: JSON response indicating success or error.

    """
    data = request.get_json()

    if 'Username' not in data:
        return jsonify({"error": "Username is required in the request"}), 400
    if 'Amount_to_charge' not in data:
        return jsonify({"error": "Amount to charge is required as an input"}), 400
    # Cannot charge negative amount
    if data['Amount_to_charge'] < 0:
        return jsonify({"error": "Amount to charge should be non-negative"}), 400

    customer = Customer.query.filter_by(Username=data['Username']).first()
    if customer is None:
        return jsonify({"error": "Customer not found"}), 404
    if type(data['Amount_to_charge'])!=int:
        if type(data['Amount_to_charge'])!=float:
            return jsonify({"error": "Invalid type for amount to charge! You shopuld input a decimal or an integer"}), 400
    customer.wallet += Decimal(data['Amount_to_charge'])
    
    db.session.commit()
    return jsonify({"message": "Customer wallet charged successfully"}), 200




#deduct money from the wallet
def deduct_money():
    """
    Deducts customer's money in database.
    Input: Username
    Returns:
        jsonify: JSON response indicating success or error.

    """
    data = request.get_json()

    if 'Username' not in data:
        return jsonify({"error: Username is required in the request"}), 400
    if "Amount_to_deduct" not in data:
        return jsonify({"error": "Amount to deduct is required as an input"}), 400
    # Cannot charge negative amount
    if data['Amount_to_deduct'] < 0:
        return jsonify({"error": "Amount to deduct should be non-negative"}), 400
    
    customer = Customer.query.filter_by(Username=data['Username']).first()
    if customer is None:
        return jsonify({"error": "Customer not found"}), 404
    if type(data['Amount_to_deduct'])!=int:
        if type(data['Amount_to_deduct'])!=float:
            return jsonify({"error": "Invalid type for amount to deduct! You shopuld input a decimal or an integer"}), 400
    if(data['Amount_to_deduct'] > customer.wallet):
        return jsonify({"error": "Deduction failed. Wallet does not contain this amount!"})

    customer.wallet -= Decimal(data['Amount_to_deduct'])
    
    db.session.commit()
    return jsonify({"message": "Deducted from customer wallet successfully"}), 200

