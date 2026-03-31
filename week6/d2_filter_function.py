"""
The prototype for the filter function is filter(test_func returns true/false, list[] )
return only matching items in the list
"""
ages = [4, 15, 43, 38, 64, 29, 12, 10, 9, 50]
#we want to get only ones 18 and above. We can do this with filter function
adults = list(filter(lambda x: x >= 18, ages))
print(adults)


heights = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28,]
min_height = 18
#we need to find minimum height requirement

height_check = list(filter(lambda height: height>=min_height, heights))
print(height_check)

#this finds the current date, and ocmpares it to what is in the list
from datetime import date
today = date.today()
print(today)
due_dates = [ date(2026,3,1), date(2026,4,15), date(2026,3,24)]
overdue = list(filter(lambda date: date < today, due_dates))
print(overdue)



