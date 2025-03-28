from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Абстрактный базовый класс для товаров"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self) -> str:
        pass


class LogMixin:
    """Миксин для логирования создания объектов"""

    def __init__(self, *args, **kwargs):
        """Логирует параметры создания объекта"""
        print(f"Создан объект {self.__class__.__name__}")
        print(f"Аргументы: {args}, Ключевые аргументы: {kwargs}")
        super().__init__(*args, **kwargs)


class Product(LogMixin, BaseProduct):
    """Конкретный класс продукта"""

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: 'Product') -> float:
        if type(self) != type(other):
            raise TypeError("Нельзя складывать разные типы продуктов")
        return self.price * self.quantity + other.price * other.quantity


class Smartphone(Product):
    """Класс для смартфонов"""

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для газонной травы"""

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
