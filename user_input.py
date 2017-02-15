def add_to_table(table):
    '''
    '''
    pass

def modify_table(table):
    '''
    '''
    pass

def delete_table(table):
    '''
    '''
    pass

def make_new_table():
    '''
    '''
    pass

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
        print()
    print("Done!")
    print("----------")
    print()

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