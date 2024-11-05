import pytest

from src.product import Product, Category, LawnGrass, Smartphone


@pytest.fixture
def test_product_samsung():
    '''Фикстура для инициализации продукта "смартфон"'''
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
@pytest.fixture
def test_product_grass():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

@pytest.fixture
def test_smartphone_xiaomi():
    return Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")

@pytest.fixture
def test_smartphone_iphone():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")

@pytest.fixture
def test_product_nokia():
    return Product(
        "Nokia 3310", "Монохромный дисплей, Серый цвет, без камеры", 1000.0, 9
    )


@pytest.fixture
def test_category_smartphones():
    '''Фикстура для инициализации категории "смартфоны"'''

    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации",
        [product1, product2, product3],
    )


@pytest.fixture
def test_product_tv_1():
    '''Фикстура для инициализации продукта "телевизор"'''
    return Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)


@pytest.fixture
def new_price_1():
    return 500


@pytest.fixture
def new_price_2():
    return 150000


@pytest.fixture
def test_category_tv():
    "Фикстура для проверки числа продуктов в категории"
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )


@pytest.fixture
def test_product_tv_2():
    '''Фикстура для инициализации продукта "телевизор"'''
    product = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    product.price = 500
    return product


@pytest.fixture
def new_product():
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }


