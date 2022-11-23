"""The Graphical User Interface"""
import customtkinter as ctk

# pylint: disable=R0901

class view(ctk.CTkFrame):
    """
    A class to represent a view.

    ...

    Attributes
    ----------
    parent : str
        first name of the person

    Methods
    -------
    set_controller(controller):
        Assigns the controller to self.
    """
    def __init__(self, parent):
        """Test Code for TKinter Project"""
        super().__init__(parent)

        # label
        self.label = ctk.CTkLabel(self, text='ARs:')
        self.label.grid(row=0, column=0)


        # set the controller
        self.controller = None

    # def set_controller(self, controller):
    #     """
    #     Set the controller
    #     :param controller:
    #     :return:
    #     """
    #     self.controller = controller

    # def save_button_clicked(self):
    #     """
    #     Handle button click event
    #     :return:
    #     """
    #     if self.controller:
    #         self.controller.save(self.email_var.get())

    # def show_error(self, message):
    #     """
    #     Show an error message
    #     :param message:
    #     :return:
    #     """
    #     self.message_label['text'] = message
    #     self.message_label['foreground'] = 'red'
    #     self.message_label.after(3000, self.hide_message)
    #     self.email_entry['foreground'] = 'red'

    # def show_success(self, message):
    #     """
    #     Show a success message
    #     :param message:
    #     :return:
    #     """
    #     self.message_label['text'] = message
    #     self.message_label['foreground'] = 'green'
    #     self.message_label.after(3000, self.hide_message)

    #     # reset the form
    #     self.email_entry['foreground'] = 'black'
    #     self.email_var.set('')

    # def hide_message(self):
    #     """
    #     Hide the message
    #     :return:
    #     """
    #     self.message_label['text'] = ''
