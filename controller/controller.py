"""API between view and model"""
from model import model
from view import view

class controller:
    """Class controller saves data"""
    def __init__(self, model, view):
        """Test Code for TKinter Project"""
        self.model = model
        self.view = view

    def save(self, data):
        """
        Save the data
        :param data:
        :return:
        """
        try:

            # save the model
            self.model.data = data
            self.model.save()

            # show a success message
            self.view.show_success(f'The data {data} saved!')

        except ValueError as error:
            # show an error message
            self.view.show_error(error)
