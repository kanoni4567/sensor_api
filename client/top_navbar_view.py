import tkinter as tk


class TopNavbarView(tk.Frame):
    """ Navigation Bar """

    TEMP = 'temperature'
    PRES = 'pressure'

    def __init__(self, parent, controller):
        """ Initialize the nav bar """
        tk.Frame.__init__(self, parent)
        self._parent = parent
        self._controller = controller
        self._page = tk.IntVar()
        self._create_widgets()

    def _create_widgets(self):
        """ Creates the widgets for the nav bar """
        tk.Label(self,
                 text="Sensor Type:").grid(row=0, column=0)

        tk.Radiobutton(self,
                       text="Temperature",
                       variable=self._page,
                       value=1,
                       command=self._page_switch).grid(row=0, column=1)

        tk.Radiobutton(self,
                       text="Pressure",
                       variable=self._page,
                       value=2,
                       command=self._page_switch).grid(row=0, column=2)
        self._page.set(1)

    def _page_switch(self):
        """ Handle Switching Between Pages """

        if (self._controller.app_state["sensor"] == TopNavbarView.TEMP):
            self._controller.app_state["sensor"] = TopNavbarView.PRES
            self._controller.refresh()

        elif (self._controller.app_state["sensor"] == TopNavbarView.PRES):
            self._controller.app_state["sensor"] = TopNavbarView.TEMP
            self._controller.refresh()
