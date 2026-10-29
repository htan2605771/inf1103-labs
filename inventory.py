class Inventory:
    """Manages a collection of Product objects."""
 
    def __init__(self):
        self.__products = []
 
    def add_product(self, product):
        """
        Adds a Product to the inventory.
        Returns False (and does not add it) if the product ID already exists.
        """
        if self.search_product(product.get_product_id()) is not None:
            return False
        self.__products.append(product)
        return True
 
    def search_product(self, product_id):
        """Returns the Product with the given ID, or None if not found."""
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None
 