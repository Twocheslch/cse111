##This is a comment
#"this is a string"
#"""This is also a comment?"""
#
#print(15.67)
#
#familySize = 5
#price = 1.25 #this is a float
#lastName = "Jones" #This is a string
#isDone = False #This is a boolean
#friends = ["micky", "minnie", "daisy"] #array of variables
#testScore = {"mickey":65, "Minnie":98, "Mouse":99, } #This is a dictionary
#print(type(familySize), familySize)
#print(type(price), price)
#print(type(lastName), lastName)
#print(type(isDone), isDone)
#print(type(friends), friends)
#print(type(testScore), testScore)
#print(type(familySize), familySize)
#
##getting user input
#item = input("Item Name?")
#itemPrice = float(input("Item Price?"))
#itemCount = float(input("Item Count?"))
#print(type(item), item)
#print(type(itemPrice), itemPrice)
#print(type(itemCount), itemCount)
#
#total = itemPrice * itemCount
#print(f"The total is: ${total:,.2f}")
#
##arithmatic operators
##+ - * / % **

#num1 = 3
#num2 = 5
#messy_number = num1 + num2 * num1 / num2 // num1 % num2 ** num1
#print(messy_number)
#
#total = 0
#
#for i in range(1, 11):
#    total+= i
#    print(total)
#
##total2 = 55
#
#for i in range(1, 11):
#    total-= i
#
#    if total % 2 == 0:
#        print(f"{total} is even")
#    else:
#        print(f"{total} is odd")
    
fruits = ["banana", "apple", "strawberry" ]

for i in fruits:
  if i == "strawberry":
    print(f"{i} is the last one")
    break
  print(i)

score = 89
grade = ""
if score >= 90:
    grade = "A"
elif score >= 80 and score <= 89:
    grade = "B"
elif score >=70 and score <= 79:
    grade = "C"

print(grade)