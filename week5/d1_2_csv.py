with open("hymns.csv", mode="w") as file:
    file.write("number, title\n")
    file.write('7, "Israel, Israel, God is calling"\n')
    file.write('30, "come, come, come me saints"\n')

import csv

with open("hymns.csv") as file:
    reader = csv.reader(file)
    for line in reader:
        print(f"1 {line}")
    file.seek(0)
    for line in reader:
        print(f"2 {line}")
    file.seek(0)
    next(reader)
    hymns_dict = {}
    for key, value in reader:
        hymns_dict[key] = value
    print(hymns_dict)
