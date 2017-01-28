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

    def set_column(self, column_name, data):
        '''(Table, str, str) -> Nonetype
        Adds a column to the table. Done by adding a header-key pair to the
        table.
        '''
        self._data[column_name] = data

    def delete_column(self, column_name):
        '''
        '''
        del self._data[column_name]

    def get_headers(self):
        '''
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
        '''
        '''
        header_list = self.get_headers
        for header in header_list:
            self.delete_item(header, row_num)

    def set_item(self, column_name, row_index, item):
        '''
        '''
        # what if the row doesn't exist
        # what if an item is already/not there?
        pass

    def set_item(self, column_name, item):
        '''
        '''
        # what if the row doesn't exist
        # what if an item is already/not there?
        self._data[column_name].append(item)

    def get_item(self, column_name, row_index):
        '''
        '''
        return self._data[column_name][row_index]

    def delete_item(self, column_name, row_index):
        '''
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


class Database():
    ''' A class to represent a database'''

    def __init__(self):
        '''
        '''
        self._data = {}

    def add_table(self, table_name, table):
        '''
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
        '''
        '''
        return self._data.keys()
