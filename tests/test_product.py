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


@pytest.fixture
def sample_product():
    return Product(name="Смартфоны",
                   description="Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
                   price=180000.0, quantity=5)


def test_price_setter(sample_product):
    sample_product.price = -500
    assert sample_product.price == 180000.0  # Цена не изменилась
    sample_product.price = 189000.0
    assert sample_product.price == 189000.0  # Цена изменилась


def test_new_product():
    data = {"name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
            "price": 123000.0, "quantity": 7}
    p = Product.new_product(data)
    assert p.name == "Телевизоры"
    assert p.price == 123000.0


@pytest.fixture
def sample_product():
    return Product(name="Смартфон",
                   description="Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
                   price=180000.0, quantity=5)


def test_product_str(sample_product):
    assert str(sample_product) == "Смартфон, 180000.0 руб. Остаток: 5 шт."


def test_product_addition(sample_product):
    product2 = Product("Телевизоры",
                       "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                       123000.0, 7)
    assert sample_product + product2 == 180000.0 * 5 + 123000.0 * 7
