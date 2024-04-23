from src.product import Product


class Category:

    category_count = 0
    products_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        for product in products:
            if not product.quantity:
                raise ValueError('Продукт с нулевым количеством не может быть добавлен')
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.products_count += len(set(products))

    def add_product(self, new_product):
        if isinstance(new_product, Product):
            if not new_product.quantity:
                raise ValueError('Продукт с нулевым количеством не может быть добавлен')
            self.__products.append(new_product)
        else:
            raise TypeError("Могут быть добавлены только экземпляры класса Продукт или экземпляры дочерних классов")

    def avg_price(self):
        try:
            summ = 0
            for prod in self.__products:
                summ += prod.price
            return summ/len(self.__products)
        except ZeroDivisionError:
            return 0

    @property
    def products(self):
        list_products = ''
        for product in self.__products:
            list_products += str(product)
        return list_products

    def __len__(self):
        prod_gen_quant = 0
        for product in self.__products:
            prod_gen_quant += len(product)
        return prod_gen_quant

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self)}"
