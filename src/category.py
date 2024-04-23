from src.product import Product


class Category:

    category_count = 0
    products_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.products_count += len(set(products))

    def add_product(self, new_product):
        if isinstance(new_product, Product):
            self.__products.append(new_product)
        else:
            print("Могут быть добавлены только экземпляры класса Продукт или экземпляры дочерних классов")

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