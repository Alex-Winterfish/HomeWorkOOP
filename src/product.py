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

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price > 0:
            self.__price = price
        else:
            self.__price = self.__price

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

    def __add__(self, other):
        return self.quantity * self.__price + other.quantity * other.price


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
        a = ""
        for product in self.__products:
            a += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
        return a

    def __str__(self):
        total = 0  # переменная для подсчета общего числа единиц товара в категории
        for product in self.__products:
            total += product.quantity
        return f"{self.name}. Остаток: {total} шт."

    def add_product(self, product):
        if not isinstance(product,Product):
            raise TypeError
        else:
            self.__products.append(product)
            Category.product_count += 1


class Smartphone(Product):

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(self) == type(other):
            return  super().__add__(other)

        else:
            raise TypeError



class LawnGrass(Product):

    def __init__(self,name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(self) == type(other):
            return super().__add__(other)
        else:
            raise TypeError
