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
 
 