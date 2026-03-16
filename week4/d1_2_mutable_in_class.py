"""imutable values"""
# immutable: cannot change the value
# Cannot change the value
# Examples:
# str, int, float, bool



my_age = 19                 #These numbers are immutable. So their internal addresses are different.
your_age = my_age           #so when you make one equal to another, only one gets changed.
my_age += 1
print(my_age)
print(your_age)

#lists are mutable
#this means that the values of elements in the list can be changed

my_age_1 = [19]                 #The internal adresses for both of these age_ls is the exact same. So when you change one, the other gets changed too.
your_age_l = my_age_1           #They both get changed
my_age_1[0] = my_age_1[0] +1
print(my_age_1)
print(your_age_l)
your_age_l[0] += 1
print(my_age_1)
print(your_age_l)


def double(numbers):
    assert isinstance(numbers, list)
    for i in range(len(numbers)):
        numbers[i] *= 2

numbers = [1, 2, 3,]
print(numbers)

double(numbers)
print(numbers)
#here, we can see that the updated value of the list "numbers" is changed outside of the function too.

def double_int(number):
    number *= 2
    return number

number = 4
print(number)

return_number = double_int(number)
print(number)
print(return_number)
#here we can see that the number that gets changed inside the function is different from the global number











