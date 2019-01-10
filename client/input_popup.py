import tkinter as tk

class InputPopup(tk.Frame):

    def __init__(self, parent, controller):
        """ Initializes input popup """
        tk.Frame.__init__(self, parent, width=100, height=300)
        self._parent = parent
        self._controller = controller
        self.grid(rowspan=3, columnspan=3)
        self._create_widgets()

    def _create_widgets(self):
        """ Create widgets for pop up input """
        tk.Label(self, text="Model").grid(row=0)
        tk.Label(self, text="Min Value").grid(row=1)
        tk.Label(self, text="Avg Value").grid(row=2)
        tk.Label(self, text="Max Value").grid(row=3)
        tk.Label(self, text="Time").grid(row=4)
        tk.Label(self, text="Status").grid(row=5)

        self.model_entry = tk.Entry(self,width=30)
        self.model_entry.grid(row=0, column=1)
        self.min_entry = tk.Entry(self,width=30)
        self.min_entry.grid(row=1, column=1)
        self.avg_entry = tk.Entry(self,width=30)
        self.avg_entry.grid(row=2, column=1)
        self.max_entry = tk.Entry(self,width=30)
        self.max_entry.grid(row=3, column=1)
        self.time_entry = tk.Entry(self,width=30)
        self.time_entry.grid(row=4, column=1)
        self.status_entry = tk.Entry(self,width=30)
        self.status_entry.grid(row=5, column=1)

        self._confirm_button = tk.Button(self, height=1, width=10)
        self._confirm_button["text"] = "OK"
        self._confirm_button["command"] = self._confirm
        self._confirm_button.grid(row=6, column=1)

        if self._controller.app_state["action"] == "update":
            self.model_entry.insert(0,self._controller.app_state["selected_reading"]["sensor_model"])
            self.min_entry.insert(0,self._controller.app_state["selected_reading"]["min_value"])
            self.avg_entry.insert(0,self._controller.app_state["selected_reading"]["avg_value"])
            self.max_entry.insert(0,self._controller.app_state["selected_reading"]["max_value"])
            self.time_entry.insert(0,self._controller.app_state["selected_reading"]["timestamp"])
            self.status_entry.insert(0,self._controller.app_state["selected_reading"]["status"])

    def _confirm(self):
        """ Confirm Input """
        input_dict = {
            "timestamp": self.time_entry.get(),
            "sensor_model": self.model_entry.get(),
            "min_value": self.min_entry.get(),
            "avg_value": self.avg_entry.get(),
            "max_value": self.max_entry.get(),
            "status": self.status_entry.get()
        }
        self._controller.app_state["payload"] = input_dict
        self._controller.submit()
        self._controller.refresh()
        self._parent.destroy()
