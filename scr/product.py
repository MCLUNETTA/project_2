class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    name: str
    description: str
    products: list

    # Атрибуты класса для подсчета общего количества категорий и товаров
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products

        # Увеличиваем счетчик категорий при создании объекта
        Category.category_count += 1
        # Увеличиваем общий счетчик товаров на количество элементов в списке продуктов этой категории
        Category.product_count += len(products)
