def test_category_init_1(test_category_smartphones):
    "Функция проверяет инициализацию экземпляра класса Category"
    assert test_category_smartphones.name == "Смартфоны"
    assert (
        test_category_smartphones.description
        == "Смартфоны, как средство не только коммуникации"
    )
    assert test_category_smartphones.products == test_category_smartphones.products
    assert test_category_smartphones.category_count == 1
    assert test_category_smartphones.product_count == 3


def test_category_init_2(test_category_tv):
    "Функция проверяет инициализацию экземпляра класса Category"
    assert test_category_tv.name == "Телевизоры"
    assert (
        test_category_tv.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert test_category_tv.products == test_category_tv.products
    assert test_category_tv.category_count == 2
    assert test_category_tv.product_count == 4


def test_category_append(test_category_smartphones, test_category_tv):
    "Функция проверяет подсчет числа категороий и единиц продукта в классе Category"
    assert test_category_tv.category_count == 4
    assert test_category_tv.product_count == 8


def test_category_product_append(test_category_smartphones, test_product_nokia):
    "Функция проверяет вывод добавлние продукта"
    assert test_category_smartphones.product_count == 11
    test_category_smartphones.add_product(test_product_nokia)
    assert test_category_smartphones.product_count == 12


def test_category_product_output(capsys, test_category_smartphones):
    "Функция проверяет вывод информации о продуктах и их количестве"
    assert test_category_smartphones.product_count == 15
    assert test_category_smartphones.products == ('Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                                'Iphone 15, 210000.0 руб. Остаток: 8 шт.\n'
                                                'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n')

