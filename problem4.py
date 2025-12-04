recipe = {
    "flour": 500,
    "sugar": 200,
    "eggs": 3,
    "milk": 100,
    "vanilla": 5
}
pantry = {
    "flour": 400,       # We have some, but not enough (need 100 more)
    "eggs": 10,         # We have plenty (need 0)
    "milk": 100,        # We have exact amount (need 0)
    # sugar is missing completely (need 200)
    # vanilla is missing completely (need 5)
}

def smart_kitchen(recipe, pantry):
    shopping_list = {}
    for item, value in recipe.items():
        if value > pantry.get(item, 0):
            needed = pantry.get(item, 0) - value
            shopping_list[item] = needed
    print("\nShopping List:")
    for item, value in shopping_list.items():
        print(f"{item}: {abs(value)}")
    print()

smart_kitchen(recipe, pantry)