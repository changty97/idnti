"""A listbox where you can directly edit an item via double-click"""
import tkinter as tk

# import customtkinter as ctk


class editablelistbox(tk.Listbox):
    """A listbox where you can directly edit an item via double-click"""

    def __init__(self, master, **kwargs):
        """A listbox where you can directly edit an item via double-click"""
        super().__init__(master, **kwargs)
        self.edit_item = None
        self.bind("<Double-1>", self._start_edit)
        self.bind("<<ListboxSelect>>", self.get_selected_index)

    def _start_edit(self, event):
        """A listbox where you can directly edit an item via double-click"""
        index = self.index(f"@{event.x},{event.y}")
        self.start_edit(index)
        return "break"

    def start_edit(self, index):
        """A listbox where you can directly edit an item via double-click"""
        self.edit_item = index
        text = self.get(index)
        y_first_index = self.bbox(index)[1]
        entry = tk.Entry(self, borderwidth=0, highlightthickness=1)
        entry.bind("<Return>", self.accept_edit)
        entry.bind("<Escape>", self.cancel_edit)

        entry.insert(0, text)
        entry.selection_from(0)
        entry.selection_to("end")
        entry.place(relx=0, y=y_first_index, relwidth=1, width=-1)
        entry.focus_set()
        entry.grab_set()

    def cancel_edit(self, event):
        """A listbox where you can directly edit an item via double-click"""
        event.widget.destroy()

    def accept_edit(self, event):
        """A listbox where you can directly edit an item via double-click"""
        new_data = event.widget.get()
        self.delete(self.edit_item)
        self.insert(self.edit_item, new_data)
        event.widget.destroy()

    def get_selected_index(self):
        """Returns the index of the selected editable list box"""
        index = self.curselection()
        for i in index:
            return i

    def remove_button_callback(self):
        """Button is Clicked"""
        self.delete(self.get_selected_index(), "active")
