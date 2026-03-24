#Type Python raises an exception when it encounters a problem while running the code
#there are many types od exceptions:
#ex) try to open a file that does not exist
#ex) user input was a float when it wasn't expected.

"""
Exception handeling follows this format:
try:
    regular code
    refular code
except (type of error) as error:
    do something specific for this error case

regular code
regular code
"""







#value error
while True:
    try:
        #normal code
        user_input = int(input("Please enter an integer "))
        break

    except ValueError as error:
        print(f"error valuerror: {error}")


