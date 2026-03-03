age = 18

def global_age():
    print(f"global age is {age}")

global_age()

def local_age():
    age=21
    print(f"local age is {age}.")
    
print(f"{age}")
local_age()

def global_overide():
    global age
    age = 25
    print(f"global overide is :{age}")
global_overide()
print(age)