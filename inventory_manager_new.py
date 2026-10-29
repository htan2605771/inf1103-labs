import json
import os
 
from product import Product
from inventory import Inventory
 
INVENTORY_FILE = "inventory.json"

def create_default_inventory():
    inventory = Inventory()
    inventory.add_product(Product("P001", "Laptop", 1200.00, 15))
    inventory.add_product(Product("P002", "Mouse", 25.50, 40))
    inventory.add_product(Product("P003", "Keyboard", 45.00, 25))
    return inventory

 
def load_inventory():
    """
    Loads inventory.json into an Inventory of Product objects if the file exists.
    Otherwise starts with the default products.
    """
    if os.path.exists(INVENTORY_FILE):
        print("inventory.json found.")
        try:
            with open(INVENTORY_FILE, "r") as f:
                data = json.load(f)
 
            inventory = Inventory()
            for item in data:
                inventory.add_product(
                    Product(item["id"], item["name"], item["price"], item["stock"])
                )
            print("Inventory loaded successfully.")
            return inventory
 
        except (json.JSONDecodeError, KeyError):
            print("inventory.json could not be read. Starting with default inventory.")
            return create_default_inventory()
 
    print("inventory.json not found. Starting with default inventory.")
    return create_default_inventory()
 
 
def save_inventory(inventory, announce=True):
    """Saves every Product in the inventory to inventory.json."""
    if announce:
        print("Saving inventory...")
 
    data = [product.to_dict() for product in inventory.get_products()]
    with open(INVENTORY_FILE, "w") as f:
        json.dump(data, f, indent=4)
 
    if announce:
        print("Inventory saved successfully to inventory.json.")
 
 
def print_menu():
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")
 
def add_product_menu(inventory):
    print("Add New Product")
    product_id = input("Product ID: ")
    name = input("Product Name: ")
 
    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
    except ValueError:
        print("Error: Invalid price or stock quantity. Product not added.")
        return
 
    product = Product(product_id, name, price, stock)
    if inventory.add_product(product):
        print("Product added successfully!")
    else:
        print("Error: Product ID already exists.")
 
 
def update_stock_menu(inventory):
    print("Update Stock")
    product_id = input("Enter Product ID: ")
    product = inventory.search_product(product_id)
 
    if product is None:
        print("Product not found.")
        return
 
    print("Product Found:")
    print(f"Name: {product.get_name()}")
    print(f"Current Stock: {product.get_stock()}")
 
    try:
        new_stock = int(input("New Stock Quantity: "))
    except ValueError:
        print("Error: Invalid stock quantity.")
        return
 
    if product.update_stock(new_stock):
        print("Stock updated successfully!")
 
def search_product_menu(inventory):
    print("Search Product")
    product_id = input("Enter Product ID: ")
    product = inventory.search_product(product_id)
 
    if product is None:
        print("Product not found.")
        return
 
    print("Product Found")
    print("-" * 50)
    product.display_details()
    print("-" * 50)
 