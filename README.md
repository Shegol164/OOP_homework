# Учебный проект по Python : 
Объектно-ориентированное программирование



## Описание:
Данный учебный проект содержит материалы заданий уроков:
- 14.1 Введение в ООП
- 14.2 Режимы доступа
- 15.1 Магические методы
- 16.1 Наследование
- 16.2 Множественное наследование


## Установка:
   1. Клонируйте репозиторий:
https://github.com/Shegol164/OOP_homework.git
   2. Перейдите в директорию проекта:
 OOP_homework

## Использование:
Для запуска main использовать:
from src.utils import load_data_from_json
from src.category import Category
### main:
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
### main 2:
from src.product_2 import Product, Smartphone, LawnGrass
from src.category_2 import Category

def main() -> None:
    # Создаем смартфоны
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый"
    )
    smartphone2 = Smartphone(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8,
        98.2,
        "15",
        512,
        "Gray space"
    )
    smartphone3 = Smartphone(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14,
        90.3,
        "Note 11",
        1024,
        "Синий"
    )

    # Выводим информацию о смартфонах
    for smartphone in [smartphone1, smartphone2, smartphone3]:
        print(f"Название: {smartphone.name}")
        print(f"Описание: {smartphone.description}")
        print(f"Цена: {smartphone.price} руб.")
        print(f"Количество: {smartphone.quantity} шт.")
        print(f"Производительность: {smartphone.efficiency}%")
        print(f"Модель: {smartphone.model}")
        print(f"Память: {smartphone.memory}GB")
        print(f"Цвет: {smartphone.color}\n")

    # Создаем газонную траву
    grass1 = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый"
    )
    grass2 = LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый"
    )

    # Выводим информацию о газонной траве
    for grass in [grass1, grass2]:
        print(f"Название: {grass.name}")
        print(f"Описание: {grass.description}")
        print(f"Цена: {grass.price} руб.")
        print(f"Количество: {grass.quantity} шт.")
        print(f"Страна: {grass.country}")
        print(f"Срок прорастания: {grass.germination_period}")
        print(f"Цвет: {grass.color}\n")

    # Демонстрация сложения товаров
    smartphone_sum = smartphone1 + smartphone2
    print(f"Общая стоимость смартфонов: {smartphone_sum} руб.")

    grass_sum = grass1 + grass2
    print(f"Общая стоимость газонной травы: {grass_sum} руб.")

    # Попытка сложить разные типы товаров
    try:
        invalid_sum = smartphone1 + grass1
    except TypeError as e:
        print(f"Ошибка при сложении разных типов: {e}")

    # Работа с категориями
    category_smartphones = Category(
        "Смартфоны",
        "Высокотехнологичные смартфоны",
        [smartphone1, smartphone2]
    )
    category_grass = Category(
        "Газонная трава",
        "Различные виды газонной травы",
        [grass1, grass2]
    )

    # Добавление товара в категорию
    category_smartphones.add_product(smartphone3)
    print("\nТовары в категории 'Смартфоны':")
    print(category_smartphones.products)

    # Вывод общего количества продуктов
    print(f"\nОбщее количество продуктов: {Product.product_count}")

    # Попытка добавить не товар в категорию
    try:
        category_smartphones.add_product("Not a product")
    except TypeError as e:
        print(f"Ошибка при добавлении не товара: {e}")


if __name__ == "__main__":
    main()

### main 3:
from src.product_3 import Smartphone, LawnGrass


def main():
    # Создание продуктов с логированием
    phone = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый"
    )

    grass = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый"
    )

    # Вывод информации о продуктах
    print("\nИнформация о продуктах:")
    print(phone)
    print(grass)


if __name__ == "__main__":
    main()

# Тесты
Для всех функций написаны подробные тесты в папке tests:
- test_category
- test_product
- test_category_2
- test_product_2 


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

## Например: test_category_2

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

## Например: test_product_3
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