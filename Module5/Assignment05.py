# -- Info -- #
# Name: Priya Jaglal
# Assignment: #5
# Program Description: This program adds items to To Do List
# Date: 11/12/18
# ------------------------------------------------------------------------------------------------------------ #

# -- Functions -- #
# Function Name: options
# Function description: List options and save the selected option as an integer


def options():
    print("Menu of Options:\n1) Show current data")
    print("2) Add a new item. \n3) Remove an existing item. \n4) Save Data to File \n5) Exit Program")
    default = int(input("Please select a number: \n "))
    return default

# Function Name: Decisions
# Function Description: Computes based on option chosen by user


def decisions(choice=5):
    if choice == 1:
        print(table_dict)
        decisions(options())

    elif choice == 2:
        item = input("Please add another item to the list: ")
        priority = input("Please indicate the item's priority level: High/Med/Low")
        temp_dict = {"Item": item, "Priority": priority}
        table_dict.append(temp_dict)
        decisions(options())

    elif choice == 3:
        table_dict.pop()
        decisions(options())

    elif choice == 4:
        new_file = file_open()
        new_file.write(str(table_dict))
        new_file.close()
        decisions(options())
    elif choice == 5:
        new_file = file_open()
        new_file.write(str(table_dict))
        new_file.close()
        print("Bye :)")

    else:
        print("File not saved!")
        print("Later :P")

# Function Name: file_open
# Function Description: Opens To Do text file


def file_open():
    fh = open("C:\_PythonClass\To_Do.txt", "w")
    return fh


# 1. Create a text file using the following data:
if __name__ == '__main__':
    # Writing To Do items to new file
    new_file = open("C:\_PythonClass\To_Do.txt", "w")
    row1 = "Clean House, Low"
    row2 = "Pay Bills, High"
    table = [row1, row2]
    new_file.write(str(table))
    new_file.close()

    # 2. When the program starts, load each row of data from the
    # Text file into a Python dictionary. (The data will be stored like a row in a table.)
    new_file = open("C:\_PythonClass\To_Do.txt", "r")
    for line in new_file:
        table = line.split("'")
        item1 = table[1]
        item2 = table[3]
    new_file.close()
    dict_item = {}
    dict_item1 = {}
    table_dict = []

    while True:
        if len(table_dict) < 1:
            todo = item1.split(",")
            dict_item["Item"] = todo[0]
            dict_item["Priority"] = todo[1]
            table_dict.append(dict_item)
        elif len(table_dict) == 1 and len(table_dict) < 4:
            todo = item2.split(",")
            dict_item1["Item"] = todo[0]
            dict_item1["Priority"] = todo[1]
            table_dict.append(dict_item1)
        else:
            break

    print(table_dict)

    line3 = {}

    line3["Item"] = input("Please enter new item: ")
    line3["Priority"] = input("Please enter the priority level (High/Med/Low)")

    table_dict.append(line3)
    # 4. Display the contents of the List to the user.
    print(table_dict)
    # 5. Allow the user to Add or Remove tasks from the list using numbered choices. Something like this would work:
    #     Menu of Options
    #     1) Show current data
    #     2) Add a new item.
    #     3) Remove an existing item.
    #     4) Save Data to File
    #     5) Exit Program

    num = options()
    decisions(num)

# 6. Save the data from the table into the .txt file when the program exits.
