import pytest
from src.product_4 import Product
from src.category_4 import Category

def test_product_zero_quantity():
    """Проверка создания продукта с нулевым количеством"""
    with pytest.raises(ValueError) as excinfo:
        Product("Тест", "Описание", 100.0, 0)
    assert "Товар с нулевым количеством не может быть добавлен" in str(excinfo.value)

def test_product_creation():
    """Проверка корректного создания продукта"""
    product = Product("Телефон", "Смартфон", 10000.0, 5)
    assert product.name == "Телефон"
    assert product.price == 10000.0
    assert product.quantity == 5

def test_middle_price_with_products():
    """Проверка расчета средней цены"""
    p1 = Product("Товар1", "Описание", 100.0, 2)
    p2 = Product("Товар2", "Описание", 200.0, 3)
    category = Category("Категория", "Описание", [p1, p2])
    assert category.middle_price() == 150.0

def test_middle_price_empty_category():
    """Проверка пустой категории"""
    category = Category("Пустая", "Категория")
    assert category.middle_price() == 0.0

def test_middle_price_with_zero_prices():
    """Проверка расчета с нулевыми ценами"""
    p1 = Product("Товар1", "Описание", 0.0, 2)
    p2 = Product("Товар2", "Описание", 0.0, 3)
    category = Category("Категория", "Описание", [p1, p2])
    assert category.middle_price() == 0.0