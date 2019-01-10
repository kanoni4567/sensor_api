import tkinter as tk
from tkinter import messagebox as tkMessageBox
from input_popup import InputPopup

class BottomNavbarView(tk.Frame):
    """ Navigation Bar """

    def __init__(self, parent, controller):
        """ Initialize the nav bar """
        tk.Frame.__init__(self, parent)
        self._parent = parent

        self._controller = controller
        self._create_widgets()

    def _create_widgets(self):
        """ Create widgets for bottom navbar """
        tk.Button(self,
                  text="Add",
                  height=1, width=10,
                  command=self._add).grid(row=2, column=0, padx=5, pady=5)

        tk.Button(self,
                  text="Update",
                  height=1, width=10,
                  command=self._update).grid(row=2, column=1, padx=5, pady=5)

        tk.Button(self,
                  text="Delete",
                  height=1, width=10,
                  command=self._delete).grid(row=2, column=2, padx=5, pady=5)
        tk.Button(self,text="QUIT",fg="red",height=1, width=10,
                  command=self._controller.quit).grid(row=2, column=3, padx=5, pady=5)

    def _add(self):
        """ Set action to add, initialize pop up """
        self._controller.app_state["action"] = "add"
        self._input_popup()

    def _update(self):
        """ Set action to update, initialize pop up """
        self._controller.app_state["action"] = "update"
        self._controller.confirm_selection()
        self._input_popup()

    def _delete(self):
        """ Set action to delete, prompt confirmation """
        self._controller.app_state["action"] = "delete"
        self._controller.confirm_selection()
        if tkMessageBox.askyesno('Verify', 'Really delete?'):
            self._controller.submit()

    def _input_popup(self):
        """ Initializes pop up for input """
        self._popup_win = tk.Toplevel()
        if self._controller.app_state["action"] == 'add':
            self._popup_win.title('Add')
        elif self._controller.app_state["action"] == 'update':
            self._popup_win.title('Update')
        self._popup = InputPopup(self._popup_win, self._controller)