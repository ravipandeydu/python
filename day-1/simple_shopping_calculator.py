item1price = int(input("Enter price of item 1: "))
item1quantity = int(input("Enter quantity of item 1: "))
item2price = int(input("Enter price of item 2: "))
item2quantity = int(input("Enter quantity of item 2: "))
item3price = int(input("Enter price of item 3: "))
item3quantity = int(input("Enter quantity of item 3: "))

print("Output")
print(f"Item 1: {item1quantity} x {item1price} = {item1price * item1quantity}")
print(f"Item 2: {item2quantity} x {item2price} = {item2price * item2quantity}")
print(f"Item 3: {item3quantity} x {item3price} = {item3price * item3quantity}")
print(f"Subtotal: {item1price * item1quantity + item2price * item2quantity + item3price * item3quantity}")
print(f"Tax (8.5%): {(item1price * item1quantity + item2price * item2quantity + item3price * item3quantity) * 0.085}")
print(f"Total: {(item1price * item1quantity + item2price * item2quantity + item3price * item3quantity) * 1.085}")