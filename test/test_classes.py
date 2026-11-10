import pytest

from product import BaseProduct, LawnGrass, Product, Smartphone


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


def test_product_price_setter():
    """Проверяем работу сеттера цены (включая защиту от некорректных значений)."""
    product = Product("Товар", "Описание", 200.0, 10)

    product.price = 250.0
    assert product.price == 250.0

    product.price = -50
    assert product.price == 250.0


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
