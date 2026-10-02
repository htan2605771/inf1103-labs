import json
import os
 
INVENTORY_FILE = "inventory.json"
 
DEFAULT_INVENTORY = [
    {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
    {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
    {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25},
]


def load_inventory():
    """
    Loads inventory from inventory.json if it exists.
    Otherwise starts with a default list of products.
    Returns a list of dictionaries.
    """
    if os.path.exists(INVENTORY_FILE):
        print("inventory.json found.")
        with open(INVENTORY_FILE, "r") as f:
            data = json.load(f)
        print("Inventory loaded successfully.")
        return data
    else:
        print("inventory.json not found. Starting with default inventory.")
        return [dict(item) for item in DEFAULT_INVENTORY]

def save_inventory(inventory):
    """
    Saves the current inventory list to inventory.json.
    """
    print("Saving inventory...")
    with open(INVENTORY_FILE, "w") as f:
        json.dump(inventory, f, indent=4)
    print("Inventory saved successfully to inventory.json.")

def display_all(inventory):
    """
    Prints all products in the inventory.
    """
    print("Current Inventory")
    print("-" * 50)
    if not inventory:
        print("No products in inventory.")
    else:
        for item in inventory:
            print(f"ID: {item['id']} | Name: {item['name']} | "
                  f"Price: ${item['price']:.2f} | Stock: {item['stock']}")
    print("-" * 50)

def add_product(inventory):
    """
    Prompts for new product details and adds it to the inventory list.
    """
    print("Add New Product")
    product_id = input("Product ID: ")
    name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))
 
    inventory.append({
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock
    })
 
    print("Product added successfully!")
 
 
def update_stock(inventory):
    """
    Prompts for a product ID, and if found, updates its stock quantity.
    """
    print("Update Stock")
    product_id = input("Enter Product ID: ")
 
    for item in inventory:
        if item["id"] == product_id:
            print("Product Found:")
            print(f"Name: {item['name']}")
            print(f"Current Stock: {item['stock']}")
            new_stock = int(input("New Stock Quantity: "))
            item["stock"] = new_stock
            print("Stock updated successfully!")
            return
 
    print("Product not found.")

 
def search_product(inventory):
    """
    Prompts for a product ID and prints its details if found.
    """
    print("Search Product")
    product_id = input("Enter Product ID: ")
 
    for item in inventory:
        if item["id"] == product_id:
            print("Product Found")
            print("-" * 50)
            print(f"ID: {item['id']}")
            print(f"Name: {item['name']}")
            print(f"Price: ${item['price']:.2f}")
            print(f"Stock: {item['stock']}")
            print("-" * 50)
            return
 
    print("Product not found.")


def print_menu():
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")
 