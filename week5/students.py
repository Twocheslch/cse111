import csv

def read_dictionary(filename):
    next(filename)
    dictionary = {}
    for i in filename:
        print(f"this is I {i}")
    print(dictionary)
    return(dictionary)
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """


def main():
    with open("week5/students.csv", mode="r") as file:
        #csv reader converts csv files into a dictionary, in this case "reader"
        #reader = csv.DictReader(file)
        reader = csv.reader(file)
        read_dictionary(reader)
        #students = list(reader)
        #print(students)
        #print (reader)
        read_dictionary(reader)


if __name__ == "__main__":
    main()

