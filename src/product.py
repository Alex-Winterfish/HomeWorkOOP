class Product:
    """Класс Product принимает описание единицы товар"""

    name: str
    description: str
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @classmethod
    def new_product(
        cls,
        new_product,
    ):
        name = new_product.get("name")
        description = new_product.get("description")
        price = new_product.get("price")
        quantity = new_product.get("quantity")
        return cls(name, description, price, quantity)


class Category:
    """Класс Category принимает описание группы товаров"""

    name: str
    description: str
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    @property
    def products(self):

        for product in self.__products:
            print(f"{product.name}, {product.price} руб. Остаток: {product.quantity}")

    def add_product(self, product):
        self.product_count += 1
        return self.__products.append(product)
