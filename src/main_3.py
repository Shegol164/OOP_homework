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
