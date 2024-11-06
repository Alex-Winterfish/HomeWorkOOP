import pytest

from src.product import Category


def test_smartphone_init_1(capsys, test_smartphone_xiaomi):
    """Функция проверяет инициализацию экземпляра класса с новыми атрибутами
    и вывод информации при создании экземпляра класса"""
    assert test_smartphone_xiaomi.model == "Note 11"
    assert test_smartphone_xiaomi.memory == 1024
    assert test_smartphone_xiaomi.efficiency == 90.3
    assert test_smartphone_xiaomi.color == "Синий"
    captured_repr = (
        capsys.readouterr()
    )  # отлавливаем вывод информации при создании класса
    assert (
        captured_repr.out
        == "Smartphone, Xiaomi Redmi Note 11, 1024GB, Синий, 31000.0,14\n"
    )
    print(test_smartphone_xiaomi)
    captured = capsys.readouterr()
    assert captured.out == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"


def test_smartphone_init_2(capsys, test_smartphone_iphone):
    """Функция проверяет инициализацию экземпляра класса с новыми атрибутами
    и вывод информации при создании экземпляра класса"""
    assert test_smartphone_iphone.model == "15"
    assert test_smartphone_iphone.memory == 512
    assert test_smartphone_iphone.efficiency == 98.2
    assert test_smartphone_iphone.color == "Gray space"
    captured_repr = capsys.readouterr()
    assert captured_repr.out == "Smartphone, Iphone 15, 512GB, Gray space, 210000.0,8\n"
    print(test_smartphone_iphone)
    captured = capsys.readouterr()
    assert captured.out == "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"


def test_lawn_grass_init(capsys, test_product_grass):
    assert test_product_grass.color == "Зеленый"
    assert test_product_grass.germination_period == "7 дней"
    assert test_product_grass.color == "Зеленый"
    assert test_product_grass.country == "Россия"
    captured_repr = capsys.readouterr()
    assert (
        captured_repr.out
        == "LawnGrass, Газонная трава, Элитная трава для газона, 500.0,20\n"
    )
    print(test_product_grass)
    captured = capsys.readouterr()
    assert captured.out == "Газонная трава, 500.0 руб. Остаток: 20 шт.\n"


def test_smartphone_add(test_smartphone_iphone, test_smartphone_xiaomi):
    """Функция проверяет сложение продуктов одной категории"""
    sum_smartphone = test_smartphone_xiaomi + test_smartphone_iphone
    assert sum_smartphone == 2114000.0


def test_add_dif_product(test_smartphone_iphone, test_product_grass):
    """Функция проверяет ошибку TypeError при сложении разных продуктов"""
    with pytest.raises(TypeError):
        sum_product = test_product_grass + test_smartphone_iphone
        print(sum_product)


def test_add_wrong_product(test_smartphone_iphone, test_smartphone_xiaomi):
    """Функция проверяет невозможность добавления в категорию других сущностей, кроме продуктов"""
    smart_phone_cat = Category(
        "Смартфоны",
        "Высокотехнологичные смартфоны",
        [test_smartphone_iphone, test_smartphone_xiaomi],
    )
    with pytest.raises(TypeError):
        smart_phone_cat.add_product(True)
