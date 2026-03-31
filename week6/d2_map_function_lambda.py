numbers = [1,2,3,4,5]

def double(x):
    return x * 2

#list() is a cast? What does that mean
#Here, when you fit a function into a map, you remove the parenthesis from the function.
#This is the standard way
doubled = list(map(double, numbers))
print(doubled)

#lambda way:
#map function takes a function as a paramater,
#doubled is a list because we cast it as a list()
doubled = list(map(lambda x: x*2, numbers))

prices = [10, 20, 30]

tax = 1.06

def add_tax(price):
    return price*tax

#This is the normal way
with_tax = list(map(add_tax, prices))
print(with_tax)

#this is the lambda way:
with_tax = list(map(lambda p: p*tax, prices))
print(with_tax)

prices = [2.50, 5.75, 3.25]
quantities = [5, 4, 7]

#in lambda, the first variables in order (here is p, q) are assigned the values of the
#variables at the end (in this case it's prices, quantities)
total = list(map(lambda p, q: p*q, prices, quantities))
print(total)


sides = [5, 7, 9]
lengths = [10, 14, 18]

areas = list(map(lambda s, l: s*l, sides, lengths ))
print(f"{areas} areas")