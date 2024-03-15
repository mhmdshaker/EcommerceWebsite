"""
app.py
-------

This module contains the main Flask application.

"""

from flask import Flask
from models import db, Customer
import customers
import inventory
import sales


app = Flask(__name__)

# Configure your MySQL database connection here
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:new_password@localhost:3306/mydb'
db.init_app(app)

#test
@app.route('/khalil', methods=['GET'])
def hello_worldd():
    return customers.hello_world()

#add customer to DB:
@app.route('/create_customer', methods=['POST'])
def create_customer():
    return customers.create_customer()

#delete a costumer
@app.route('/delete_customer', methods=['POST'])
def delete_customer():
    return customers.delete_customer()

#update customer
@app.route('/update_customer_info', methods=['PATCH'])
def update_customer_info():
    return customers.update_customer_info()

#add good to DB:
@app.route('/add_good', methods = ['POST'])
def add_good():
    return inventory.add_good()

@app.route('/customers', methods=['GET'])
def get_all_customers():
    return customers.get_all_customers()

@app.route('/remove_stock', methods = ['PATCH'])
def remove_stock():
    return inventory.remove_stock()

@app.route('/update_good_info', methods = ['PATCH'])
def update_good_info():
    return inventory.update_good_info()

@app.route('/get_customer_by_username', methods=['GET'])
def get_customer_by_username():
    return customers.get_customer_by_username()

@app.route('/charge_wallet', methods=['PATCH'])
def charge_wallet():
    return customers.charge_wallet()

@app.route('/display_available_goods', methods = ['GET'])
def display_available_goods():
    return sales.display_available_goods()

@app.route('/good_details', methods = ['GET'])
def good_details():
    return sales.good_details()

@app.route('/deduct_money', methods = ['PATCH'])
def deduct_money():
    return customers.deduct_money()

@app.route('/make_sale', methods = ['PATCH'])
def make_sale():
    return sales.make_sale()

@app.route('/get_payment_history', methods = ['GET'])
def get_payment_history():
    return sales.get_payment_history()