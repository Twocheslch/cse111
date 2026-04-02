#JSON stands for JavaScript Object Notation
#Is used for data interchange. It's a data interchange format.
#.json files are lists with dictionaries within

import json

#with open("week6/users.json") as file:
   # users = json.load(file)
   # print(users)

import sys

def read_my_json(file_name):
    try:
        with open(file_name) as file:
            json_list = json.load(file)
            return json_list
    except FileNotFoundError as error:
        print(error)
        print(f"error, the file {file_name} does not exist!")
        raise SystemExit("The file does not exist!")
    except json.JSONDecodeError as error:
        print(error)
        print(f"error, the file name {file_name} contains invalid JSON formatting!")
        raise SystemExit("Cannot read JSON file.")
    
json_list = read_my_json("week6/users.json")
print(json_list)

def add_user(new_user, path="week6/users.json"):
    json_list = read_my_json(path)
    json_list.append(new_user)
    print(json_list)
    with open(path, "w") as file:
        #just indents 2 spaces for all of them
        #dump adds a new line
        json.dump(json_list, file, indent=2)
        

user = {
    "name": "Donald Duck",
    "age": 23
}

add_user(user)