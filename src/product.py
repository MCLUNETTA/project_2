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
        """Складывает два продукта, возвращая сумму произведений цены на количество."""
        if not isinstance(other, Product):
            raise TypeError("Складывать можно только объекты класса Product")
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
        # Подсчитываем общее количество товаров на складе для всех продуктов в этой категории
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в приватный список товаров и увеличивает общий счетчик продуктов."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер, возвращающий список продуктов в виде отформатированных строк."""
        # Оптимизировали геттер: теперь он превращает объект продукта в строку через str(product)
        return "".join([f"{str(product)}\n" for product in self.__products])
