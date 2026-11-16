# Документация проекта

## Содержание

1. [Модуль `product`](#модуль-product)
   - [Класс `Product`](#класс-product)
   - [Класс `Category`](#класс-category)
2. [Модуль `test_classes`](#модуль-test_classes)
   - [Фикстуры](#фикстуры)
   - [Тесты класса `Product`](#тесты-класса-product)
   - [Тесты класса `Category`](#тесты-класса-category)

---

## Модуль `product`

Модуль содержит классы `Product` и `Category` для работы с товарами и категориями товаров.

### Класс `Product`

Класс представляет товар и хранит его название, описание, цену и количество на складе. Цена хранится в приватном атрибуте `__price` и доступна через свойство `price`, которое позволяет получать и изменять её с проверкой значения.

#### `__init__`

```python
__init__(
    self,
    name: str,
    description: str,
    price: float,
    quantity: int
) -> None
```

Конструктор создаёт объект товара и инициализирует его атрибуты.

**Параметры:**
- `name` — название товара.
- `description` — описание товара.
- `price` — цена товара.
- `quantity` — количество товара на складе.

**Пример:**

```python
product = Product(
    "Samsung Galaxy S23 Ultra",
    "256GB, Серый",
    180000.0,
    5
)
```

#### `new_product`

```python
@classmethod
new_product(cls, product_data: dict) -> Product
```

Создаёт и возвращает объект класса `Product` на основе словаря с данными о товаре.

**Параметры:**
- `product_data` — словарь, содержащий ключи `name`, `description`, `price` и `quantity`.

**Возвращает:**
- `Product` — новый объект товара.

**Пример:**

```python
product_data = {
    "name": "Sony",
    "description": "Camera",
    "price": 50000.0,
    "quantity": 3
}

product = Product.new_product(product_data)
```

#### `price`

```python
@property
def price(self) -> float
```

Геттер, возвращающий текущую цену товара.

**Возвращает:**
- `float` — текущая цена товара.

**Пример:**

```python
product = Product("Sony", "Camera", 50000.0, 3)
print(product.price)
```

Результат:

```text
50000.0
```

#### `price.setter`

```python
@price.setter
def price(self, new_price: float) -> None
```

Сеттер для изменения цены товара. Если новая цена больше нуля, она сохраняется. Если цена равна нулю или отрицательна, значение не изменяется, а в консоль выводится сообщение об ошибке.

**Параметры:**
- `new_price` — новая цена товара.

**Возвращает:**
- `None`.

**Пример:**

```python
product = Product("Sony", "Camera", 50000.0, 3)

product.price = 55000.0
print(product.price)

product.price = 0
print(product.price)
```

Результат:

```text
55000.0
Цена не должна быть нулевая или отрицательная
55000.0
```

### Класс `Category`

Класс представляет категорию товаров. Он хранит название категории, описание и список товаров. Также класс ведёт общие счётчики количества созданных категорий и количества товаров, добавленных в категории.

**Атрибуты класса:**
- `category_count` — общее количество созданных объектов `Category`.
- `product_count` — общее количество товаров, учтённых при создании категорий и добавлении товаров.

**Приватный атрибут:**
- `__products` — список объектов `Product`, принадлежащих категории.

#### `__init__`

```python
__init__(
    self,
    name: str,
    description: str,
    products: list
) -> None
```

Создаёт категорию, сохраняет её название и описание, а также список товаров. Если список `products` пустой или имеет значение, которое оценивается как ложное, создаётся пустой список.

При создании объекта увеличивается `Category.category_count`. Счётчик `Category.product_count` увеличивается на количество переданных товаров.

**Параметры:**
- `name` — название категории.
- `description` — описание категории.
- `products` — список товаров категории.

**Пример:**

```python
product = Product("Sony", "Camera", 50000.0, 3)

category = Category(
    "Фототехника",
    "Фотоаппараты и аксессуары",
    [product]
)
```

#### `add_product`

```python
def add_product(self, product: Product) -> None
```

Добавляет объект `Product` в список товаров категории и увеличивает общий счётчик `Category.product_count` на единицу.

**Параметры:**
- `product` — объект товара, который нужно добавить в категорию.

**Возвращает:**
- `None`.

**Пример:**

```python
category.add_product(
    Product("Canon", "Фотоаппарат", 70000.0, 2)
)
```

#### `products`

```python
@property
def products(self) -> str
```

Геттер, который возвращает информацию о товарах категории в виде одной строки. Для каждого товара указываются название, цена в рублях и остаток на складе. Каждая запись заканчивается символом переноса строки.

**Возвращает:**
- `str` — отформатированный список товаров.

**Пример:**

```python
product = Product("Sony", "Camera", 50000.0, 3)
category = Category("Фототехника", "Фотоаппараты", [product])

print(category.products)
```

Результат:

```text
Sony, 50000.0 руб. Остаток: 3 шт.
```

---

## Модуль `test_classes`

Модуль содержит автоматические тесты для классов `Product` и `Category`, написанные с использованием библиотеки `pytest`.

Тесты проверяют:
- корректность инициализации объектов;
- работу геттера и сеттера цены;
- формирование строки с товарами категории;
- добавление товаров и обновление счётчика;
- создание товара с помощью метода `new_product`.

### Фикстуры

#### `sample_products`

```python
@pytest.fixture
def sample_products()
```

Создаёт два объекта `Product` с тестовыми данными и возвращает их в виде кортежа.

Используется в тестах для повторного применения подготовленных объектов товаров.

#### `sample_category`

```python
@pytest.fixture
def sample_category(sample_products)
```

Получает товары из фикстуры `sample_products`, создаёт категорию «Смартфоны» и возвращает её.

Используется в тестах, связанных с классом `Category`.

### Тесты класса `Product`

#### `test_product_initialization`

```python
def test_product_initialization(sample_products)
```

Проверяет, что после создания объекта `Product` его атрибуты `name`, `description`, `price` и `quantity` содержат ожидаемые значения.

#### `test_product_price_setter`

```python
def test_product_price_setter()
```

Проверяет работу сеттера цены:
- корректная положительная цена сохраняется;
- нулевая цена не изменяет текущее значение;
- отрицательная цена не изменяет текущее значение.

#### `test_new_product_class_method`

```python
def test_new_product_class_method()
```

Проверяет создание объекта `Product` с помощью метода `new_product`. Тест подтверждает, что метод возвращает объект класса `Product` и корректно переносит данные из словаря.

### Тесты класса `Category`

#### `test_category_initialization`

```python
def test_category_initialization(sample_category, sample_products)
```

Проверяет правильность инициализации категории: название, описание и форматирование списка товаров через свойство `products`.

#### `test_add_product_to_category`

```python
def test_add_product_to_category(sample_category)
```

Проверяет добавление нового товара в категорию. Тест подтверждает, что:
- общий счётчик `Category.product_count` увеличивается на единицу;
- информация о новом товаре появляется в строке, возвращаемой свойством `products`.

### Запуск тестов

Для запуска тестов из корневой директории проекта выполни команду:

```bash
pytest
```

Чтобы запустить только тесты из файла `test_classes.py`:

```bash
pytest test_classes.py
```
