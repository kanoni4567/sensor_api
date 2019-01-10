import tkinter as tk


class ListView(tk.Frame):
    """ List of Readings """

    def __init__(self, parent, controller):
        """ Initialize Page 1 """
        tk.Frame.__init__(self, parent)
        self._parent = parent
        self._controller = controller
        self._create_widgets()

    def _create_widgets(self):
        """ Creates the widgets for Reading List """
        tk.Label(self,text="Readings").grid(row=0,column=1)
        self._xscrollbar = tk.Scrollbar(self, orient=tk.HORIZONTAL)
        self._yscrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)

        self._xscrollbar.grid(row=2,columnspan=3, sticky=tk.E + tk.W)
        self._yscrollbar.grid(row=1, column=5, sticky=tk.N + tk.S)

        self._listbox = tk.Listbox(self, width=70, xscrollcommand=self._xscrollbar.set, yscrollcommand=self._yscrollbar.set)
        self._listbox.grid(row=1, columnspan=3)

        self._xscrollbar["command"] = self._listbox.xview


    def selected_index(self):
        """ Returns index of current selected reading """
        return self._listbox.index(tk.ACTIVE)

    def load_readings(self):
        """ Load readings and show in list """
        self._listbox.delete(0, tk.END)
        for reading in self._controller.app_state["readings"]:
            self._listbox.insert(tk.END, '%d %.23s %s %.3f %.3f %.3f %s' % (reading["sequence_number"],reading["timestamp"],reading["sensor_model"],reading["min_value"],reading["avg_value"],reading["max_value"],reading["status"]))