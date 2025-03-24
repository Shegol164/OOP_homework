import pytest
from src.category_2 import Category
from src.product_2 import Product, Smartphone, LawnGrass

@pytest.fixture
def sample_category():
    return Category("Электроника", "Техника")

@pytest.fixture
def sample_products():
    return [
        Product("Телефон", "Смартфон", 10000, 5),
        Smartphone("iPhone", "Флагман", 80000, 3, 95.5, "15 Pro", 256, "Black"),
        LawnGrass("Газон", "Элитный", 500, 10, "Россия", "14 дней", "Зеленый")
    ]

def test_category_creation(sample_category):
    assert sample_category.name == "Электроника"
    assert sample_category.description == "Техника"
    assert len(sample_category.products.split('\n')) == 0  # Пустая категория

def test_add_product(sample_category, sample_products):
    for product in sample_products:
        sample_category.add_product(product)
    assert len(sample_category.products.split('\n')) == 3

def test_add_invalid_product(sample_category):
    with pytest.raises(TypeError, match="Можно добавлять только объекты Product или его наследников"):
        sample_category.add_product("Не товар")

def test_category_str(sample_category, sample_products):
    for product in sample_products[:2]:
        sample_category.add_product(product)
    assert "Электроника" in str(sample_category)
    assert "количество продуктов: 2" in str(sample_category)

def test_category_count(sample_category):
    initial_count = Category.category_count
    new_category = Category("Тест", "Тест")
    assert Category.category_count == initial_count + 1