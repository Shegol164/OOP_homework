from __future__ import annotations
from typing import List, Union
from src.product_2 import Product, Smartphone, LawnGrass


class Category:
    """Класс для представления категории товаров."""

    category_count = 0  # Счетчик всех категорий

    def __init__(
            self,
            name: str,
            description: str,
            products: List[Union[Product, Smartphone, LawnGrass]] = None
    ) -> None:
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.category_count += 1

    def add_product(self, product: Union[Product, Smartphone, LawnGrass]) -> None:
        if not isinstance(product, (Product, Smartphone, LawnGrass)):
            raise TypeError("Можно добавлять только объекты Product или его наследников")
        self.__products.append(product)

    @property
    def products(self) -> str:
        return "\n".join(str(product) for product in self.__products)

    def __str__(self) -> str:
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."