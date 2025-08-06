from collections import Counter


class Product:
    """
    Represents a product in the e-commerce system, with inventory management
    and category-level analytics.
    """

    _total_products = 0
    _category_popularity = Counter()

    def __init__(self, product_id, name, price, category, stock_quantity):
        """
        Initializes a new Product.

        Args:
            product_id (str): Unique ID for the product.
            name (str): Name of the product.
            price (float): Price of the product.
            category (str): Category of the product.
            stock_quantity (int): Available stock.
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
        self.stock_quantity = stock_quantity
        Product._total_products += 1
        Product._category_popularity[category] += 1

    def get_product_info(self):
        """Returns a dictionary with product information."""
        return {
            "ID": self.product_id,
            "Name": self.name,
            "Price": self.price,
            "Category": self.category,
            "Stock": self.stock_quantity,
        }

    def update_stock(self, quantity):
        """Updates the stock quantity. A negative value decreases stock."""
        if self.stock_quantity + quantity < 0:
            return "Error: Not enough stock."
        self.stock_quantity += quantity
        return "Stock updated."

    @classmethod
    def get_total_products(cls):
        """Returns the total number of unique products in the system."""
        return cls._total_products

    @classmethod
    def get_most_popular_category(cls):
        """Returns the category with the most products."""
        if not cls._category_popularity:
            return None
        return cls._category_popularity.most_common(1)[0][0]


class Customer:
    """
    Represents a customer, managing their information and discount eligibility.
    """

    _total_revenue = 0

    def __init__(self, customer_id, name, email, membership_level="standard"):
        """
        Initializes a new Customer.

        Args:
            customer_id (str): Unique ID for the customer.
            name (str): Customer's name.
            email (str): Customer's email.
            membership_level (str): 'standard', 'premium', or 'vip'.
        """
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.membership_level = membership_level

    def get_discount_rate(self):
        """Returns the discount rate based on membership level."""
        if self.membership_level == "premium":
            return 10  # 10% discount
        elif self.membership_level == "vip":
            return 20  # 20% discount
        return 0  # 0% discount

    def __str__(self):
        return (
            f"Customer: {self.name} ({self.email}), Membership: {self.membership_level}"
        )

    @classmethod
    def get_total_revenue(cls):
        """Returns the total revenue from all customers."""
        return cls._total_revenue

    @classmethod
    def add_revenue(cls, amount):
        """Adds to the total revenue."""
        cls._total_revenue += amount


class ShoppingCart:
    """
    Manages a collection of products for a customer, handling cart operations
    and order placement.
    """

    def __init__(self, customer):
        """
        Initializes a ShoppingCart for a specific customer.

        Args:
            customer (Customer): The customer associated with the cart.
        """
        self.customer = customer
        self.items = {}  # {product_id: {'product': product_object, 'quantity': count}}

    def add_item(self, product, quantity=1):
        """Adds a product to the cart."""
        if product.stock_quantity < quantity:
            return "Cannot add item: Not enough stock."

        if product.product_id in self.items:
            self.items[product.product_id]["quantity"] += quantity
        else:
            self.items[product.product_id] = {"product": product, "quantity": quantity}
        return f"Added {quantity} of {product.name} to cart."

    def remove_item(self, product_id):
        """Removes a product from the cart."""
        if product_id in self.items:
            del self.items[product_id]
            return "Item removed."
        return "Item not in cart."

    def get_cart_items(self):
        """Returns a list of items in the cart."""
        return [
            {"name": item["product"].name, "quantity": item["quantity"]}
            for item in self.items.values()
        ]

    def get_total_items(self):
        """Returns the total number of items in the cart."""
        return sum(item["quantity"] for item in self.items.values())

    def get_subtotal(self):
        """Calculates the subtotal before discounts."""
        return sum(
            item["product"].price * item["quantity"] for item in self.items.values()
        )

    def calculate_total(self):
        """Calculates the final total after applying customer discounts."""
        subtotal = self.get_subtotal()
        discount_rate = self.customer.get_discount_rate() / 100
        discount_amount = subtotal * discount_rate
        return subtotal - discount_amount

    def place_order(self):
        """Processes the order, updates stock, and clears the cart."""
        for item_info in self.items.values():
            product = item_info["product"]
            quantity = item_info["quantity"]
            if product.stock_quantity < quantity:
                return f"Order failed: Not enough stock for {product.name}."

        # All items are in stock, proceed with order
        final_total = self.calculate_total()
        for item_info in self.items.values():
            item_info["product"].update_stock(-item_info["quantity"])

        Customer.add_revenue(final_total)
        self.clear_cart()
        return f"Order placed successfully! Total: ${final_total:.2f}"

    def clear_cart(self):
        """Clears all items from the cart."""
        self.items = {}


# --- Test Cases ---

# Test Case 1: Creating products with different categories
laptop = Product("P001", "Gaming Laptop", 1299.99, "Electronics", 10)
book = Product("P002", "Python Programming", 49.99, "Books", 25)
shirt = Product("P003", "Cotton T-Shirt", 19.99, "Clothing", 50)

print(f"Product info: {laptop.get_product_info()}")
print(f"Total products in system: {Product.get_total_products()}")
print("-" * 30)

# Test Case 2: Creating customer and shopping cart
customer = Customer("C001", "John Doe", "john@email.com", "premium")
cart = ShoppingCart(customer)

print(f"Customer: {customer}")
print(f"Customer discount: {customer.get_discount_rate()}%")
print("-" * 30)

# Test Case 3: Adding items to cart
cart.add_item(laptop, 1)
cart.add_item(book, 2)
cart.add_item(shirt, 3)

print(f"Cart total items: {cart.get_total_items()}")
print(f"Cart subtotal: ${cart.get_subtotal():.2f}")
print("-" * 30)

# Test Case 4: Applying discounts and calculating final price
final_total = cart.calculate_total()
print(
    f"Final total (with {customer.get_discount_rate()}% discount): ${final_total:.2f}"
)
print("-" * 30)

# Test Case 5: Inventory management
print(f"Laptop stock before order: {laptop.stock_quantity}")
order_result = cart.place_order()
print(f"Order result: {order_result}")
print(f"Laptop stock after order: {laptop.stock_quantity}")
print("-" * 30)

# Test Case 6: Class methods for business analytics
popular_category = Product.get_most_popular_category()
print(f"Most popular category: {popular_category}")

total_revenue = Customer.get_total_revenue()
print(f"Total revenue: ${total_revenue:.2f}")
print("-" * 30)

# Test Case 7: Cart operations
# Re-add items to test removal
cart.add_item(laptop, 1)
cart.add_item(book, 1)
cart.remove_item("P002")  # Remove book
print(f"Items after removal: {cart.get_cart_items()}")

cart.clear_cart()
print(f"Items after clearing: {cart.get_total_items()}")
