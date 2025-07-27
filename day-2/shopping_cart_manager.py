def display_cart(cart):
    """Displays the current contents of the shopping cart with indices."""
    if not cart:
        print("Your shopping cart is empty.")
    else:
        print("\n--- Current Shopping Cart Contents ---")
        for index, item in enumerate(cart):
            print(f"{index}: {item.capitalize()}")
    print("-" * 35)

def add_item(cart, item):
    """Adds an item to the shopping cart."""
    cart.append(item.lower()) # Store items in lowercase for consistent handling
    print(f"'{item.capitalize()}' has been added to your cart.")

def remove_specific_item(cart, item):
    """Removes a user-specified item if it exists in the cart."""
    item_lower = item.lower()
    if item_lower in cart:
        cart.remove(item_lower)
        print(f"'{item.capitalize()}' has been removed from your cart.")
    else:
        print(f"'{item.capitalize()}' was not found in your cart.")

def remove_last_added_item(cart):
    """Removes the most recently added item from the cart."""
    if cart:
        removed_item = cart.pop()
        print(f"'{removed_item.capitalize()}' (last added item) has been removed from your cart.")
    else:
        print("Your cart is empty, nothing to remove.")

def display_sorted_items(cart):
    """Displays all items in the cart in alphabetical order."""
    if not cart:
        print("Your shopping cart is empty.")
    else:
        print("\n--- Shopping Cart Items (Alphabetical Order) ---")
        sorted_cart = sorted(cart)
        for item in sorted_cart:
            print(f"- {item.capitalize()}")
    print("-" * 45)


# --- Sample Operations to Implement ---

# Start with an empty cart
shopping_cart = []
print("Welcome to your Shopping Cart Manager!")
display_cart(shopping_cart)

# Add items: "apples", "bread", "milk", "eggs"
print("\n--- Performing Sample Operations ---")
add_item(shopping_cart, "apples")
add_item(shopping_cart, "bread")
add_item(shopping_cart, "milk")
add_item(shopping_cart, "eggs")
display_cart(shopping_cart)

# Remove "bread"
remove_specific_item(shopping_cart, "bread")
display_cart(shopping_cart)

# Remove the last added item
remove_last_added_item(shopping_cart)
display_cart(shopping_cart)

# Sort and display items alphabetically
display_sorted_items(shopping_cart)

# Display final cart with index numbers
print("\n--- Final Cart Contents with Index Numbers ---")
display_cart(shopping_cart)