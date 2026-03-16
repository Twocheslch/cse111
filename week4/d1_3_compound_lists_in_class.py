[[], []]
#this is a compound list. Lists within a list
inventory = [
    #[item, stock, unit price]
    ["laptops", 10, 800,],
    ["mice", 50, 25],
    ["keyboards", 30, 45],
    ["monitors", 15, 200]
]

print(inventory)

mouse_value = inventory[1][1] * inventory[1][2]
print(mouse_value)
#here we can see how to find indexes in a compound list. 
#The fist index item applies to the first list, so the first [1] finds ["mice", 50, 25]
#Then the second index searches within that. So the second [1] is 50. 

#remove monitor inventory by 5:
print(inventory[2][1])
inventory[2][1] -=5
print(inventory[2][1])
print(f"{inventory[2][0]} stock is {inventory[2][1]}")

for inner_list in inventory:
    if inner_list [1] < 20:
        print(f"WARNING: You have less than 20 {inner_list[0]} in stock!")
        print(f"you have {inner_list[1]} left.")









