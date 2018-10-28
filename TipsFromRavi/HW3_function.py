def take_usr_input(request_statement):
    return input(request_statement)


if __name__ == '__main__':
    household_item = ()
    while True:
        temp_tuple = ()

        item = take_usr_input(request_statement="Please enter name of household item: "),
        if item[0]:
            temp_tuple += item
            value = take_usr_input(request_statement="Please enter the estimated value of item: "),
            if value[0]:
                temp_tuple += value
            else:
                break
        else:
            break
        household_item += temp_tuple
    save = take_usr_input("Do you want to save this information?(Y/N)")
    if save.upper() == "Y":
        txt_file = open("C:\_PythonClass\HomeInventory.txt", "a")
        for i in range(0, len(household_item), 2):
            txt_file.write("Your {0} has an estimated cost of ${1}\n".format(household_item[i], household_item[i + 1]))
        txt_file.close()
    else:
        print("Not saving to file: Exiting")
