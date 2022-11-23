"""Database Functions"""
import re

class model:
    """Model saves data into Excel"""
    def __init__(self, data):
        self.data = data

    @property
    def data(self):
        """Test Code for TKinter Project"""
        return self.__data

    @data.setter
    def data(self, value):
        """
        Validate the data
        :param value:
        :return:
        """
        # pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        # if re.fullmatch(pattern, value):
        self.__data = value
        # else:
        #     raise ValueError(f'Invalid data: {value}')

    def save(self):
        """
        Save the data into a file
        :return:
        """
        with open('data.txt', 'a') as file:
            file.write(self.data + '\n')
