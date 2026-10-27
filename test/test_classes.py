import pytest

from src.product import Category, Product


@pytest.fixture
def sample_products():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray", 210000.0, 8)
    return product1, product2


@pytest.fixture
def sample_category(sample_products):
    product1, product2 = sample_products
    return Category("Смартфоны", "Устройства связи", [product1, product2])


def test_product_initialization(sample_products):
    product1, _ = sample_products
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_product_price_setter():
    product = Product("Test", "Desc", 100.0, 1)

    # Корректная установка цены
    product.price = 150.0
    assert product.price == 150.0

    # Некорректная установка цены (нулевая или отрицательная)
    product.price = 0
    assert product.price == 150.0  # Цена не должна измениться

    product.price = -50.0
    assert product.price == 150.0


def test_category_initialization(sample_category, sample_products):
    product1, product2 = sample_products
    assert sample_category.name == "Смартфоны"
    assert sample_category.description == "Устройства связи"
    # Проверяем работу геттера products
    expected_products_str = (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    )
    assert sample_category.products == expected_products_str


def test_add_product_to_category(sample_category):
    initial_count = Category.product_count
    new_product = Product("Xiaomi", "Redmi", 30000.0, 10)
    sample_category.add_product(new_product)

    assert Category.product_count == initial_count + 1
    assert "Xiaomi" in sample_category.products


def test_new_product_class_method():
    product_data = {
        "name": "Sony",
        "description": "Camera",
        "price": 50000.0,
        "quantity": 3,
    }
    product = Product.new_product(product_data)
    assert isinstance(product, Product)
    assert product.name == "Sony"
    assert product.price == 50000.0
    assert product.quantity == 3
