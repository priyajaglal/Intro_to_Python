# Function description: List out the menu options for the user
def menu():
    print("Menu of Options:\n1) Show current data")
    print("2) Add a new item. \n3) Remove an existing item. \n4) Save Data to File \n5) Exit Program")


# Function Description: Opens text file in the specified mode "read", "write", "append"
def file_open(status):
    fh = open("C:\_PythonClass\To_Do.txt", status)
    return fh


# Function Description: returns the choice made as an integer
def menu_input():
    default = int(input("Please select a number: \t "))
    return default


# Function description: prints the current list of items (to be saved)
def current_list():
    print(table_dict)


# Function Description: Saves the same file
def save_file():
    fh = file_open("w")
    fh.write(str(table_dict))
    fh.close()


# Function description: edits the list of items based on user's choice
def add_remove(choice):
    if choice == 2:
        item = input("Please add another item to the list: ")
        priority = input("Please indicate the item's priority level: High/Med/Low")
        temp_dict = {"Item": item, "Priority": priority}
        table_dict.append(temp_dict)
    elif choice == 3:
        current_list()
        number = int(input("What item would you like to remove?: "))
        table_dict.pop(number)
    else:
        print("Error")


# Function opens txt file and creates a dictionary with the contents
def list_to_dict():
    fh = file_open("r")
    for line in fh:
        table = line.split("'")
        item1 = table[1]
        item2 = table[3]
    new_file.close()

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
    return table_dict


# Function description: prints the menu and ask of futher instruction
def repeat():
    print(menu())
    num = menu_input()
    return num


if __name__ == '__main__':
    table = []
    dict_item = {}
    dict_item1 = {}
    table_dict = []

    # Writing To Do items to new file
    new_file = file_open("w")
    row1 = "Clean House, Low"
    row2 = "Pay Bills, High"
    table_1 = [row1, row2]
    new_file.write(str(table_1))
    new_file.close()

table_dict = list_to_dict()

# Prompting user for 1st additional item
add_remove(2)
current_list()

print(menu())
choice = menu_input()

while True:
    if choice == 1:
        current_list()
        choice = repeat()
        continue
    elif choice == 2 or choice == 3:
        add_remove(choice)
        choice = repeat()
        continue
    elif choice == 4:
        save_file()
        choice = repeat()
        continue
    else:
        print("Bye!")
        save_file()
        break
