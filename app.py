"""File that runs main program"""
import customtkinter as ctk
from model import model
from view import view
from controller import controller
from view.action_required import action_required

class app(ctk.CTk):
    """Constructor that initialises the GUI"""
    def __init__(self):
        super().__init__()

        # Setting tkinter window size to fit Screen
        self.state('zoomed')

        # Set title of App
        self.title('iDNTI')

        # Set min size
        self.minsize(1000, 745)

        # create grid system
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        # Frame for AR navbar
        self.ar_navbar_frame = ctk.CTkFrame(master=self, width=200, height=20, corner_radius=5, border_color="default_theme")
        self.ar_navbar_frame.grid(row=0, column=0, columnspan=2, padx=20, pady=(10, 0), sticky="nsew")
        
        # label
        self.ar_label = ctk.CTkLabel(self.ar_navbar_frame, text='Action Requests:')
        self.ar_label.grid(row=0, column=0, padx=5, pady=5, sticky="nw")

        # Tab for Completed AR(s)
        self.completed_button = ctk.CTkButton(master=self.ar_navbar_frame, command=self.button_callback, text="Completed")
        self.completed_button.grid(row=0, column=1, padx=5, pady=5, sticky="nw")

        # Add button
        self.add_button = ctk.CTkButton(master=self.ar_navbar_frame, command=self.button_callback, text="Add")
        self.add_button.grid(row=0, column=2, padx=5, pady=5, sticky="nw")

        # Drop Down for AR(s)
        self.optionmenu_var = ctk.StringVar(value="3")  # set initial value
        self.combobox = ctk.CTkComboBox(master=self.ar_navbar_frame,
                                     values=["5", "10", "20"],
                                     command=self.optionmenu_callback,
                                     variable=self.optionmenu_var)
        self.combobox.grid(row=0, column=3, padx=5, pady=5, sticky="nw")

        # Frame for ARs
        self.ar_frame = ctk.CTkFrame(master=self, width=200, height=300, corner_radius=5)
        self.ar_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=(10, 10), sticky="nsew")

        # Frame for Notes navbar
        self.notes_navbar_frame = ctk.CTkFrame(master=self, width=200, height=20, corner_radius=5, border_color="default_theme")
        self.notes_navbar_frame.grid(row=2, column=0, columnspan=2, padx=20, pady=(10, 0), sticky="nsew")

        # label
        self.notes_label = ctk.CTkLabel(self.notes_navbar_frame, text='Notes:')
        self.notes_label.grid(row=2, column=0, padx=5, pady=5, sticky="nw")

        # Create Notes Box
        self.notes = ctk.CTkTextbox(self, width=200, height=650, corner_radius=5)
        self.notes.grid(row=3, column=0, columnspan=2, padx=20, pady=(10, 10), sticky="nsew")
        # self.notes.configure(state="enable")

        # create a model
        # self.model = model.model('hello@pythontutorial.net')

        # create a view and place it on the root window
        # self.view = view.view(self)
        # view.view.grid(row=0, column=0, padx=10, pady=10)

        # create a controller
        # con = controller.controller(self.model, self.view)

        # set the controller to view
        # view.view.set_controller(con)

    def button_callback(self):
        print("pressed")

    def optionmenu_callback(choice):
        print("optionmenu dropdown clicked:", choice)


if __name__ == '__main__':
    app = app()
    app.mainloop()
