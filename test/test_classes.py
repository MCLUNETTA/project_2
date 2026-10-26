import pytest

from scr.product import (  # Замени src.product на путь к твоему модулю с классами
    Category, Product)


@pytest.fixture
def sample_products():
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    return product1, product2


@pytest.fixture
def sample_category(sample_products):
    product1, product2 = sample_products
    return Category("Смартфоны", "Устройства связи", [product1, product2])


def test_product_initialization(sample_products):
    product1, _ = sample_products
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_category_initialization(sample_category, sample_products):
    product1, product2 = sample_products
    assert sample_category.name == "Смартфоны"
    assert sample_category.description == "Устройства связи"
    assert sample_category.products == [product1, product2]


def test_category_and_product_counters(sample_products):
    # Сбрасываем счетчики перед тестом, если они накопились от других тестов
    Category.category_count = 0
    Category.product_count = 0

    product1, product2 = sample_products
    category1 = Category("Смартфоны", "Описание 1", [product1, product2])

    assert Category.category_count == 1
    assert Category.product_count == 2
    assert category1.name == "Смартфоны"
    assert category1.description == "Описание 1"
    product3 = Product("Телевизор", "4K", 50000.0, 2)
    _ = Category("Телевизоры", "Описание 2", [product3])

    assert Category.category_count == 2
    assert Category.product_count == 3
