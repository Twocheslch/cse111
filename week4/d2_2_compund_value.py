students = {
    #ID: [name,major,year]
    
}





if 104 not in students:
    students[104] = ["mary", "Art", 2]

print(students)

for key in students:
    print(key)

for value in students.values():
    print(value)

for key, value in students.items():
    print(key, value)

if 105 not in students:
    students[105] = ["John", "Business", 1]