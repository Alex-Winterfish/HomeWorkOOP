import pytest

from src.product import Product, Category


@pytest.fixture
def test_product_samsung():
    '''Фикстура для инициализации продукта "смартфон"'''
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)



@pytest.fixture
def test_category_smartphones():
    '''Фикстура для инициализации категории "смартфоны"'''
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    return Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1,product2,product3])

@pytest.fixture
def test_product_tv():
    '''Фикстура для инициализации продукта "телевизор"'''
    return Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)


@pytest.fixture
def test_category_tv():
    'Фикстура для проверки числа продуктов в категории'
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    return Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])