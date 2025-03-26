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
    s = Smartphone("iPhone", "Флагман", 80000, 1,
                  "A15", "13", "128GB", "Black")
    assert isinstance(s, Product)
    assert isinstance(s, BaseProduct)