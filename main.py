from file_read import *
from file_write_append import *

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
            delete_table()

def add_to_table():
    '''
    '''

def modify_table():
    '''
    '''

def delete_table():
    '''
    '''

    # Need to remove table and re-write file


def preview_all_tables(database):
    '''
    '''
    # Make space beforehand
    print()
    print("----------")
    for table in database.get_all_table_names():
        print ("Table Name: " + table)
        print()
        database.get_table(table).print_table()
        # database.get_table(table).print_csv()
        print()
    print("Done!")
    print("----------")
    print()

def make_new_table():
    '''
    '''

def open_existing_table(database):
    '''
    '''
    print()
    list_of_tables = list(database.get_all_table_names())
    print("These are the courses you currently have: ")
    for table in list_of_tables:
        print(table)

    print()
    print("Which course do you want to open?")
    table_choice = input("Please enter the exact name as it is displayed above: ")
    while (table_choice not in list_of_tables):
        print("This course was not found in the database")
        table_choice = input("Please try again: ")
    database.get_table(table_choice).print_table()


if (__name__ == "__main__"):
    main()