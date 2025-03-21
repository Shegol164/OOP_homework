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
        self.__products = products  # Приватный атрибут списка товаров
        # Обновление атрибутов класса
        Category.category_count += 1
        Category.product_count += len(products)

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products  # Приватный атрибут списка товаров
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        """Строковое представление категории."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product):
        """Добавляет товар в категорию."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер для списка товаров. Возвращает строку с информацией о товарах."""
        return "\n".join(
            [
                f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт."
                for p in self.__products
            ]
        )

    def __len__(self):
        return len(self.__products)

    def __repr__(self):
        return f"Category(name={self.name}, products={self.__products})"
