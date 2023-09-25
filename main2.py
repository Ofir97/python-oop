from Item import Item
from Keyboard import Keyboard
from Phone import Phone

Item.instantiate_from_csv()
# print(Item.all)

# print(Item.is_integer(7))

phone = Phone("iPhone 11", 1400, 5, 3)
keyboard = Keyboard('jscKeyboard', 1000, 5)

phone.apply_discount()  # polymorphic method -> can be accessed from any child class of Item
keyboard.apply_discount()  # polymorphic method -> can be accessed from any child class of Item

print(phone)
print(phone.calculate_total_price())
print(f'Keyboard price: {keyboard.price}')
print(f'Phone price: {phone.price}')
print(Item.all)
