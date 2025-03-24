import pytest
from src.product_2 import Product, Smartphone, LawnGrass

@pytest.fixture
def sample_product():
    return Product("Телефон", "Смартфон", 10000, 5)

@pytest.fixture
def sample_smartphone():
    return Smartphone("iPhone", "Флагман", 80000, 3, 95.5, "15 Pro", 256, "Black")

@pytest.fixture
def sample_lawn_grass():
    return LawnGrass("Газон", "Элитный", 500, 10, "Россия", "14 дней", "Зеленый")

def test_product_creation(sample_product):
    assert sample_product.name == "Телефон"
    assert sample_product.description == "Смартфон"
    assert sample_product.price == 10000
    assert sample_product.quantity == 5

def test_smartphone_creation(sample_smartphone):
    assert sample_smartphone.name == "iPhone"
    assert sample_smartphone.efficiency == 95.5
    assert sample_smartphone.model == "15 Pro"
    assert sample_smartphone.memory == 256
    assert sample_smartphone.color == "Black"

def test_lawn_grass_creation(sample_lawn_grass):
    assert sample_lawn_grass.name == "Газон"
    assert sample_lawn_grass.country == "Россия"
    assert sample_lawn_grass.germination_period == "14 дней"
    assert sample_lawn_grass.color == "Зеленый"

def test_product_str(sample_product):
    assert str(sample_product) == "Телефон, 10000 руб. Остаток: 5 шт."

def test_smartphone_str(sample_smartphone):
    assert "iPhone" in str(sample_smartphone)
    assert "80000" in str(sample_smartphone)

def test_product_addition_same_type(sample_product):
    p2 = Product("Наушники", "Беспроводные", 5000, 2)
    assert sample_product + p2 == 10000*5 + 5000*2

def test_product_addition_different_types(sample_product, sample_smartphone):
    with pytest.raises(TypeError, match="Нельзя складывать товары разных типов"):
        sample_product + sample_smartphone

def test_product_count(sample_product, sample_smartphone, sample_lawn_grass):
    assert Product.product_count >= 3  # Проверяем, что счетчик увеличивается