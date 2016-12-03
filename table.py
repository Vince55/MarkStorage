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

    def get_item(self, column_name, row_index):
        '''
        '''
        return self._data[column_name][row_index]

    def delete_item(self, column_name, row_index):
        '''
        '''
        del self._data[column_name][row_index]


class Database():
    ''' A class to represent a database'''

    def __init__():
        '''
        '''
        self._data = {}

    def add_table(self, table_name, table):
        '''
        '''
        self._data[table_name] = table

    def get_table(self, table_name):
        '''
        '''
