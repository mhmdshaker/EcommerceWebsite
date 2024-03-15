"""
test_customers.py
-------------------

This module contains test functions for the customer-related operations.

"""

import json
import pytest
from app import app
from flask import jsonify

def test_create_customer():
    """
    Test the creation of a new customer.

    Creates a new customer using a sample data and checks if the response
    indicates successful creation.

    """
    data = {
        "Fullname": "ece435x",
        "Username": "ece435x",
        "Password": "hello123",
        "Age": 20,
        "Address": "aub",
        "Gender": "Male",
        "MaritalStatus": "Single",
        "wallet": 3804.70
    }
    response = app.test_client().post('/create_customer', json=data)
    assert response.status_code == 201
    assert b"Customer created successfully" in response.data


# def test_create_existing_customer():

#     data = {
#         "Fullname": "Mohamad Shaker",
#         "Username": "khb",
#         "Password": "pass",
#         "Age": 20,
#         "Address": "hamra",
#         "Gender": "Male",
#         "MaritalStatus": "Married",
#         "wallet": 100.00
#     }
#     response = app.test_client().post('/create_customer', json=data)
#     assert response.status_code ==

# Additional test functions for create_existing_customer, delete_customer,
# delete_nonexisting_customer, update_customer_info, update_nonexisting_customer_info,
# get_customer_by_username, get_nonexisting_customer_by_username, charge_wallet,
# negative_charge_wallet, nonexisting_customer_charge_wallet, deduct_money,
# deduct_nonexisting_customer_money, negative_deduct_wallet.

# def test_delete_customer():

#     data = {
#         "Username" : "ryj01"
#     }
#     response = app.test_client().post('/delete_customer', json=data)
#     assert response.status_code == 200
#     assert b"Customer deleted successfully" in response.data

# def test_delete_nonexisting_customer():
#     data = {
#         "Username" : "mmm"
#     }
#     response = app.test_client().post('/delete_customer', json=data)
#     assert response.status_code == 404
#     assert b"Customer not found" in response.data


# def test_update_customer_info():
#     data = {
#         "Fullname": "Khalil Bitar",
#         "Username": "khil",
#         "Password": "password123",
#         "Age": 20,
#         "Address": "bliss",
#         "Gender": "Male",
#         "MaritalStatus": "Single",
#         "wallet": 100.00
#     }
#     response = app.test_client().patch('/update_customer_info', json=data)
#     assert response.status_code == 200
#     assert b"Customer information updated successfully" in response.data

# def test_update_nonexisting_customer_info():
#     data = {
#         "Fullname": "Khalil Bitar",
#         "Username": "ece435",
#         "Password": "password123",
#         "Age": 20,
#         "Address": "bliss",
#         "Gender": "Male",
#         "MaritalStatus": "Single",
#         "wallet": 100.00
#     }
#     response = app.test_client().patch('/update_customer_info', json=data)
#     assert response.status_code == 404
#     assert b"Customer not found" in response.data


# def test_get_customer_by_username():

#     data = {
#         "Username" : "khil"
#     }
#     response = app.test_client().get('/get_customer_by_username', json=data)
#     assert response.status_code == 200

# def test_get_nonexisting_customer_by_username():

#     data = {
#         "Username" : "mmm"
#     }
#     response = app.test_client().get('/get_customer_by_username', json=data)
#     assert response.status_code == 404
#     assert b"Customer not found" in response.data


# def test_charge_wallet():
#     data = {
#         "Username" : "khil",
#         "Amount_to_charge" : 10
#     }
#     response = app.test_client().patch('/charge_wallet', json=data)
#     assert response.status_code == 200
#     assert b"Customer wallet charged successfully" in response.data

# def test_negative_charge_wallet():
#     data = {
#         "Username" : "",
#         "Amount_to_charge" : -10
#     }
#     response = app.test_client().patch('/charge_wallet', json=data)
#     assert response.status_code == 400
#     assert b"Amount to charge should be non-negative" in response.data

# def test_nonexisting_customer_charge_wallet():
#     data = {
#         "Username" : "mmm",
#         "Amount_to_charge" : 10
#     }
#     response = app.test_client().patch('/charge_wallet', json=data)
#     assert response.status_code == 404
#     assert b"Customer not found" in response.data

# def test_deduct_money():
#     data = {
#         "Username" : "khil",
#         "Amount_to_deduct" : 10
#     }
#     response = app.test_client().patch('/deduct_money', json=data)
#     assert response.status_code == 200
#     assert b"Deducted from customer wallet successfully" in response.data

# def test_deduct_nonexisting_customer_money():
#     data = {
#         "Username" : "mmm",
#         "Amount_to_deduct" : 10
#     }
#     response = app.test_client().patch('/deduct_money', json=data)
#     assert response.status_code == 404
#     assert b"Customer not found" in response.data

# def test_negative_charge_wallet():
#     data = {
#         "Username" : "khb",
#         "Amount_to_deduct" : -10
#     }
#     response = app.test_client().patch('/deduct_money', json=data)
#     assert response.status_code == 400
#     assert b"Amount to deduct should be non-negative" in response.data