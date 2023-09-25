import csv


class Item:
    pay_rate = 0.8  # CLASS ATTRIBUTE (class level): The pay rent after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        self.__validate_name(name)
        assert price >= 0, f'Price {price} is not greater than or equal to zero.'
        assert quantity >= 0, f'Quantity {quantity} is not greater than or equal to zero.'

        # Assign to self object
        self.__name = name  # __ PRIVATE instance attribute
        self.__price = price  # __ PRIVATE instance attribute
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def __validate_name(self, name):
        if not isinstance(name, str):
            raise Exception(f'Invalid name format.')
        if len(name) >= 15:
            raise Exception(f'The name given {name} must be less than 15 characters.')

    @property
    def price(self):
        return self.__price

    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__validate_name(name)
        self.__name = name

    def calculate_total_price(self):
        return self.__price * self.quantity  # if instance attr not exist -> pull value from class level

    def apply_discount(self):
        self.__price *= self.pay_rate

    def apply_increment(self, increment_value):
        self.__price += self.__price * increment_value

    @classmethod  # class relationship for instantiating objects
    def instantiate_from_csv(cls):  # must send class reference as argument
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

            for item in items:
                Item(
                    name=item.get('name'),
                    price=float(item.get('price')),
                    quantity=int(item.get('quantity'))
                )

    @staticmethod  # class relationship and not unique per instance
    def is_integer(num):  # no mandatory args should be sent
        if isinstance(num, float):
            return num.is_integer()  # if float is integer return True
        return isinstance(num, int)

    def __connect(self, smpt_server):  # private method
        pass

    def __prepare_body(self):  # private method
        return f'''
        Hello Someone.
        We have {self.quantity} of {self.name} in store.
        Regards.  
        '''

    def __send(self):  # private method
        pass

    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"
