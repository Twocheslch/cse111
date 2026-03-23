#with open("date.txt") as file:
#    for line in file:
#        print(line)

#mode options on oprn(file_name, mode = "rt")
#r(read), w(write), a(apend), x(create a new file), 
#r+(read and write), w+(write and read), a+, x+,
#rb(read_from_binary_file), wb(write_to_binary_file), ab, xb,

with open("my.txt", mode="w") as file:
    file.write("I can write to a file\n")
    file.write("I am learning a new skill.\n")

with open("my.txt", mode="a") as file:
    file.write("whatup\n")
    file.write("idk\n")

with open("my.txt") as file:
    for line in file:
        print(line)
        print(line.strip)