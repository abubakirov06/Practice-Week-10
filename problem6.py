def friend_recommender(users, target):
    same_interests = {}
    for user, interests in users.items():
        if user != target:
            for interest in interests:
                if interest in users[target]:
                    if user in same_interests:
                        same_interests[user] += 1
                    else:
                        same_interests[user] = 1
    for user in users:
        if user != target:
            if user not in same_interests:
                same_interests[user] = 0
    new_list = []
    for user, interest in same_interests.items():
        new_list.append([interest, user])
    new_list.sort()
    print()
    for name, interest in same_interests.items():
        print(f"Comparing Alice with {name}... {interest} shared interests.")
    print(f'------------------------------')
    print(f"Best match for Alice is {new_list[-1][1]} with {new_list[-1][0]} shared interests.\n")

users = {
    "Alice": ["Coding", "Music", "Hiking", "Pizza"],
    "Bob":   ["Movies", "Hiking", "Tacos"],
    "Charlie": ["Coding", "Pizza", "Gaming", "Music"],
    "David": ["Cooking", "Travel"]
}
target = "Alice"
friend_recommender(users, target)
