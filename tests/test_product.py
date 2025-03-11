import pytest

from src.product import Product


@pytest.fixture
def sample_product():
    return Product(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        price=180000.0,
        quantity=5,
    )


def test_product_initialization(sample_product):
    assert sample_product.name == "Смартфоны"
    assert (
        sample_product.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert sample_product.price == 180000.0
    assert sample_product.quantity == 5
