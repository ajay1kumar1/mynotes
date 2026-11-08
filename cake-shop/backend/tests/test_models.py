import pytest
from app.models import Cake, Order
from datetime import datetime

def test_cake_model():
    cake = Cake(
        name="Chocolate Cake",
        description="Rich chocolate",
        price=29.99,
        category="chocolate",
        ingredients=["flour", "cocoa", "sugar"]
    )
    assert cake.name == "Chocolate Cake"
    assert cake.price == 29.99
    assert cake.in_stock == True

def test_order_model():
    order = Order(
        customer_name="John Doe",
        customer_email="john@example.com",
        items=[{"name": "Cake", "qty": 1}],
        total_amount=29.99
    )
    assert order.customer_name == "John Doe"
    assert order.status == "pending"
