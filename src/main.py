from src.category import Category
from src.utils import load_data_from_json


def main() -> None:
    # Загрузка данных из JSON
    categories = load_data_from_json(
        r"C:\Users\Pavel\PycharmProjects\oop_homework\data\products.json"
    )

    # Вывод информации о категориях и товарах
    for category in categories:
        print(f"Категория: {category.name}")
        print(f"Описание: {category.description}")
        print(f"Количество товаров: {len(category.products)}")
        for product in category.products:
            print(
                f"  Товар: {product.name}, Цена: {product.price}, Количество: {product.quantity}"
            )
        print()

    # Вывод общей статистики
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")


if __name__ == "__main__":
    main()
