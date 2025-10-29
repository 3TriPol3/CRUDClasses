class MyTasks_3:
    def __init__(self):
        self.__list_products = [
            {"id": 1, "product": "Хлеб", "quantity": 1, "bought": False},
            {"id": 2, "product": "Молоко", "quantity": 2, "bought": True}
        ]
        self.id = 3  # Следующий ID для нового продукта

    @property
    def products(self):
        return self.__list_products

    @products.setter
    def products(self, dict):
        dict['id'] = self.id
        self.__list_products.append(dict)
        self.id += 1


if __name__ == "__main__":
    product = MyTasks_3()
    print(product.products)
    product.products = {"product": "Яйца", "quantity": 10, "bought": False}
    print(product.products)