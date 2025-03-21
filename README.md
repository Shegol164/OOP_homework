# Учебный проект по Python : 
Объектно-ориентированное программирование



## Описание:
Данный учебный проект содержит материалы заданий уроков:
- 14.1 Введение в ООП
- 14.2 Режимы доступа
- 15.1 Магические методы


## Установка:
   1. Клонируйте репозиторий:
https://github.com/Shegol164/OOP_homework.git
   2. Перейдите в директорию проекта:
 OOP_homework

## Использование:
Для запуска main использовать:
from src.utils import load_data_from_json
from src.category import Category
Пример main:
def main() -> None:
    # Загрузка данных из JSON
    categories = load_data_from_json(
        r"C:\Users\Pavel\PycharmProjects\oop_homework\data\products.json"
    )

    # Вывод информации о категориях и товарах
    for category in categories:
        print(f"Категория: {category.name}")
        print(f"Описание: {category.description}")
        print(f"Количество товаров: {len(category)}")
        print("Товары:")
        print(category.products)
        print()
    print("#" * 119)

    # Вывод общей статистики
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")
    print("#" * 119)

    # Вывод информации о категориях и товарах
    for category in categories:
        print(category)  # Используем __str__ для категории
        print("Товары:")
        for product in category._Category__products:  # Итерация по товарам
            print(product)  # Используем __str__ для продукта
        print()

    # Пример сложения продуктов
    product1 = Product("Смартфон",
                       "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
                       180000.0, 5)
    product2 = Product("Телевизоры",
                       "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                       123000.0, 7)
    total_value = product1 + product2
    print(f"Общая стоимость товаров: {total_value} руб.")

if __name__ == "__main__":
    main()

# Тесты
Для всех функций написаны подробные тесты в папке tests:
- test_category
- test_product


Протестированы разные сценарий формата ввода и вывода 

## Например: test_category
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


@pytest.fixture
def sample_category():
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
                    [])

def test_category_str(sample_category):
    p1 = Product("Смартфоны",
                     "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
                     180000.0, 5)
    p2 = Product("Телевизоры",
                     "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                     123000.0, 7)
    sample_category.add_product(p1)
    sample_category.add_product(p2)
    assert str(sample_category) == "Смартфоны, количество продуктов: 12 шт."

