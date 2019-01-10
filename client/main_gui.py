import tkinter as tk
from top_navbar_view import TopNavbarView
from bottom_navbar_view import BottomNavbarView
from list_view import ListView
import requests


class MainAppController(tk.Frame):
    """ Main Application for GUI """

    def __init__(self, parent):
        """ Initialize Main Application """
        tk.Frame.__init__(self, parent)
        self.app_state = {
            "sensor": TopNavbarView.TEMP,
            "action": '',
            "selected_reading": 0,
            "payload": {},
            "readings": []
        }
        self._top_navbar = TopNavbarView(self,self)
        self._top_navbar.grid(row=0)

        self._readings_list = ListView(self,self)
        self._readings_list.grid(row=1)

        self._bottom_navbar = BottomNavbarView(self,self)
        self._bottom_navbar.grid(row=2)

        self.refresh()

    def refresh(self):
        """ Reload data to show state change """
        self._get_all_readings()
        self._readings_list.load_readings()

    def confirm_selection(self):
        """ Confirm selected reading """
        selected_index = self._readings_list.selected_index()
        selected_reading = self.app_state["readings"][selected_index]
        self.app_state["selected_reading"] = dict(selected_reading)
        return self.app_state["selected_reading"]

    def submit(self):
        """ Send out http request """
        if self.app_state["action"] == "delete":
            seq = self.app_state["selected_reading"]["sequence_number"]
            response = requests.delete(f'http://127.0.0.1:5000/sensor/{self.app_state["sensor"]}/reading/{seq}')
            if response.status_code == 400:
                self._alert_bad_data()
        elif self.app_state["action"] == "add":
            message = self.app_state["payload"]
            headers = {"content-type": "application/json"}
            response = requests.post(f'http://127.0.0.1:5000/sensor/{self.app_state["sensor"]}/reading',json=message,headers=headers)
            if response.status_code == 400:
                self._alert_bad_data()

        elif self.app_state["action"] == "update":
            message = self.app_state["payload"]
            headers = {"content-type": "application/json"}
            seq = self.app_state["selected_reading"]["sequence_number"]
            response = requests.put(f'http://127.0.0.1:5000/sensor/{self.app_state["sensor"]}/reading/{seq}',json=message,headers=headers)
            if response.status_code == 400:
                self._alert_bad_data()
        self.refresh()

    def _get_all_readings(self):
        """ Get All readings depending on sensor type """
        response = None
        if self.app_state["sensor"] == TopNavbarView.TEMP:
            response = requests.get("http://127.0.0.1:5000/sensor/temperature/reading/all")
        elif self.app_state["sensor"] == TopNavbarView.PRES:
            response = requests.get("http://127.0.0.1:5000/sensor/pressure/reading/all")
        readings = response.json()
        self.app_state["readings"] = readings

    def _alert_bad_data(self):
        """ Alert user when data is in incorrect format """
        tk.messagebox.showerror("Error", "Data format is incorrect!")

if __name__ == "__main__":
    root = tk.Tk()
    root.title('Readings Manager')
    MainAppController(root).pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.mainloop()
