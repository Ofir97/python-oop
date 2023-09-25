from Item import Item

item = Item("Pen", 3.5, 5)
# print(item.__name) --> error: 'Item' object has no attribute '__name'

item.name = "Pencil"
print(item.name)

item.apply_increment(0.2)

print(item.price)

item.send_email()