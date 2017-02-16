from file_read import *
from file_write_append import *
from user_input import *

def main():
    '''
    '''
    introductions()
    # What I should do for now is put all the source code into one folder and
    # put main into another
    # done
    # Reads in all existing table files into table
    # done
    # Tells the user the files it found
    # done
    # Asks user if they want to print everything or open one at a time
    # Add ability to do more than one at a time

    # Prints all the tables requested

    # Asks for command
    # Add, delete, calculate, close

def introductions():
    print("Welcome to Grade-a-base (still working on the name)")
    print("Loading previous courses...")

    # Make the database
    database = read_database()
    print("Done!")

    # Previewing all tables found
    print("Would you like to see a preview of the tables we found? Enter yes or no (yes/no):")
    preview_choice = input()
    while (preview_choice != "yes" and preview_choice != "no"):
        print("Please enter either \"yes\" or \"no\":")
        preview_choice = input()
    if (preview_choice == "yes"):
        preview_all_tables(database)

    # Asking whether to open old courses for editing or create a new one
    print("Would you like open previous courses or add a new one?")
    open_make_choice = input("Enter either open or make(open/make): ")
    while (open_make_choice != "open" and open_make_choice != "make"):
        print("Please enter either \"open\" or \"make\":")
        open_make_choice = input()
    if (open_make_choice == "make"):
        make_new_table()
    else:
        open_existing_table(database)

        editing_choices = ["add", "modify", "delete"]
        print()
        print("Would you like to add, modify or delete this table? (add/modify/delete)")
        add_modify_delete_choice = input()
        while (add_modify_delete_choice not in editing_choices):
            add_modify_delete_choice = input("Please enter an option: ")
        if (add_modify_delete_choice == "add"):
            add_to_table()
        elif (add_modify_delete_choice == "modify"):
            modify_table()
        else:
            delete_table(database, table)
    print("Exited successfully")

if (__name__ == "__main__"):
    main()