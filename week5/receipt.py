def read_dictionary(filename, key_column_index):
    students_dict = {}

    with open(filename, "rt", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        for row_list in reader:
            key = row_list[key_column_index]
            students_dict[key] = row_list
    print(students_dict)
    return students_dict





def main():
    read_dictionary("products.csv", 0)

if __name__ == "__main__":
    main()