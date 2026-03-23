with open("disney.csv", mode="w") as file:
    file.write("ID, Name, Major, Year\n")
    file.write("I10,Mickey Mouse,Art,Freshman,\n")
    file.write("I11,Minnie Mouse,PE,Junior\n")

import csv
with open("disney.csv", mode="r") as file:
    reader = csv.reader(file)
    disney_dict = {}
    