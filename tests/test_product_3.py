import pytest
from src.product_3 import BaseProduct, Product, Smartphone

def test_base_product_is_abstract():
    with pytest.raises(TypeError):
        BaseProduct("Test", "Test", 100, 1)

def test_product_creation(capsys):
    p = Product("Телефон", "Смартфон", 10000, 5)
    captured = capsys.readouterr()
    assert "Создан объект Product" in captured.out
    assert str(p) == "Телефон, 10000 руб. Остаток: 5 шт."

def test_smartphone_inheritance():
    s = Smartphone("Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый")
    assert isinstance(s, Product)
    assert isinstance(s, BaseProduct)