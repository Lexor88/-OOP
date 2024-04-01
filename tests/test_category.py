import pytest
from src.category import Category
from src.product import Product


@pytest.fixture
def for_category():
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, но и "
                    "получение дополнительных функций для удобства жизни",
                    [Product("Samsung Galaxy C23 Ultra",
                             "256GB, Серый цвет, 200MP камера",
                             180000.0, 5),
                     Product("Iphone 15", "512GB, Gray space",
                             210000.0, 8)])


def test_init(for_category):
    assert for_category.name == "Смартфоны"
    assert for_category.description == ("Смартфоны, как средство не только "
                                        "коммуникации, но и "
                                        "получение дополнительных функций для "
                                        "удобства жизни")
    assert for_category.products.startswith("Samsung Galaxy C23 Ultra") is True
    assert Category.category_count == 1
    assert Category.products_count == 2
