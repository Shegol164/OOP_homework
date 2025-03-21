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


@pytest.fixture
def sample_category():
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
                    [])


def test_add_product(sample_category):
    p = Product("Смартфоны",
                "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
                210000.0, 8)
    sample_category.add_product(p)
    assert len(sample_category) == 1
    assert Category.product_count == 1


def test_products_getter(sample_category):
    p = Product("Смартфоны",
                "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
                180000.0, 5)
    sample_category.add_product(p)
    assert "Смартфоны, 180000.0 руб. Остаток: 5 шт." in sample_category.products
