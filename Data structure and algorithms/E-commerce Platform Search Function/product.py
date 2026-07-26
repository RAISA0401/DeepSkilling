class Product:
    def __init__(self, product_id, product_name, category):
        self.product_id = product_id
        self.product_name = product_name
        self.category = category

    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.product_name}, Category: {self.category}"