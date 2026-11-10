from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs):
        super().__init__()


class PrintCreationMixin:
    def __init__(self, *args, **kwargs):
        print(repr(self))
        super().__init__()

    def __repr__(self):
        # Формируем строковое представление со всеми атрибутами объекта
        attributes = ", ".join([f"{v!r}" for v in self.__dict__.values()])
        return f"{self.__class__.__name__}({attributes})"


class Product(PrintCreationMixin, BaseProduct):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена должна быть указана корректно (> 0)")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, product_data: dict, *args, **kwargs):
        return cls(**product_data)


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
