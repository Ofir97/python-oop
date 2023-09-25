from Item import Item


# inheritance: Phone Class inherits from Item Class

class Phone(Item):

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )
        self.broken_phones = broken_phones
        self.quantity -= broken_phones
