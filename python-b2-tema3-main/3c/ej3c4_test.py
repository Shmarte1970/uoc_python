from ej3c4 import apply_discount
from functools import partial


def apply_discount(price: float, discount: float) -> float:
    """Applies a discount to the price and returns the final price."""
    return price - (price * discount / 100)

# Create specialized discount functions
vip_discount = partial(apply_discount, discount=20)
new_customer_discount = partial(apply_discount, discount=10)

def test_apply_discount():
    # Test the generic discount function
    assert apply_discount(100, 20) == 80
    assert apply_discount(100, 10) == 90

def test_vip_discount():
    # Test the VIP discount
    assert vip_discount(100) == 80

def test_new_customer_discount():
    # Test the new customer discount
    assert new_customer_discount(100) == 90
