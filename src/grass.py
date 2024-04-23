from src.product import Product


class Grass(Product):

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country_prod, germin_period, color):
        self.country_prod = country_prod
        self.germin_period = germin_period
        self.color = color
        super().__init__(name, description, price, quantity)
        if type(self) is Product:
            self.print_ex()
