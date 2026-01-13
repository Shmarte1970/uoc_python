import pytest
from ej3a1 import Book, Electronic, Clothing, Order


def test_product_creation():
    book = Book("Test Book", 10.0, "Test Author", "1234567890")
    assert book._name == "Test Book"
    assert book.price == 10.0
    assert book.author == "Test Author"
    assert book.isbn == "1234567890"


def test_product_price_setting():
    electronic = Electronic("Test Electronic", 100.0, "Test Brand", "Test Model")
    electronic.price = 150.0
    assert electronic.price == 150.0


def test_product_negative_price_setting():
    clothing = Clothing("Test Clothing", 20.0, "L", "Red")
    with pytest.raises(ValueError):
        clothing.price = -10.0

def test_order_addition_and_total_calculation():
    order = Order()
    order.add_product(Book("Test Book", 10.0, "Test Author", "1234567890"))
    order.add_product(Electronic("Test Electronic", 100.0, "Test Brand", "Test Model"))
    order.add_product(Clothing("Test Clothing", 20.0, "L", "Red"))
    assert len(order.products) == 3
    assert order.calculate_total() == 130.0


def test_product_description():
    book = Book("Test Book", 10.0, "Test Author", "1234567890")
    description = book.describe_product()
    assert description == "Book: Test Book, Author: Test Author, ISBN: 1234567890, Price: $10.0"
