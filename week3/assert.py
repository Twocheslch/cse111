color = "white"
assert color == "white", "color must be white!"

def divide(dividend, divisor):
    assert divisor != 0, "divisor cannot be zero"
    return dividend / divisor

print(divide(10, 4))

