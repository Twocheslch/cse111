#dictionary is a key value pair
#key must be unique - can only appear once
#dictionaries are mutable

#This is a dictionary. You can tell becasue of the {} and the :
fruit = {
    'name': 'apple',
    'color': "red",
    "count": 5
}

print(fruit)

value = fruit["name"]
#changes the color
fruit["color"] = "green"
#change the price
fruit["price"] = 0.50

print(fruit)
#remove the "color" index
del fruit["color"]

print(value)
print(fruit)
print(len(fruit))

total = fruit["price"] * fruit["count"]
print(f"${total}")