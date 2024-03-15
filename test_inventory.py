"""
test_inventory.py
-------------------

This module contains test functions for the inventory-related operations.

"""

import json
import pytest
from app import app
from flask import jsonify


def test_add_good():
    data = {
        "Name" : "cucumber",
        "Category" : "food",
        "Price_per_item" : 1,
        "Description" : "veggie",
        "Count_of_available_items" : 10
    }
    response = app.test_client().post('/add_good', json=data)
    assert response.status_code == 201
    assert b"Good added successfully" in response.data

def test_add_existing_good():
    data = {
        "Name" : "cucumber",
        "Category" : "food",
        "Price_per_item" : 1,
        "Description" : "veggie",
        "Count_of_available_items" : 10
    }
    response = app.test_client().post('/add_good', json=data)
    assert response.status_code == 400
    assert b"The item already exists, please update its fields instead" in response.data


def test_remove_stock():
    data = {
        "Name" : "banana",
        "Amount_to_be_removed" : 1
    }
    response = app.test_client().patch('/remove_stock', json=data)
    assert response.status_code == 200
    assert b"Amount count changed successfuly" in response.data


def test_remove_non_existing_stock():
    data = {
        "Name" : "melon",
        "Amount_to_be_removed" : 1
    }
    response = app.test_client().patch('/remove_stock', json=data)
    assert response.status_code == 404
    assert b"Good not found" in response.data

def test_update_good_info():
    data = {
        "Name" : "cucumber",
        "Category" : "food",
        "Price_per_item" : 2,
        "Description" : "veggie",
        "Count_of_available_items" : 70
    }
    response = app.test_client().patch('/update_good_info', json=data)
    assert response.status_code == 200
    assert b"Item (Good) information updated successfully" in response.data


def test_update_nonexisting_good_info():
    data = {
        "Name" : "melon",
        "Category" : "food",
        "Price_per_item" : 2,
        "Description" : "veggie",
        "Count_of_available_items" : 70
    }
    response = app.test_client().patch('/update_good_info', json=data)
    assert response.status_code == 404
    assert b"Name not found" in response.data