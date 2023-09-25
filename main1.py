from Item import Item
from Phone import Phone

phone = Phone('Phone', 1000, 10)  # create an instance from Item class
print(phone.calculate_total_price())  # when calling a method, python by default pass the instance to the method

item1 = Item('Laptop', 1000, 3)
print(item1.calculate_total_price())  # when calling a method, python by default pass the instance to the method

item2 = Item('Airpods', 900)

print(f'Pay rent: {Item.pay_rate}')
print(f'Pay rent: {phone.pay_rate}')  # since instance attribute not exist -> python looking for class attribute
print(f'Pay rent: {item1.pay_rate}')

print(Item.__dict__)  # All the attributes for Class level
print(phone.__dict__)  # All the attributes for Instance level
# dict -> takes all attributes and convert into dictionary

phone.apply_discount()  # polymorphic method -> can be accessed from any child class of Item
print(f'Item1 after discount: {phone.price}')

item1.pay_rate = 0.7
item1.apply_discount()
print(f'Item2 after discount: {item1.price}')

print(phone.name)
print(item1.name)
print(phone.quantity)
print(item1.quantity)
print(item2.quantity)

name = str('Bob')  # create an instance from str class

print(type(phone))
print(type(name))
