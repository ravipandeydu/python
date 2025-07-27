from collections import Counter, defaultdict

# Given data from the image
posts = [
    {"id": 1, "user": "alice", "content": "Love Python programming!", "likes": 15, "tags": ["python", "coding"]},
    {"id": 2, "user": "bob", "content": "Great weather today", "likes": 8, "tags": ["weather", "life"]},
    {"id": 3, "user": "alice", "content": "Data structures are fun", "likes": 22, "tags": ["python", "learning"]},
    {"id": 4, "user": "bob", "content": "Learning new things", "likes": 12, "tags": ["learning", "tech"]},
    {"id": 5, "user": "charlie", "content": "Exploring data science", "likes": 30, "tags": ["data science", "python", "analytics"]}
]

users = {
    "alice": {"followers": 150, "following": 75},
    "bob": {"followers": 89, "following": 120},
    "charlie": {"followers": 200, "following": 100}
}

print("--- Initial Social Media Data ---")
print("Posts:")
import json
print(json.dumps(posts, indent=2))
print("\nUsers:")
print(json.dumps(users, indent=2))

# Task 1: Most Popular Tags – Use collections.Counter to find the most frequent tags across posts.
print("\n--- Task 1: Most Popular Tags ---")
all_tags = []
for post in posts:
    all_tags.extend(post["tags"])

tag_counts = Counter(all_tags)
print("Most frequent tags:")
for tag, count in tag_counts.most_common(5): # Display top 5 most common tags
    print(f"- #{tag}: {count} times")

# Task 2: User Engagement Analysis – Use defaultdict to compute total likes per user.
print("\n--- Task 2: User Engagement Analysis (Total Likes per User) ---")
user_likes = defaultdict(int) # Default value for int is 0
for post in posts:
    user_likes[post["user"]] += post["likes"]

print("Total likes per user:")
for user, likes in user_likes.items():
    print(f"- {user.capitalize()}: {likes} likes")

# Task 3: Top Posts by Likes – Use sorted() to list posts in descending order of likes.
print("\n--- Task 3: Top Posts by Likes ---")
# Sort posts by 'likes' in descending order
top_posts_by_likes = sorted(posts, key=lambda post: post["likes"], reverse=True)

print("Posts sorted by likes (descending):")
for post in top_posts_by_likes:
    print(f"- Post ID: {post['id']}, User: {post['user'].capitalize()}, Likes: {post['likes']}, Content: \"{post['content'][:30]}...\"") # Truncate content for display

# Task 4: User Activity Summary – Combine post and user data to generate a summary per user.
print("\n--- Task 4: User Activity Summary ---")
user_activity_summary = {}

# Initialize summary with user details
for user_name, user_data in users.items():
    user_activity_summary[user_name] = {
        "posts_count": 0,
        "total_likes_received": 0,
        "followers": user_data["followers"],
        "following": user_data["following"]
    }

# Populate posts count and total likes from posts data
for post in posts:
    user = post["user"]
    if user in user_activity_summary:
        user_activity_summary[user]["posts_count"] += 1
        user_activity_summary[user]["total_likes_received"] += post["likes"]
    # Handle cases where a post user might not be in the initial users dictionary
    else:
        user_activity_summary[user] = {
            "posts_count": 1,
            "total_likes_received": post["likes"],
            "followers": 0, # Default for users not in initial 'users' dict
            "following": 0  # Default for users not in initial 'users' dict
        }

print("User Activity Summary:")
print(json.dumps(user_activity_summary, indent=2))