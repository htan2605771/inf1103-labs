INVENTORY_FILE = "inventory.txt"
 
 
def load_inventory():
    """
    Reads the previously saved total and transaction history from inventory.txt.
    Returns:
        (total, history) as (float, list of floats)
    If the file doesn't exist, returns (0, []) and does not error.
    """
    try:
        with open(INVENTORY_FILE, "r") as f:
            lines = f.readlines()
 
            total = float(lines[0].strip()) if len(lines) > 0 and lines[0].strip() else 0
 
            if len(lines) > 1 and lines[1].strip():
                history = [float(x) for x in lines[1].strip().split(",")]
            else:
                history = []
 
            return total, history
 
    except FileNotFoundError:
        return 0, []
    
def save_inventory(total, history):
    """
    Writes the final total and transaction history to inventory.txt.
    Line 1: total
    Line 2: comma-separated history of transaction amounts
    """
    with open(INVENTORY_FILE, "w") as f:
        f.write(f"{total}\n")
        f.write(",".join(str(x) for x in history) + "\n")
 

def get_valid_input():
    """
    Prompts the user for a stock quantity.
    Returns:
        - an integer if the input is valid
        - "quit" if the user wants to stop
        - None if the input was invalid (caller should count this as failed)
    """
    stock = input("Enter stock quantity (or 'quit' to stop): ")
 
    if stock.lower() == "quit":
        return "quit"
 
    if stock.startswith("-"):
        print("Error: Negative stock quantities are not allowed.")
        return None
 
    if not stock.isdigit():
        print("Error: Invalid input. Please enter an integer.")
        return None
 
    return int(stock)


def process_delivery(current_total, new_value):
    """
    Adds new_value to current_total and returns the new total.
    """
    return current_total + new_value


def calculate_tax(amount):
    """
    Calculates 10% tax on a single delivery amount.
    """
    return amount * 0.10
 

def generate_report(total_units, failed_attempts):
    """
    Prints the final summary report.
    """
    print("\n--- Inventory Report ---")
    print("Total Units Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)



def main():
    inventory = 0
    failed_entries = 0
    deliveries_processed = 0
 
    while True:
        result = get_valid_input()
 
        if result == "quit":
            break
 
        if result is None:
            failed_entries += 1
            continue
 
        # Valid delivery received
        tax = calculate_tax(result)
        inventory = process_delivery(inventory, result)
        deliveries_processed += 1
 
        print("Stock accepted.")
        print("Current inventory:", inventory)
        print(f"Tax for this delivery: {tax:.2f}")
 
        if inventory > 500:
            print("ALERT: Overstock! Inventory exceeds 500 units.")
            break
 
    generate_report(inventory, failed_entries)
    print("Total Deliveries Processed:", deliveries_processed)
 
 
if __name__ == "__main__":
    main()