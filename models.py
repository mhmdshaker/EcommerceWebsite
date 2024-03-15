"""
models.py
----------

This module defines the SQLAlchemy models for the application.

"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Numeric

db = SQLAlchemy()

       
#Define the Customer model
class Customer(db.Model):
    """
    Represents a customer in the database.

    Attributes:
        Fullname (str): Full name of the customer.
        Username (str): Unique username for the customer (primary key).
        Password (str): Password for the customer.
        Age (int): Age of the customer.
        Address (str): Address of the customer.
        Gender (Enum): Gender of the customer (Male, Female).
        MaritalStatus (Enum): Marital status of the customer.
        wallet (Numeric): Wallet balance of the customer.

    """
    Fullname = db.Column(db.String(255), nullable=False)
    Username = db.Column(db.String(255), unique=True, nullable=False, primary_key=True)
    Password = db.Column(db.String(255), nullable=False)
    Age = db.Column(db.Integer)
    Address = db.Column(db.String(255))
    Gender = db.Column(db.Enum('Male', 'Female'))
    MaritalStatus = db.Column(db.Enum('Single', 'Married', 'Divorced', 'Widowed'))
    wallet = db.Column(db.Numeric(10, 2), nullable=False, default=0.00)

#Define the Goods model
class Goods(db.Model):
    """
    Represents a product in the inventory.

    Attributes:
        Name (str): Name of the product (primary key).
        Category (Enum): Category of the product.
        Price_per_item (Numeric): Price per item of the product.
        Description (str): Description of the product.
        Count_of_available_items (int): Count of available items in the inventory.
        payment_history_username (str): Username linked to payment history.

    """
    __tablename__ = 'goods'
    Name = db.Column(db.String(255), primary_key=True, nullable=False)
    Category = db.Column(db.Enum('food', 'clothes', 'accessories', 'electronics'), nullable=False)
    Price_per_item = db.Column(db.Numeric(10, 2), nullable=False)
    Description = db.Column(db.String(225))
    Count_of_available_items = db.Column(db.Integer, nullable=False)
    payment_history_username = db.Column(db.String(225), db.ForeignKey('payment_history.customer_username'), nullable=False)

#Define the Payment_History model
class Payment_History(db.Model):
    """
    Represents the payment history of a customer.

    Attributes:
        customer_username (str): Username of the customer (primary key).
        goods (relationship): Relationship with the Goods model.

    """
    __tablename__ = 'payment_history'
    customer_username = db.Column(db.String(225), primary_key=True, nullable=False)
    goods = db.relationship('Goods', backref='payment_history_user', lazy=True)
