class Product:
    """Класс для представления товара в магазине."""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Инициализирует экземпляр класса Product.

        Args:
            name: Название товара
            description: Описание товара
            price: Цена товара
            quantity: Количество товара на складе

        Raises:
            ValueError: Если количество товара равно нулю
        """
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта Product."""
        return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"
