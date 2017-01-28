def main():
    '''
    '''
    introductions()
    # What I should do for now is put all the source code into one folder and
    # put main into another

    # Reads in all existing table files into table

    # Tells the user the files it found

    # Asks user if they want to print everything or open one at a time
    # Add ability to do more than one at a time

    # Prints all the tables requested

    # Asks for command
    # Add, delete, calculate, close

def introductions():
    print("Welcome to Grade-a-base (still working on the name)")
    print("Would you like open previous courses or add a new one?")
    open_make_choice = input("Enter either open or make(open/make): ")
    while (open_make_choice != "open" and open_make_choice != "make"):
        print("Please enter either \"open\" or \"make\":")
        open_make_choice = input()
    if (open_make_choice == "make"):
        make_new_table()
    else:
        open_existing_table()


def make_new_table():
    '''
    '''

def open_existing_table():
    '''
    '''


if (__name__ == "__main__"):
    main()