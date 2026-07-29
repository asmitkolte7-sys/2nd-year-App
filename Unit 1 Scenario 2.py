# Product Inventory System

class Product:
    def __init__(self, product_id, product_name, price):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price

    # Categorize product based on price
    def category(self):
        if self.price >= 1000:
            return "Expensive"
        else:
            return "Affordable"

    # Display product details
    def display(self):
        print(f"Product ID   : {self.product_id}")
        print(f"Product Name : {self.product_name}")
        print(f"Price        : ${self.price:.2f}")
        print(f"Category     : {self.category()}")
        print("-" * 30)


class Inventory:
    def __init__(self):
        self.products = []

    # Add product to inventory
    def add_product(self, product):
        self.products.append(product)

    # Display all products
    def display_products(self):
        print("\n------ Product Inventory ------")
        for product in self.products:
            product.display()


# Main Program
inventory = Inventory()

n = int(input("Enter number of products: "))

for i in range(n):
    print(f"\nEnter details of Product {i + 1}")
    pid = int(input("Product ID: "))
    name = input("Product Name: ")
    price = float(input("Price: "))

    product = Product(pid, name, price)
    inventory.add_product(product)

inventory.display_products()
