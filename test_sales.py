"""
test_sales.py
-------------------

This module contains test functions for the sales-related operations.

"""

import json
import pytest
from app import app
from flask import jsonify

def test_good_details():
    data = {
        "Name" : "banana"
    }
    response = app.test_client().get('/good_details', json=data)
    assert response.status_code == 200

def test_nonexisting_good_details():
    data = {
        "Name" : "melon"
    }
    response = app.test_client().get('/good_details', json=data)
    assert response.status_code == 404
    assert b"Good name is not found" in response.data

def test_make_sale():
    data = {
        "Name" : "banana",
        "Username" : "khil"
    }
    response = app.test_client().patch('/make_sale', json=data)
    assert response.status_code == 200
    assert b"Sale completed successfully" in response.data


def test_make_sale_nonexisting_good():
    data = {
        "Name" : "melon",
        "Username" : "khil"
    }
    response = app.test_client().patch('/make_sale', json=data)
    assert response.status_code == 404
    assert b"Good or customer not found" in response.data


def test_make_sale_out_of_stock_good():
    data = {
        "Name" : "banana",
        "Username" : "wsy"
    }
    response = app.test_client().patch('/make_sale', json=data)
    assert response.status_code == 400
    assert b"Good is out of stock" in response.data


def test_make_sale_insufficient_finds():
    data = {
        "Name" : "apple",
        "Username" : "ryj"
    }
    response = app.test_client().patch('/make_sale', json=data)
    assert response.status_code == 400
    assert b"Insufficient funds" in response.data


def test_get_payment_history():
    data = {
        "Username" : "khb"
    }
    response = app.test_client().get('/get_payment_history', json=data)
    assert response.status_code == 200


def test_get_payment_history_nonexisting_user():
    data = {
        "Username" : "sfhb"
    }
    response = app.test_client().get('/get_payment_history', json=data)
    assert response.status_code == 404
    assert b"Payment history not found" in response.data
