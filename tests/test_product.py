

def test_product_init_1(test_product_samsung):
    "Функция проверяет инициализацию экземпляра класса Product"
    assert test_product_samsung.name == 'Samsung Galaxy S23 Ultra'
    assert test_product_samsung.description == '256GB, Серый цвет, 200MP камера'
    assert test_product_samsung.price ==  180000.0
    assert test_product_samsung.quantity == 5

def test_product_inti_2(test_product_tv):
    "Функция проверяет инициализацию экземпляра класса Product"
    assert test_product_tv.name == '55" QLED 4K'
    assert test_product_tv.description == 'Фоновая подсветка'
    assert test_product_tv.price == 123000.0
    assert test_product_tv.quantity == 7





