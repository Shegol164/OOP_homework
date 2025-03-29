from typing import Optional, List
from src.product_4 import Product


class Category:
    """Класс для представления категории товаров."""

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
        """
        Инициализирует экземпляр класса Category.

        Args:
            name: Название категории
            description: Описание категории
            products: Список товаров в категории (по умолчанию пустой)
        """
        self.name = name
        self.description = description
        self.products = products if products else []

    def middle_price(self) -> float:
        """
        Рассчитывает среднюю цену товаров в категории.

        Returns:
            Средняя цена товаров или 0, если в категории нет товаров
        """
        try:
            total = sum(p.price for p in self.products)
            return total / len(self.products)
        except ZeroDivisionError:
            return 0.0

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта Category."""
        return f"Category(name='{self.name}', products={len(self.products)} items)"
