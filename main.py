class Item:
    # constructor assign attributes to use in the __init__ method
    def __init__(self, name, price, quantity=0):
        # print(f"An instance created: {name}")
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculateTotalPrice(self):
        return self.price * self.quantity


# attributes of Item class
item1 = Item("Phone", 100, 5)

item2 = Item("Laptop", 1000, 3)

print(item1.name)
print(item2.name)
print(item1.price)
print(item2.price)
print(item1.quantity)
print(item2.quantity)
