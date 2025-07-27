inventory = {
    "apples": {"price": 1.50, "quantity": 100},
    "bananas": {"price": 0.75, "quantity": 150},
    "oranges": {"price": 2.00, "quantity": 80}
}

print("--- Initial Inventory ---")
for product, details in inventory.items():
    print(f"{product.capitalize()}: Price = ${details['price']:.2f}, Quantity = {details['quantity']}")

# Task 1: Add a New Product
print("\n--- Task 1: Add a New Product ---")
product_name = "grapes"
price = 3.50
quantity = 75
inventory[product_name] = {"price": price, "quantity": quantity}
print(f"Added '{product_name.capitalize()}' with price ${price:.2f} and quantity {quantity}.")
print("\n--- Inventory after adding grapes ---")
for product, details in inventory.items():
    print(f"{product.capitalize()}: Price = ${details['price']:.2f}, Quantity = {details['quantity']}")


# Task 2: Update Product Price
print("\n--- Task 2: Update Product Price ---")
product_to_update = "bananas"
new_price = 0.85
if product_to_update in inventory:
    inventory[product_to_update]["price"] = new_price
    print(f"Updated price of '{product_to_update.capitalize()}' to ${new_price:.2f}.")
else:
    print(f"Product '{product_to_update.capitalize()}' not found in inventory.")
print("\n--- Inventory after updating banana price ---")
for product, details in inventory.items():
    print(f"{product.capitalize()}: Price = ${details['price']:.2f}, Quantity = {details['quantity']}")


# Task 3: Sell 25 Apples
print("\n--- Task 3: Sell 25 Apples ---")
product_to_sell = "apples"
quantity_sold = 25
if product_to_sell in inventory:
    if inventory[product_to_sell]["quantity"] >= quantity_sold:
        inventory[product_to_sell]["quantity"] -= quantity_sold
        print(f"Sold {quantity_sold} '{product_to_sell.capitalize()}'. Remaining quantity: {inventory[product_to_sell]['quantity']}.")
    else:
        print(f"Not enough '{product_to_sell.capitalize()}' in stock to sell {quantity_sold}.")
else:
    print(f"Product '{product_to_sell.capitalize()}' not found in inventory.")
print("\n--- Inventory after selling apples ---")
for product, details in inventory.items():
    print(f"{product.capitalize()}: Price = ${details['price']:.2f}, Quantity = {details['quantity']}")


# Task 4: Calculate Total Inventory Value
print("\n--- Task 4: Calculate Total Inventory Value ---")
total_inventory_value = 0
for product, details in inventory.items():
    total_inventory_value += details["price"] * details["quantity"]
print(f"Total inventory value: ${total_inventory_value:.2f}")


# Task 5: Find Low Stock Products
print("\n--- Task 5: Find Low Stock Products ---")
low_stock_threshold = 100
low_stock_products = {}
for product, details in inventory.items():
    if details["quantity"] < low_stock_threshold:
        low_stock_products[product] = details["quantity"]

if low_stock_products:
    print(f"Products with quantity below {low_stock_threshold}:")
    for product, quantity in low_stock_products.items():
        print(f"- {product.capitalize()}: {quantity}")
else:
    print("No products found with quantity below the threshold.")