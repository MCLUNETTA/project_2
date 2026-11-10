from src.product import Product, Smartphone, LawnGrass

if __name__ == "__main__":
    print("--- Создание продуктов и проверка миксина ---")
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, "high", "15", "512GB", "Gray space")
    product3 = LawnGrass("Газонная трава", "Элитная", 500.0, 20, "Россия", "7 дней", "Зеленый")

    print("\n--- Проверка свойств и сеттера цены ---")
    print(product1.name, product1.price)
    product1.price = 185000.0
    print(f"Новая цена product1: {product1.price}")

    # Попытка установить некорректную цену
    product1.price = -50
    print("Всё работает отлично и без ошибок!")
