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