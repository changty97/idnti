"""The Graphical User Interface"""
import customtkinter as ctk
from .editablelistbox import editablelistbox

# import tkinter as tk

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

        # set the controller
        self.controller = None

        # Frame for AR navbar
        self.ar_navbar_frame = ctk.CTkFrame(
            master=parent,
            width=200,
            height=20,
            corner_radius=5,
            border_color="default_theme",
        )
        self.ar_navbar_frame.grid(
            row=0, column=0, columnspan=2, padx=20, pady=(10, 0), sticky="nsew"
        )

        # List box for AR(s)
        self.listbox = editablelistbox(self.ar_navbar_frame)

        self.listbox.grid(
            row=1, column=0, columnspan=2, padx=20, pady=(10, 0), sticky="nsew"
        )

        self.task_list = [
            "Eat apple",
            "drink water",
            "go gym",
            "write software",
            "write documentation",
            "take a nap",
            "Learn something",
            "paint canvas",
        ]

        for item in self.task_list:
            self.listbox.insert("end", item)

        # AR(s) label
        self.ar_label = ctk.CTkLabel(self.ar_navbar_frame, text="Action Required:")
        self.ar_label.grid(row=0, column=0, padx=5, pady=5, sticky="nw")

        # Check box for all AR(s)

        # Add button
        self.add_button = ctk.CTkButton(
            master=self.ar_navbar_frame,
            command=self.add_button_callback,
            fg_color="green",
            hover_color="dark green",
            text="Add",
        )
        self.add_button.grid(row=0, column=2, padx=5, pady=5, sticky="nw")

        # Done button
        self.add_button = ctk.CTkButton(
            master=self.ar_navbar_frame, command=self.add_button_callback, text="Done"
        )
        self.add_button.grid(row=0, column=4, padx=5, pady=5, sticky="nw")

        # Remove button
        self.add_button = ctk.CTkButton(
            master=self.ar_navbar_frame,
            command=self.listbox.remove_button_callback,
            fg_color="red",
            hover_color="dark red",
            text="Remove",
        )
        self.add_button.grid(row=0, column=5, padx=5, pady=5, sticky="nw")

        # Drop Down for AR(s)
        self.optionmenu_var = ctk.StringVar(value="3")  # set initial value

        self.combobox = ctk.CTkComboBox(
            master=self.ar_navbar_frame,
            values=["5", "10", "20"],
            command=self.optionmenu_callback,
            variable=self.optionmenu_var,
        )

        self.combobox.grid(row=0, column=1, padx=5, pady=5, sticky="nw")

        # Frame for Notes navbar
        self.notes_navbar_frame = ctk.CTkFrame(
            master=parent,
            # width=200,
            # height=20,
            corner_radius=5,
        )
        self.notes_navbar_frame.grid(
            row=2, column=0, columnspan=2, padx=20, pady=(10, 0), sticky="nsew"
        )

        # label
        self.notes_label = ctk.CTkLabel(self.notes_navbar_frame, text="Notes:")
        self.notes_label.grid(row=2, column=0, padx=5, pady=5, sticky="nw")

        # Create Notes Box
        self.notes = ctk.CTkTextbox(
            self.notes_navbar_frame, width=200, height=650, corner_radius=5
        )
        self.notes.grid(
            row=3,
            column=0,
            # columnspan=5,
            padx=5,
            pady=(5, 5),
            sticky="nsew",
        )
        # self.notes.configure(state="enable")

    def add_button_callback(self):
        """Button is Clicked"""
        self.listbox.insert(0, "")
        self.listbox.start_edit(0)
        print("Adding AR")

    def optionmenu_callback(self, choice):
        """Dropdown menu is selected"""
        print("optionmenu dropdown clicked:", choice)

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

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
