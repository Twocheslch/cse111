#makes a list of fruits
fruits = ["apple", "banana", "cherry"]
print(fruits)

#adds "grape" to the list
fruits.append("grape")
print(fruits)

#adds "lemon" to the list, but specifically at the 0th place
fruits.insert(0, "lemon")
print(fruits)

#finds the number index place at which "cherry" lies
cherry_index = fruits.index("cherry")
print(cherry_index)

#removes the item at cherry index
fruits.pop(cherry_index)
print(fruits)

#if no index, pops last item
fruits.pop()
print(fruits)

#.remove removes items, but errors if the item is not present
fruits.remove("apple")
print(fruits)

#.remove errors out if the item being removed is not present. So check first.
if "lemon" in fruits:
    fruits.remove("lemon")
print(fruits)

"""vegetable list excercise"""
vegetables = ["cabbage", "okra", "potato", "spinach", "asparagus", "broccoli", "mushroom"]

if "cabbage" in vegetables:
    vegetables.remove("cabbage")
print(vegetables)

vegetables.append("corn")
print(vegetables)

if "asparagus" in vegetables:
    vegetables.remove("asparagus")
    vegetables.insert(0, "asparagus")
print(vegetables)

#if "spinach" in vegetables and "spinach" != vegetables(1)
#checks if spinach exists, then if spinach is in the second to last place in the list.
#if not, then it moves spinach to the right place. We do this using len() which checks for the 
#length of the list.
number_of_items = len(vegetables)
spinach_place = vegetables.index("spinach")
if ("spinach" in vegetables) and (spinach_place != (number_of_items - 2)):
    vegetables.remove("spinach")
    place = number_of_items - 2
    vegetables.insert(place, "spinach")
    print(vegetables)
    
#if there are two duplicate items in a list, and you remove or call on one, the first item
#that matches will be selected.
vegetables.append("broccoli")
print(vegetables)
vegetables.remove("broccoli")
print(vegetables)












