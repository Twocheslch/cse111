import math
from datetime import datetime

now = datetime.now()

#print(f"{math.pi}")

w = int(input(f"The size of car tires in America are represented with three numbers, like this: 205/60R15. Please type in the first number of your car tire (EX: 205): "))
a = int(input(f"The size of car tires in America are represented with three numbers, like this: 205/60R15. Please type in the second number of your car tire (EX: 60): "))
d = int(input(f"The size of car tires in America are represented with three numbers, like this: 205/60R15. Please type in the third number of your car tire (EX: 15): "))

volume = (math.pi * w ** 2 * a * (w * a + 2540 * d)) / 10_000_000_000

print(volume)