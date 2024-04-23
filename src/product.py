class Product:

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def from_dict(cls, dict_with_prod):
        name = dict_with_prod.get['name']
        description = dict_with_prod.get['description']
        price = dict_with_prod.get['price']
        quantity = dict_with_prod.get['quantity']
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if not new_price <= 0:
            self.__price = new_price
        else:
            print("Заданная цена не соответствует условиям")

    def __len__(self):
        return self.quantity

    def sum_price(self):
        return self.price * self.quantity

    def __add__(self, other):
        if isinstance(other, Product):
            return self.sum_price() + other.sum_price()
        else:
            print("Допустимо сложение только с ЭК Продукт или дочерними по отношению к нему классами")

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity}"

