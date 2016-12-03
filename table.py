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

    def set_row(self, row_num, data):
        '''(Table, int, str) -> NoneType
        Adds a row to the table. Done by adding each element of the row into
        its respective columns.
        '''

    def delete_row(self, row_num):
        '''
        '''

    def set_item(self, row_index, column_name, item):
        '''
        '''

    def get_item(self, row_index, column_name):
        '''
        '''


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
