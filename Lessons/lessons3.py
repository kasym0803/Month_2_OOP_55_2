


class Product:
    def __init__(self, name, price, stock):
        self.__name = name
        self.__price = price
        self.__stock = stock


    def get_info(self):
        return f"Товар:{self.__name}, Цены: {self.__price}, Количества: {self.__stock}"

    def buy(self, quantity):
        if quantity <= self.__stock:
            self.__stock -= quantity
            return True, f"Количество товаров осталось {self.__stock}"
        else:
            return False

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

product = Product("My Product", 50000, 100)
print(product.get_info())
print(product.buy(5))


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product, quantity):
        if product.buy(quantity):
            self.products.append(product)
            return f"Добавлен продукт в казину {product.get_info()} >> {quantity} шт"
        else:
            return f"Продукт не добавлен в корзину "

    def checkout(self):
        if not self.products:
            return "Корзина пуста"

        total = 0
        result = ""
        for product, quantity in self.products:
            item_total = product.get_price() * quantity
            result += f"Товар: {product.get_name()}, {quantity} шт. по {product.get_price()} = {item_total}\n"
            total += item_total
        result += f"Итого: {total}"
        return result

product_1 = Product("phone", 67999, 33)
product_2 = Product("Airpods", 42999, 22)

cart = Cart()

print(product_1.get_info())
print(product_2.get_info())

print(cart.add_product(product_1, 10))
print(cart.add_product(product_2, 10))
print(cart.checkout())
