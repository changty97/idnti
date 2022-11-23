"""Database Functions"""

# pylint: disable=W1514

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
        self.__data = value

    def save(self):
        """
        Save the data into a file
        :return:
        """
        with open('data.txt', 'a') as file:
            file.write(self.data + '\n')
