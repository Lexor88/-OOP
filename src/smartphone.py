class Smartphone(Product):

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 perfomance, model, memory_storage, color):
        super().__init__(name, description, price, quantity)
        self.perfomance = perfomance
        self.model = model
        self.memory_storage = memory_storage
        self.color = color