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
 