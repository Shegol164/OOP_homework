class Product:
    """Класс для представления товара"""

    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int,
    ):
        """
        Инициализация товара.

        :param name: Название товара.
        :param description: Описание товара.
        :param price: Цена товара.
        :param quantity: Количество товара в наличии.
        """
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут цены
        self.quantity = quantity

    def __str__(self):
        """Строковое представление продукта"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """
        Магический метод сложения.
        Возвращает сумму произведений цены на количество для двух продуктов.
        """
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product.")
        return (self.price * self.quantity) + (other.price * other.quantity)

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"

    @classmethod
    def new_product(cls, product_data: dict, products: list = None):
        """
        Класс-метод для создания нового товара.
        Если товар с таким именем уже существует, обновляет его количество и цену.
        """
        if products:
            for product in products:
                if product.name == product_data["name"]:
                    product.quantity += product_data["quantity"]
                    if product_data["price"] > product.price:
                        product.price = product_data["price"]
                    return product
        return cls(**product_data)

    @property
    def price(self):
        """Геттер для цены."""
        return self.__price

    @price.setter
    def price(self, value: float):
        """
        Сеттер для цены с проверкой на положительное значение.
        Если цена понижается, запрашивает подтверждение у пользователя.
        """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if value < self.__price:
            confirm = input("Подтвердите снижение цены (y/n): ")
            if confirm.lower() != "y":
                print("Изменение цены отменено")
                return

        self.__price = value
