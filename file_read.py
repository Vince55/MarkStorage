# Functions that can read files into tables and databases

from table import *

def read_file_into_table(file_name):
    '''(str) -> Table
    Return a table object with header-list pairs as key-value pairs from
    reading in and processing a valid csv. file. Processes by reading in each
    line in order in the file, separates each element and each header and
    allocated the header as a key and each element into lists that are mapped
    as values to each key.
    REQ: file_name must exist
    '''
    # Creating file handle
    file_handle_read = open(file_name, "r")
    table = Table()

    # Read in line containing all the headers
    table_header_names = file_handle_read.readline().rstrip()
    # Split the line into pieces containing each header
    table_headers_list = table_header_names.split(",")

    # Goes through every header in the list by its index
    for header_pos in range(len(table_headers_list)):
        # Uses index to access header in list, strips whitespace
        table_headers_list[header_pos] = table_headers_list[header_pos].strip()
        # Adds it to the table as a new header with an empty list
        table.set_column(table_headers_list[header_pos], [])

    # Preparing to read in rest of data
    next_row = file_handle_read.readline().rstrip()

    # As long as there are more lines to read, read another
    while(next_row != ''):
        # Gets the row, breaks up the data
        line_data = next_row.split(",")

        # Iterates through data in row
        for column in range(len(table_headers_list)):
            # Adds it to its respective list(header identified by position in
            # the header list, also known as table_headers_list
            table.set_item(
                table_headers_list[column], line_data[column].strip())

        # Repeat reading lines, getting rid off all blank lines from the end
        next_row = file_handle_read.readline().rstrip()

    # Close the file once done with the file
    file_handle_read.close()

    # Return the table object
    return table


def read_database():
    '''() -> Database
    Return a database object with table name-Table pairs as key-value pairs
    from reading and processing all the csv. files in its directory. Reads in
    each file name and converts it into keys, while each file is read and then
    converted into each keys respective table
    '''
    # Get all the files
    file_list = glob.glob('*.csv')

    # Create an initial database
    database = Database()

    # Go through every file in the list
    for file_name in file_list:
        # Create a table, then add it
        table_to_add = read_table(file_name)
        # Create a table name, then add the table and table name to database
        database.add_table(file_name[:-4], table_to_add)

    # Return the database object
    return database

if (__name__ == "__main__"):
    my_table = read_file_into_table("test_file.csv")

    dict_rep = my_table._data
    column_list = list(dict_rep.keys())
    print(','.join(column_list))
    num_rows = my_table.num_rows()
    for i in range(num_rows-1):
        cur_column = []
        for column in column_list:
            cur_column.append(dict_rep[column][i])
        print(','.join(cur_column))

    print(dict_rep)
