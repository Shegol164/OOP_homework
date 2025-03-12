# Учебный проект по Python : 
Объектно-ориентированное программирование



## Описание:
Данный учебный проект содержит материалы заданий уроков:
- 14.1 Введение в ООП


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
def main():
    categories = load_data_from_json(r"C:\Users\Pavel\PycharmProjects\oop_homework\data\products.json")
    for category in categories:
        print(f"Категория: {category.name}")
        print(f"Описание: {category.description}")
        print(f"Количество товаров: {len(category.products)}")
        for product in category.products:
            print(f"  Товар: {product.name}, Цена: {product.price}, Количество: {product.quantity}")
        print()
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")

if __name__ == "__main__":
    main()

# Тесты
Для всех функций написаны подробные тесты в папке tests:
- test_category
- test_product


Протестированы разные сценарий формата ввода и вывода 

## Например: test_category
-@pytest.fixture
def sample_category():
    products = [
        Product(name="Смартфоны",
                description="Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
                price=180000.0, quantity=5),
        Product(name="Телевизоры",
                description="Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                price=123000.0, quantity=7),
    ]
    return Category(name="Смартфоны",
                    description="Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
                    products=products)


def test_category_initialization(sample_category):
    assert sample_category.name == "Смартфоны"
    assert sample_category.description == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    assert len(sample_category.products) == 2


def test_category_count(sample_category):
    assert Category.category_count > 0


def test_product_count(sample_category):
    assert Category.product_count >= len(sample_category.products)