import pytest
from src.product import Product, Category


def test_er_add_zero_product(test_prod_zero_quan):
    """Функция проверяет ошибку при добавлении продукта с нулевым количеством"""
    with pytest.raises(ValueError):
        Product.new_product(test_prod_zero_quan)


def test_middle_price(test_category_smartphones, test_smartphone_iphone):
    """Функция проверяет расчет средней цены товаров в категории"""
    assert test_category_smartphones.middle_price() == 140333.33
    test_category_smartphones.add_product(test_smartphone_iphone)
    assert test_category_smartphones.middle_price() == 157750.0


def test_middle_zero_prod():
    """Проверяет расчет средней цены, если в категории нет товаров"""
    category = Category("не товар", "без описания", [])
    assert category.middle_price() == 0
