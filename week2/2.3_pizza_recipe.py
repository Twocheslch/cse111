"""
Pizza recipe calculator.
find cups of flourand slices of pepperoni needed.

1cup of flour makes 40 in^2 of pizza.
1 pepperoni is needed per 4 in^2 of pizza.

define the following 4 functions:
compute_pizza_area(diameter(inches))
compute_pizza_volume(area(in^3), thickness(in) = 1)
find_cups_of_flour(volume(in^3))
find_slices of pepperoni(area(in^2))


"""





def find_cups_of_flour(volume):
    cup_count = volume / 40
    return cup_count
flour_cup_count = find_cups_of_flour(volume)
print(flour_cup_count)

def find_slices_of_pepperoni(area):
    pepperoni_count = area/4
    return pepperoni_count
pepperoni_count = find_slices_of_pepperoni(area)
print (round(pepperoni_count))

def main():
    diameter = float(input("diameter: "))
    thickness = float(input("How thick: "))
    area = compute_pizza_area(diameter)
    volume = compute_pizza_volume(area, thickness)
    flour_cup_count = find_cups_of_flour(volume)
    pepperoni_count = find_slices_of_pepperoni(area)
    print(f"a {diameter} inch pizza that is {thickness} inches thick should need {flour_cup_count} cups of flour and {pepperoni_count} pepperoni.")
if __name__ == "__main__":
    main()