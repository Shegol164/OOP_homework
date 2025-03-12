class Category:
    """Класс для представления категории товаров."""

    # Атрибуты класса
    category_count = 0
    product_count = 0

    def __init__(
        self,
        name: str,
        description: str,
        products: list,
    ):
        """
        Инициализация категории.
        :param name: Название категории.
        :param description: Описание категории.
        :param products: Список товаров в категории.
        """
        self.name = name
        self.description = description
        self.products = products
        # Обновление атрибутов класса
        Category.category_count += 1
        Category.product_count += len(products)
