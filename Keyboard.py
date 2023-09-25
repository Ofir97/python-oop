from Item import Item


# inheritance: Phone Class inherits from Item Class

class Keyboard(Item):
    pay_rate = 0.7  # Overrides parent attribute pay_rate

    def __init__(self, name: str, price: float, quantity=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )
