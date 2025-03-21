from src.category import Category
from src.utils import load_data_from_json
from src.product import Product


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
