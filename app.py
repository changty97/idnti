"""File that runs main program"""
import customtkinter as ctk

# import tkhtmlview
# from tkcalendar import DateEntry
# from model import model
from view.view import view

# from controller import controller

# pylint: disable=R0902


class app(ctk.CTk):
    """Constructor that initialises the GUI"""

    def __init__(self):
        super().__init__()

        # Setting tkinter window size to fit Screen
        self.state("zoomed")

        # Set title of App
        self.title("iDNTI")

        # Set min size
        self.minsize(1000, 745)

        # create grid system
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        self.view = view(self)


if __name__ == "__main__":
    app = app()
    app.mainloop()
