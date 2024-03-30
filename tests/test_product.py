import pytest
from src.product import Product


@pytest.fixture
def for_product():
    return Product("Xiaomi Redmi Note 11",
                   "1024GB, Синий",
                   31000.0, 14)

def test_init(for_product):
    assert for_product_1.name == "Xiaomi Redmi Note 11"
    assert for_product_1.description == "1024GB, Синий"
    assert for_product_1.price == 31000.0
    assert for_product_1.quantity == 14