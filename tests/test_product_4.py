import pytest
from src.product_4 import Product
from src.category_4 import Category

def test_product_zero_quantity() -> None:
    """Проверяет вызов исключения при создании товара с нулевым количеством."""
    with pytest.raises(ValueError) as excinfo:
        Product("Бракованный", "Товар", 100.0, 0)
    assert str(excinfo.value) == "Товар с нулевым количеством не может быть добавлен"

def test_middle_price_with_products() -> None:
    """Проверяет корректный расчет средней цены для категории с товарами."""
    p1 = Product("Товар1", "Описание", 100.0, 2)
    p2 = Product("Товар2", "Описание", 200.0, 3)
    category = Category("Категория", "Описание", [p1, p2])
    assert category.middle_price() == 150.0

def test_middle_price_empty_category() -> None:
    """Проверяет возврат нуля для пустой категории."""
    category = Category("Пустая", "Категория")
    assert category.middle_price() == 0.0