import csv
from datetime import datetime


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    products_dict = {}

    with open(filename, "rt", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        for row_list in reader:
            key = row_list[key_column_index]
            products_dict[key] = row_list

    return products_dict


def print_receipt(products_dict, request_filename):
    print("Inkom Emporium")
    print()

    total_items = 0
    subtotal = 0

    with open(request_filename, "rt", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        for row_list in reader:
            product_id = row_list[0]
            quantity = int(row_list[1])

            product_info = products_dict[product_id]
            product_name = product_info[1]
            product_price = float(product_info[2])

            print(f"{product_name}: {quantity} @ {product_price:.2f}")

            total_items += quantity
            subtotal += quantity * product_price

    sales_tax = subtotal * 0.06
    total = subtotal + sales_tax

    print()
    print(f"Number of Items: {total_items}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Sales Tax: {sales_tax:.2f}")
    print(f"Total: {total:.2f}")
    print()
    print("Thank you for shopping at the Inkom Emporium.")
    print()

    current_date_and_time = datetime.now()
    print(f"{current_date_and_time:%a %b %d %I:%M:%S %p %Y}")


def main():
    try:
        products_dict = read_dictionary("week5/products.csv", 0)
        print_receipt(products_dict, "week5/request.csv")

    except FileNotFoundError as file_not_found_err:
        print("Error: missing file")
        print(file_not_found_err)

    except KeyError as key_err:
        print("Error: unknown product ID in the request file")
        print(key_err)


if __name__ == "__main__":
    main()