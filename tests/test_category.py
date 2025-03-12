import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def sample_category():
    products = [
        Product(
            name="Смартфоны",
            description="Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
            price=180000.0,
            quantity=5,
        ),
        Product(
            name="Телевизоры",
            description="Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
            price=123000.0,
            quantity=7,
        ),
    ]
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        products=products,
    )


def test_category_initialization(sample_category):
    assert sample_category.name == "Смартфоны"
    assert (
        sample_category.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert len(sample_category.products) == 2


def test_category_count(sample_category):
    assert Category.category_count > 0


def test_product_count(sample_category):
    assert Category.product_count >= len(sample_category.products)
