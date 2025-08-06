def analyze_friendships():
    """
    Analyzes friendship patterns across different social media platforms using sets.

    Performs several analyses based on predefined friend lists and returns the results
    in a dictionary.
    """
    # User friends on different platforms
    facebook_friends = {"alice", "bob", "charlie", "diana", "eve", "frank"}
    instagram_friends = {"bob", "charlie", "grace", "henry", "alice", "ivan"}
    twitter_friends = {"alice", "diana", "grace", "jack", "bob", "karen"}
    linkedin_friends = {"charlie", "diana", "frank", "grace", "luke", "mary"}

    # --- Your tasks ---

    # 1. Find friends who are on ALL four platforms
    # This is the intersection of all four sets.
    all_platforms = (
        facebook_friends & instagram_friends & twitter_friends & linkedin_friends
    )

    # 2. Find friends who are ONLY on Facebook (not on any other platform)
    # This is the difference between the Facebook set and the union of all other sets.
    other_platforms = instagram_friends | twitter_friends | linkedin_friends
    facebook_only = facebook_friends - other_platforms

    # 3. Find friends who are on Instagram OR Twitter but NOT on both
    # This is the symmetric difference (XOR) between the two sets.
    instagram_xor_twitter = instagram_friends ^ twitter_friends

    # 4. Find the total unique friends across all platforms
    # This is the size of the union of all four sets.
    all_unique_friends = (
        facebook_friends | instagram_friends | twitter_friends | linkedin_friends
    )
    total_unique = len(all_unique_friends)

    # 5. Find friends who are on exactly 2 platforms
    # First, find everyone who is on at least two platforms by getting the union of all pairwise intersections.
    # Then, find everyone who is on at least three platforms by getting the union of all triplet intersections.
    # The final result is the difference between these two sets.
    on_two_or_more = (
        (facebook_friends & instagram_friends)
        | (facebook_friends & twitter_friends)
        | (facebook_friends & linkedin_friends)
        | (instagram_friends & twitter_friends)
        | (instagram_friends & linkedin_friends)
        | (twitter_friends & linkedin_friends)
    )

    on_three_or_more = (
        (facebook_friends & instagram_friends & twitter_friends)
        | (facebook_friends & instagram_friends & linkedin_friends)
        | (facebook_friends & twitter_friends & linkedin_friends)
        | (instagram_friends & twitter_friends & linkedin_friends)
    )

    exactly_two_platforms = on_two_or_more - on_three_or_more

    # Return a dictionary with all results
    results = {
        "all_platforms": all_platforms,
        "facebook_only": facebook_only,
        "instagram_xor_twitter": instagram_xor_twitter,
        "total_unique": total_unique,
        "exactly_two_platforms": exactly_two_platforms,
    }
    return results


# Test your function
result = analyze_friendships()
print("All platforms:", result.get("all_platforms"))
print("Facebook only:", result.get("facebook_only"))
print("Instagram XOR Twitter:", result.get("instagram_xor_twitter"))
print("Total unique friends:", result.get("total_unique"))
print("Exactly 2 platforms:", result.get("exactly_two_platforms"))
