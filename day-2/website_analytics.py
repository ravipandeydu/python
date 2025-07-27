# Given sets of website visitors for three consecutive days
monday_visitors = {"user1", "user2", "user3", "user4", "user5"}
tuesday_visitors = {"user2", "user4", "user6", "user7", "user8"}
wednesday_visitors = {"user1", "user3", "user6", "user9", "user10"}

print("--- Website Visitor Data ---")
print(f"Monday Visitors: {monday_visitors}")
print(f"Tuesday Visitors: {tuesday_visitors}")
print(f"Wednesday Visitors: {wednesday_visitors}")

# Task 1: Unique Visitors Across All Days
print("\n--- Task 1: Unique Visitors Across All Days ---")
unique_visitors_all_days = monday_visitors.union(tuesday_visitors, wednesday_visitors)
print(f"Total unique visitors across all three days: {unique_visitors_all_days}")
print(f"Number of unique visitors: {len(unique_visitors_all_days)}")

# Task 2: Returning Visitors on Tuesday (visited on both Monday and Tuesday)
print("\n--- Task 2: Returning Visitors on Tuesday (Monday & Tuesday) ---")
returning_visitors_tuesday = monday_visitors.intersection(tuesday_visitors)
print(f"Visitors who visited on both Monday and Tuesday: {returning_visitors_tuesday}")

# Task 3: New Visitors Each Day
print("\n--- Task 3: New Visitors Each Day ---")
# New visitors on Tuesday (visited Tuesday but not Monday)
new_visitors_tuesday = tuesday_visitors.difference(monday_visitors)
print(f"New visitors on Tuesday (not seen on Monday): {new_visitors_tuesday}")

# New visitors on Wednesday (visited Wednesday but not on Monday or Tuesday)
new_visitors_wednesday = wednesday_visitors.difference(monday_visitors.union(tuesday_visitors))
print(f"New visitors on Wednesday (not seen on Monday or Tuesday): {new_visitors_wednesday}")

# Task 4: Loyal Visitors (visited on all three days)
print("\n--- Task 4: Loyal Visitors (visited on all three days) ---")
loyal_visitors = monday_visitors.intersection(tuesday_visitors, wednesday_visitors)
print(f"Visitors who visited on all three days: {loyal_visitors}")

# Task 5: Daily Visitor Overlap Analysis
print("\n--- Task 5: Daily Visitor Overlap Analysis ---")
overlap_mon_tue = monday_visitors.intersection(tuesday_visitors)
print(f"Overlap between Monday and Tuesday: {overlap_mon_tue}")

overlap_tue_wed = tuesday_visitors.intersection(wednesday_visitors)
print(f"Overlap between Tuesday and Wednesday: {overlap_tue_wed}")

overlap_mon_wed = monday_visitors.intersection(wednesday_visitors)
print(f"Overlap between Monday and Wednesday: {overlap_mon_wed}")