"""
There are two ways to call sorted
creates a new sorted list (will not touch the original list)

sorted(list)
sorted(list, key=func)

This will reorder the original list
list.sort() 
"""

numbers = [2,4,6,2,4,6,4,6,19,8,3,3,8]
print(sorted(numbers))
#sorted(numbers) does NOT change the original list
print(numbers)

#This sorts the original and changes it
numbers.sort()
print(numbers)

#This also sorts alphabetically
letters = ["d", "a", 'c', 'b']
print(sorted(letters))

#, reverse = True will reverse the order of the sort
#:3 will only print a range, in this case being 3. You don't have to write 0:3 because it's implied
#-3: will only print the last 3. If you don't put anything in the end, it'll just go to the 
#end of the list
scores = [99, 25, 40, 81, 63, 26, 84, 26, 71]
sorted_scores = sorted(scores, reverse=True)
print(sorted_scores)
print(sorted_scores[:3])
print(sorted_scores[-3:])

#here we will sort by the order of the length of each word. We can see that the key by which it sorts
#is the function len(). 
words = ['banana', 'apple', 'zuchini', 'kiwi']
print(sorted(words, key=len, reverse=True))

#product id, name, price, quantity
inventory = [
    ["L-001", "laptop", 1200, 5],
    ["m-020", "mouse", 25, 50],
    ["m-101", "monitor", 300, 12],
    ["k-053", "keyboard", 75, 20],
]
#here, we sort the inventory by item price
#in lambda, the first item here could be anything, x, y, z, whatever.
by_price = sorted(inventory, key=lambda item: item[2])
print(by_price)

#here it is by quantity
by_quant = sorted(inventory, key=lambda item: item[3])
print(by_quant)

#sort by productID. Specifically, though, this strips the first two characters
#with the 2: we start at the second item (starting from 0) then continue to the end
# which is the letter and the hyphen
by_product_id = sorted(inventory, key=lambda item: item[0][2:])
print(by_product_id)