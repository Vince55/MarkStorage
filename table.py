class RowsUnevenError(Exception):
    '''An error to be raised when the rows are uneven upon adding a dictionary
    '''

class Table():
    '''A class to represent a table'''

    def __init__(self):
        '''(Table) -> Nonetype
        Initializing a table (data) with a dictionary.
        '''
        self._data = {}
        # Default preferences
        self._header_preferences = [
            "Name", "Mark", "Weight", "Percentage Of Total"]

    def set_column(self, column_name, data):
        '''(Table, str, str) -> NoneType
        Adds a column to the table. Done by adding a header-key pair to the
        table.
        '''
        self._data[column_name] = data

    def delete_column(self, column_name):
        '''(Table, str) -> NoneType
        Deletes a column from the table, given the column's name.
        '''
        del self._data[column_name]

    def get_headers(self):
        '''(Table) -> list of str
        Returns a list of the names of columns.
        '''
        header_list = list(self._data.keys())
        return header_list

    def set_row(self, row_num, data):
        '''(Table, int, str) -> NoneType
        Adds a row to the table. Done by adding each element of the row into
        its respective columns.
        '''
        pass

    def delete_row(self, row_index):
        '''(Table, int) -> NoneType
        Deletes a column from the table, given the row number (header doesn't
        count).
        '''
        header_list = self.get_headers
        for header in header_list:
            self.delete_item(header, row_num)

    def set_item(self, column_name, row_index, item):
        '''(Table, str, int, str) -> NoneType
        Sets a value (overwriting if a value is already set in that location)
        given the column and row for the respective table.
        '''
        # what if the row doesn't exist
        # what if an item is already/not there?
        pass

    def set_item(self, column_name, item):
        '''(Table, str, str) -> NoneType
        Adds a value to the end of a given column of a table.
        '''
        # what if the row doesn't exist
        # what if an item is already/not there?
        self._data[column_name].append(item)

    def get_item(self, column_name, row_index):
        '''(Table, str, int) -> str
        Returns the string at a given column and row of a table.
        '''
        return self._data[column_name][row_index]

    def delete_item(self, column_name, row_index):
        '''(Table, str, int) -> NoneType
        Deletes an itemn from the table, given the row number and column of the
        table.
        '''
        del self._data[column_name][row_index]

    def num_rows(self):
        '''(Table) -> int
        Returns the number of rows in the table
        '''
        # Start at 0
        row_number = 0
        # Need to get keys so a column can be accessed, can't arbitrarly pick
        # a random column
        keys = self.get_headers()
        # If columns exist
        if (len(keys) != 0):
            # Get the first one
            row_number = len(self._data[keys[0]])
        return row_number

    def print_csv(self):
        '''(Table) -> NoneType
        Print a representation of table in csv format.
        '''
        # no need to edit this one, but you may find it useful (you're welcome)
        dict_rep = self._data
        columns = list(dict_rep.keys())
        print(','.join(columns))
        rows = self.num_rows()
        for i in range(rows):
            cur_column = []
            for column in columns:
                cur_column.append(dict_rep[column][i])
            print(','.join(cur_column))

    def print_table(self):
        '''(Table) -> NoneType
        Print a representation of table in a more visually clean table format.
        '''
        dict_rep = self._data
        # all the representations
        str_lines = []

        # largest str
        largest_str = 0
        columns = list(dict_rep.keys())
        columns = self.header_preference_sorter(columns)
        if columns:
            # Find length of first column
            length = len(dict_rep[columns[0]])
            # Add the row, remember to add one for the column too
            for row in range(length + 1):
                str_lines.append("")

        # for every column
        for column in columns:
            # read the column first
            word = column
            if len(word) > largest_str:
                # record number
                largest_str = len(word)

            # go through every row in column
            for row in range(self.num_rows()):
                # if larger
                word = dict_rep[column][row]
                if len(word) > largest_str:
                    # record number
                    largest_str = len(word)

            # the length of the largest one + 1 is where the next column starts
            # add the item, then add the max length - what was already taken up
            # in spaces to the end of the string

            # also to represent the column to also be added
            str_lines[0] += column
            str_lines[0] += (largest_str - len(column) + 1) * " "
            for row in range(0, self.num_rows()):
                # add the column to the string representation so far
                word = dict_rep[column][row]
                str_lines[row + 1] += word
                str_lines[row + 1] += (largest_str - len(word) + 1) * " "
            largest_str = 0
        # when done, print every line
        for row in str_lines:
            print(row)

    def header_preference_sorter(self, input_headers):
        '''(Table, list of str) -> list of str
        Given a list of headers, with each header indexed by its preference,
        sorts the current table's headers such that it aligns with that of the
        given list. The purpose of returning an ordered list is to display the
        headers later in an ordered manner. Note that a list of default
        preferences are automaticaly for each table upon set-up.
        '''
        sorted_list = []
        # Go through every header in order
        for header in self._header_preferences:
            # If it is in the database
            if header in input_headers:
                # Add it next in priority and remove from original list
                sorted_list.append(header)
                input_headers.remove(header)
        # Add the rest back
        for header in input_headers:
            sorted_list.append(header)
        return sorted_list


class Database():
    ''' A class to represent a database'''

    def __init__(self):
        '''(Database) -> NoneType
        Initialize database with a dictionary.
        '''
        # Dictionaries enable fast lookup, deletion and insertion
        # Similar to hashmap
        self._data = {}

    def add_table(self, table_name, table):
        '''(Database, str, Table) -> NoneType
        Add a table name-Table pair as a key-value pair into the database
        REQ: table_name must not already exist in the database
        '''
        self._data[table_name] = table

    def get_table(self, table_name):
        '''(Database) -> Table
        Returns the table mapped to the given table_name
        REQ: table_name must exist in the database
        '''
        # Get the value mapped to the table_name
        return self._data[table_name]

    def get_all_table_names(self):
        '''(Database) -> list of str
        Returns a list of the names of tables in the database.
        '''
        # Table names are stored as keys in the database
        return self._data.keys()

    def delete_table(self, table_name):
        '''(Database, str) -> NoneType
        Removes a table from the database given its name, or key value.
        '''
        del self._data[table]
