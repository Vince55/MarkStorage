from table import *

def write_to_file(course_name, table):
    '''
    '''
    file_handle_write = open("_" + course_name + " marks.csv", "w")

    file_handle_write.write("Can\nseparate\nlines\nlike\nthis\n")
    file_handle_write.write("Testing writing function\n")
    file_handle_write.write("Hello friends\n")
    file_handle_write.write("Harambe\n")

    the_dict = table._data
    header_list = list(the_dict.keys())
    # Write headers
    file_handle_write.write(','.join(header_list) + "\n")
    # Subtract reader row
    num_rows = table.num_rows() - 1
    for row in range(num_rows):
        cur_column = []
        # Add every piece in the row
        for column in header_list:
            cur_column.append(the_dict[column][row])
        # Write the row in
        file_handle_write.write(','.join(cur_column) + "\n")

    file_handle_write.close()

def append_existing_file(file_name, line):
    '''
    '''
    file_handle_append = open(file_name, "a")
    file_handle_append.write("Adding information to existing file\n")
    file_handle_append.write(line)
    file_handle_append.close()

if (__name__ == "__main__"):
    # Making a table and writing it to a file
    table1 = Table()
    table1._data = {'Weight': ['Par.', 'NL', 'BV'],
                    'Mark': [
                        'Titanic',
                        'The Lord of the Rings: The Return of the King',
                        'Toy Story 3'],
                    'Name': ['1997', '2003', '2010'],
                    'PercentageOfTotal': ['2186.8', '1119.9', '1063.2']}
    write_to_file("NewTable", table1)
    #write_to_file("Computer Science")
    #append_existing_file("Computer Science marks.csv", "#Leafs3016")
