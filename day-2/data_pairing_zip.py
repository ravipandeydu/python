# Initial lists from the image
products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
prices = [999.99, 25.50, 75.00, 299.99]
quantities = [5, 20, 15, 8]

print("--- Initial Data ---")
print(f"Products: {products}")
print(f"Prices: {prices}")
print(f"Quantities: {quantities}")

# Task 1: Create Product-Price Pairs
print("\n--- Task 1: Product-Price Pairs ---")
product_price_pairs = list(zip(products, prices))
print("Product-Price Pairs:")
for product, price in product_price_pairs:
    print(f"- {product}: ${price:.2f}")

# Task 2: Calculate Total Value for Each Product
print("\n--- Task 2: Total Value for Each Product ---")
print("Total Inventory Value per Product:")
for product, price, quantity in zip(products, prices, quantities):
    total_value = price * quantity
    print(f"- {product}: ${price:.2f} x {quantity} = ${total_value:.2f}")

# Task 3: Build a Product Catalog Dictionary
print("\n--- Task 3: Build a Product Catalog Dictionary ---")
product_catalog = {}
for product, price, quantity in zip(products, prices, quantities):
    product_catalog[product] = {"price": price, "quantity": quantity}

print("Product Catalog Dictionary:")
import json
print(json.dumps(product_catalog, indent=4))

# Task 4: Find Low Stock Products
print("\n--- Task 4: Find Low Stock Products (quantity < 10) ---")
low_stock_threshold = 10
low_stock_products = []

for product, quantity in zip(products, quantities):
    if quantity < low_stock_threshold:
        low_stock_products.append(product)

if low_stock_products:
    print(f"Products with quantity less than {low_stock_threshold}:")
    for product in low_stock_products:
        print(f"- {product}")
else:
    print("No products found with quantity below the threshold.")
