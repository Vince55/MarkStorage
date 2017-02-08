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
        # Default preferences for header order
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
        # Table names are stored as keys in the database
        return list(self._data.keys())

    def set_row(self, row_num, data):
        '''(Table, int, str) -> NoneType
        Adds a row to the table. Done by adding each element of the row into
        its respective columns.
        TODO: Finish function
        '''
        pass

    def delete_row(self, row_index):
        '''(Table, int) -> NoneType
        Deletes a row from the table, given the row number (header doesn't
        count). Gets every header and the respective column, then deletes the
        item at the index given from each and every column.
        '''
        header_list = self.get_headers()
        for header in header_list:
            self.delete_item(header, row_num)

    def set_item(self, column_name, row_index, item):
        '''(Table, str, int, str) -> NoneType
        Sets a value (overwriting if a value is already set in that location)
        given the column and row for the respective table.
        TODO: Finish functions
        '''
        # what if the row doesn't exist
        # what if an item is already/not there?
        pass

    def set_item(self, column_name, item):
        '''(Table, str, str) -> NoneType
        Adds a value to the end of a given column of a table.
        '''
        self._data[column_name].append(item)

    def get_item(self, column_name, row_index):
        '''(Table, str, int) -> str
        Returns the string at a given column and row of a table.
        '''
        return self._data[column_name][row_index]

    def delete_item(self, column_name, row_index):
        '''(Table, str, int) -> NoneType
        Deletes an item from the table, given the row number and column of the
        table.
        '''
        del self._data[column_name][row_index]

    def num_rows(self):
        '''(Table) -> int
        Returns the number of rows in the table
        TODO: Add exceptions, comments
        TODO: Need to deal with entire uneven rows issue that may be created by
        set/delete item functions
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

    def print_table(self):
        '''(Table) -> NoneType
        Print a representation of table in a more visually clean table format.
        '''
        table_data_dictionary = self._data
        # This is where all the newly formatted lines of the table are going to
        # be stored, later every string in this list will be printed
        str_lines = []

        # Largest str length in a column
        largest_str = 0
        # Get columns and sort them so they can be printed in order
        non_sorted_columns = list(table_data_dictionary.keys())
        columns = self.header_preference_sorter(non_sorted_columns)

        # If it isn't empty, find the length of a column
        # This is so the list can be popluated with an equal amount of strings
        # to match the amount of rows to be concatenated into those strings
        if columns:
            length = len(table_data_dictionary[columns[0]])
            # Add an empty string for each row + a row for column headers
            for row in range(length + 1):
                str_lines.append("")

        # For every column
        for column in columns:
            # Looking for largest string to column, so that an appropriate
            # amount of spaces can be added to the rest of the strings such
            # that all the strings are the same length and the next column can
            # be aligned
            # Read the column first
            word = column
            # The largest string will automatically be the length of the
            # column name, as the length of the string will be zero or larger
            largest_str = len(word)
            # Then go through every row in column
            for row in range(self.num_rows()):
                # If larger
                word = table_data_dictionary[column][row]
                if len(word) > largest_str:
                    # Record length
                    largest_str = len(word)

            # The length of the largest one + 1 is where the next column starts
            # This is to add a buffer space for clarity
            # Add the item, then add the difference between the largest length
            # and the length of the added item
            # This is done in spaces to the end of the string

            # Add the word to the string representation in that row
            # Find the word, then add the word, then add the spaces
            # First done with columns and then every word in the row
            str_lines[0] += column
            str_lines[0] += (largest_str - len(column) + 1) * " "
            for row in range(0, self.num_rows()):
                word = table_data_dictionary[column][row]
                str_lines[row + 1] += word
                str_lines[row + 1] += (largest_str - len(word) + 1) * " "
            # Reset the largest string length for the next column
            largest_str = 0
        # When done, print every line in the newly formatted table
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
        # Go through every header in preference list in order
        for header in self._header_preferences:
            # If the given list contains the header in preference list
            if header in input_headers:
                # Add it next in priority and remove from original list
                sorted_list.append(header)
                input_headers.remove(header)
        # Add the rest of the unadded headers back, order doesn't matter
        # because they weren't given a preference
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
