class Product:
    """Represents and manages a single product."""

    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def update_stock(self, quantity):
        """
        Sets the stock to the given quantity.
        Returns True if updated, False if the quantity is invalid.
        """
        if quantity < 0:
            print("Error: Stock quantity cannot be negative.")
            return False
        self.__stock = quantity
        return True
    
    def display_information(self):
        """Prints the product on a single line."""
        print(f"ID: {self.__product_id} | Name: {self.__name} | "
              f"Price: ${self.__price:.2f} | Stock: {self.__stock}")
 
    def display_details(self):
        """Prints the product over multiple lines."""
        print(f"ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock}")
 
    def to_dict(self):
        """Returns the product as a dictionary (used when saving to JSON)."""
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
        }
