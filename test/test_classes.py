import pytest

from product import BaseProduct, Category, LawnGrass, Product, Smartphone


def test_base_product_is_abstract():
    """Проверяем, что BaseProduct является абстрактным и его нельзя инициализировать напрямую."""
    with pytest.raises(TypeError):
        BaseProduct()


def test_product_creation_and_mixin(capsys):
    """Проверяем создание продукта, работу миксина (вывод в консоль) и атрибуты."""
    product = Product("Яблоко", "Красное свежее", 100.0, 50)
    captured = capsys.readouterr()

    assert "Product" in captured.out
    assert product.name == "Яблоко"
    assert product.description == "Красное свежее"
    assert product.price == 100.0
    assert product.quantity == 50


def test_product_zero_quantity():
    """Проверяем выброс ValueError при создании товара с нулевым количеством."""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)


def test_product_price_setter():
    """Проверяем работу сеттера цены (включая защиту от некорректных значений)."""
    product = Product("Товар", "Описание", 200.0, 10)

    product.price = 250.0
    assert product.price == 250.0

    product.price = -50
    assert product.price == 250.0


def test_product_new_product():
    """Проверяем класс-метод создания товара из словаря."""
    data = {"name": "Груша", "description": "Сладкая", "price": 150.0, "quantity": 20}
    product = Product.new_product(data)
    assert product.name == "Груша"
    assert product.price == 150.0
    assert product.quantity == 20


def test_smartphone_creation():
    """Проверяем корректность создания класса Smartphone."""
    phone = Smartphone("Samsung", "Galaxy S23", 75000.0, 10, "high", "S23", "128GB", "Black")
    assert phone.name == "Samsung"
    assert phone.price == 75000.0
    assert phone.efficiency == "high"
    assert phone.model == "S23"
    assert phone.memory == "128GB"
    assert phone.color == "Black"


def test_lawn_grass_creation():
    """Проверяем корректность создания класса LawnGrass."""
    grass = LawnGrass("Газонная трава", "Изумрудная", 500.0, 20, "Россия", "7 дней", "Зеленый")
    assert grass.name == "Газонная трава"
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"


def test_category_creation_and_add_product():
    """Проверяем создание категории, добавление товаров и вывод списка."""
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product("Товар 1", "Описание 1", 100.0, 5)
    product2 = Product("Товар 2", "Описание 2", 200.0, 10)
    category = Category("Категория", "Описание категории", [product1])

    assert category.name == "Категория"
    assert Category.category_count == 1
    assert Category.product_count == 1

    category.add_product(product2)
    assert Category.product_count == 2
    assert "Товар 1, 100.0 руб. Остаток: 5 шт." in category.products
    assert "Товар 2, 200.0 руб. Остаток: 10 шт." in category.products


def test_category_add_invalid_product():
    """Проверяем защиту от добавления неверного типа объекта в категорию."""
    category = Category("Категория", "Описание")
    with pytest.raises(TypeError):
        category.add_product("Не товар")


def test_category_middle_price():
    """Проверяем подсчет среднего ценника товаров в категории."""
    product1 = Product("Товар 1", "Описание 1", 100.0, 5)
    product2 = Product("Товар 2", "Описание 2", 200.0, 10)
    category = Category("Тестовая категория", "Описание", [product1, product2])
    assert category.middle_price() == 150.0


def test_category_middle_price_empty():
    """Проверяем возврат 0 при подсчете среднего ценника в пустой категории."""
    empty_category = Category("Пустая категория", "Нет товаров", [])
    assert empty_category.middle_price() == 0
