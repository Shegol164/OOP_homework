from src.product_4 import Product
from src.category_4 import Category


def main() -> None:
    """Основная функция для демонстрации работы классов."""
    try:
        # Попытка создать товар с нулевым количеством
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством")
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    try:
        # Создание корректных товаров
        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

        # Создание категории с товарами
        category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])
        print(f"Средняя цена: {category1.middle_price():.2f} руб.")

        # Создание пустой категории
        category_empty = Category("Пустая категория", "Категория без продуктов")
        print(f"Средняя цена пустой категории: {category_empty.middle_price():.2f} руб.")

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == '__main__':
    main()
