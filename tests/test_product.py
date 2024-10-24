from src.product import Product


def test_product_init_1(test_product_samsung):
    "Функция проверяет инициализацию экземпляра класса Product"
    assert test_product_samsung.name == "Samsung Galaxy S23 Ultra"
    assert test_product_samsung.description == "256GB, Серый цвет, 200MP камера"
    assert test_product_samsung.price == 180000.0
    assert test_product_samsung.quantity == 5


def test_product_inti_2(test_product_tv_1):
    "Функция проверяет инициализацию экземпляра класса Product"
    assert test_product_tv_1.name == '55" QLED 4K'
    assert test_product_tv_1.description == "Фоновая подсветка"
    assert test_product_tv_1.price == 123000.0
    assert test_product_tv_1.quantity == 7


def test_product_change_price(test_product_tv_1, new_price_1):
    "Функция проверяет изменение цены товара"
    assert test_product_tv_1.price == 123000.0
    test_product_tv_1.price = new_price_1
    assert test_product_tv_1.price == 500


def test_new_product(new_product):
    product = Product.new_product(new_product)
    assert product.name == "Samsung Galaxy S23 Ultra"
