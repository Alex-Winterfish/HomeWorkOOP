from src.product import MixinInfo


def test_smartphone_mixin(capsys, test_smartphone_iphone):
    """Функция проверяет вывод инфоормации об экземпляре класса Smartphone при его создании"""
    captured = capsys.readouterr()
    assert captured.out == "Smartphone, Iphone 15, 512GB, Gray space, 210000.0,8\n"


def test_lawngrass_mixin(capsys, test_product_grass):
    """Функция проверяет вывод информации об экземпляре класса LawnGrass при его создании"""
    captured = capsys.readouterr()
    assert (
        captured.out
        == "LawnGrass, Газонная трава, Элитная трава для газона, 500.0,20\n"
    )


def test_mixin(capsys):
    """Функция проверяет расширение функционала тестового класса, за счет MixinInfo"""

    class DummyClass:

        def __init__(self, name, description, price, quantity):
            self.name = name
            self.description = description
            self.price = price
            self.quantity = quantity

    dummy = DummyClass("Joe", "hollow", 0, 1)
    captured = capsys.readouterr()
    assert dummy.name == "Joe"
    assert captured.out == ""

    class DummyClass(MixinInfo):

        def __init__(self, name, description, price, quantity):
            super().__init__(name, description, price, quantity)

        def price(self):
            super().price()

        def __str__(self):
            super().__str__()

    dummy = DummyClass("Joe", "hollow", 0, 1)
    captured = capsys.readouterr()
    assert dummy.name == "Joe"
    assert captured.out == "DummyClass, Joe, hollow, 0,1\n"
