inventory = 0
failed_entries = 0

while True:
    stock = input("Enter stock quantity (or 'quit' to stop): ")

    if stock.lower() == "quit":
        break

    if stock.startswith("-"):
        print("Error: Negative stock quantities are not allowed.")
        failed_entries += 1
        continue

    if not stock.isdigit():
        print("Error: Invalid input. Please enter an integer.")
        failed_entries += 1
        continue

    stock = int(stock)

    inventory += stock

    print("Stock accepted.")
    print("Current inventory:", inventory)

    if inventory > 500:
        print("ALERT: Overstock! Inventory exceeds 500 units.")
        break

print("\n--- Inventory Report ---")
print("Total Units Processed:", inventory)
print("Number of Failed/Rejected Entries:", failed_entries)