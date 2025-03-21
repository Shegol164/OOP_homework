import json
from typing import List

from src.category import Category
from src.product import Product


def load_data_from_json(filepath: str) -> List[Category]:
    """
    Загружает данные о категориях и товарах из JSON-файла.

    :param filepath: Путь к JSON-файлу.
    :return: Список объектов Category.
    """
    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)

    categories = []
    for category_data in data:
        products = [
            Product.new_product(product_data)
            for product_data in category_data["products"]
        ]
        category = Category(
            name=category_data["name"],
            description=category_data["description"],
            products=products,
        )
        categories.append(category)

    return categories


if __name__ == "__main__":
    categories = load_data_from_json(
        r"C:\Users\Pavel\PycharmProjects\oop_homework\data\products.json"
    )
    for category in categories:
        print(f"Категория: {category.name}, Товаров: {len(category.products)}")
