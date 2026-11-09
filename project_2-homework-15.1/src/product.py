class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        """Возвращает строковое представление продукта."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> float:
        """Складывает два продукта, если они принадлежат к одному и тому же классу."""
        if type(other) is not type(self):
            raise TypeError("Можно складывать только товары одинаковых классов")
        return (self.price * self.quantity) + (other.price * other.quantity)

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
        """Создает и возвращает объект класса Product на основе словаря."""
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    @property
    def price(self) -> float:
        """Геттер для получения значения цены."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для установки цены с проверкой на валидность."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    name: str
    description: str
    __products: list

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self) -> str:
        """Возвращает строковое представление категории."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в приватный список товаров с проверкой на тип."""
        if not isinstance(product, Product):
            raise TypeError(
                "В категорию можно добавлять только объекты класса Product или его наследников"
            )
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер, возвращающий список продуктов в виде отформатированных строк."""
        return "".join([f"{str(product)}\n" for product in self.__products])
