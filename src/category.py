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
        self.__products.append(new_product)

    @property
    def products(self):
        list_products = ''
        for product in self.__products:
            product_for_append = f"{product.name}, {product.price} руб. Остаток: {product.quantity}\n"
            list_products += product_for_append
        return list_products
