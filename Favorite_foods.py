Favorite_foods = ["Turtang talong", "adobo", "humba", "seafoods", "calamares"]
print("The entire list of my favorite foods: ", Favorite_foods)
print("The first food in the list:", Favorite_foods[0])
print("The last food in the list:", Favorite_foods[-1])

add_foods = input("add a new food to the list: ")
Favorite_foods.append(add_foods)
removed_foods = input("removed one from the list: ")
Favorite_foods.remove(removed_foods)
print("The updated list of my favorite foods: ", Favorite_foods)

Foods_tuple = tuple(Favorite_foods)
print("The list stored as a tuple:", Favorite_foods)
