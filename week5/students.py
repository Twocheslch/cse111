import csv


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
    students_dict = {}

    with open(filename, "rt", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        for row_list in reader:
            key = row_list[key_column_index]
            students_dict[key] = row_list

    return students_dict


def find_student(students_dict):
    """Get an I-Number from the user, verify the I-Number is
    valid, and find and print the student with that I-Number.
    """
    i_number = input("Please enter an I-Number (xxxxxxxxx): ")
    i_number = i_number.replace("-", "")

    if not i_number.isdigit():
        print("Invalid I-Number")
        return

    if len(i_number) < 9:
        print("Invalid I-Number: too few digits")
        return

    if len(i_number) > 9:
        print("Invalid I-Number: too many digits")
        return

    if i_number in students_dict:
        row = students_dict[i_number]
        print(row[1])
    else:
        print("No such student")


def main():
    students_dict = read_dictionary("week5/students.csv", 0)
    find_student(students_dict)


if __name__ == "__main__":
    main()