# Given sales data from the image
sales_data = [
    ("Q1", [("Jan", 1000), ("Feb", 1200), ("Mar", 1100)]),
    ("Q2", [("Apr", 1300), ("May", 1250), ("Jun", 1400)]),
    ("Q3", [("Jul", 1350), ("Aug", 1450), ("Sep", 1300)])
]

print("--- Initial Sales Data ---")
for quarter, monthly_sales in sales_data:
    print(f"{quarter}: {monthly_sales}")

# Task 1: Calculate Total Sales per Quarter
print("\n--- Task 1: Total Sales per Quarter ---")
for quarter, monthly_sales_list in sales_data:
    total_quarter_sales = 0
    for month, sales_value in monthly_sales_list: # Unpacking inner tuples
        total_quarter_sales += sales_value
    print(f"Total sales for {quarter}: ${total_quarter_sales}")

# Task 2: Find the Month with Highest Sales
print("\n--- Task 2: Month with Highest Sales Across All Quarters ---")
highest_sales_value = -1
month_with_highest_sales = ""

for quarter, monthly_sales_list in sales_data:
    for month, sales_value in monthly_sales_list:
        if sales_value > highest_sales_value:
            highest_sales_value = sales_value
            month_with_highest_sales = month

print(f"Month with the highest sales: {month_with_highest_sales} (${highest_sales_value})")

# Task 3: Create a Flat List of All Monthly Sales
print("\n--- Task 3: Flat List of All Monthly Sales ---")
flat_monthly_sales = []
for _, monthly_sales_list in sales_data: # Using _ to ignore the quarter string
    flat_monthly_sales.extend(monthly_sales_list) # Extend with the list of (month, sales) tuples

print("Flat list of all monthly sales:")
print(flat_monthly_sales)

# Task 4: Use Unpacking in Loops to clearly separate months, sales values, and quarters.
print("\n--- Task 4: Demonstrating Unpacking in Loops ---")
print("Iterating through sales data with unpacking:")
for quarter_name, quarter_data in sales_data:
    print(f"\nProcessing {quarter_name}:")
    for month_name, sales_amount in quarter_data:
        print(f"  Month: {month_name}, Sales: ${sales_amount}")
