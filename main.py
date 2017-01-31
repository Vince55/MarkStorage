from file_read import *
from file_write_append import *

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
        open_existing_table()


def preview_all_tables(database):
    '''
    '''
    # Make space beforehand
    print()
    print("----------")
    for table in database.get_all_table_names():
        print ("Name: " + table)
        database.get_table(table).print_table()
        # database.get_table(table).print_csv()
        print()
    print("Done!")
    print("----------")
    print()

def make_new_table():
    '''
    '''

def open_existing_table():
    '''
    '''


if (__name__ == "__main__"):
    main()