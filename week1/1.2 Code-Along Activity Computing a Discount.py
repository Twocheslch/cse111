#Use OS to find day, if (Tue or Wed) and total >= 50$, then reduce total price by 10%, 
#then add 6% sales tax

from datetime import datetime

ur = datetime.now()
day_name = ur.strftime("%A")

day = datetime.now().weekday()
#print(day)

#manual mode:
day = 0
#print(day)

isNumber = False
while isNumber == False:
    try:
        cart = float(input("Please enter cart subtotal: $"))
        isNumber = True
    except ValueError:
        print("Please enter a valid number.")

if cart >= 50 and (day == 1 or day == 2):
    cart -= cart * .10
    print("Midweek discount applied!")

cart += cart * 0.06
round(cart, 2)
print(cart)
