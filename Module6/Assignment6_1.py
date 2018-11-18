# Function description: List out the menu options for the user
def menu():
    menu_options = "Menu of Options:\n" \
                   "1) Show current data\n" \
                   "2) Add a new item.\n" \
                   "3) Remove an existing item.\n" \
                   "4) Save Data to File\n" \
                   "5) Exit Program\n"
    return menu_options


# Function Description: Opens text file in the specified mode "read", "write", "append"
def file_open(status):
    fh = open("C:\_PythonClass\ToDo.txt", status)
    return fh


# Function Description: returns the choice made as an integer
def menu_input():
    default = int(input("Please select a number: "))
    return default


# Function description: prints the current list of items (to be saved)
def display_items(data_dict):
    print('\nCurrent Data: ')
    for request in data_dict.keys():
        print('{} = {}'.format(request, data_dict[request]))
    print()
    return True


# Function Description: Saves the same file
def save_file(data_dict):
    s_fh = file_open("w")
    for request in data_dict.keys():
        s_fh.write('{},{}\n'.format(request, data_dict[request]))
    s_fh.close()
    print("File saved!")
    return True


def add_item(data_dict):
    item = input("Please enter another request: ")
    priority = input("Please enter priority for request (High,Low): ")
    data_dict[item] = priority
    return data_dict


def remove_item(data_dict):
    display_items(data_dict)
    item = input("Please enter request to be remove: ")
    del data_dict[item]
    return data_dict


def load_data():
    l_fh = file_open('r')
    request_priority_dict = {}

    for line in l_fh.readlines():
        line_list = line.split(',')
        request_priority_dict[line_list[0]] = line_list[1].strip('\n')
    l_fh.close()
    return request_priority_dict


if __name__ == '__main__':
    dict_holder = load_data()

    while True:
        print(menu())
        choice = menu_input()

        if choice == 1:
            display_items(dict_holder)
        elif choice == 2:
            add_item(dict_holder)
        elif choice == 3:
            remove_item(dict_holder)
        elif choice == 4:
            save_file(dict_holder)
        elif choice == 5:
            print("Exiting program.")
            break
        else:
            print("Unknown choice {}".format(choice))
            break
