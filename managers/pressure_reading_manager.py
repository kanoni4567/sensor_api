import datetime
from managers.abstract_reading_manager import AbstractReadingManager
from readings.pressure_reading import PressureReading

class PressureReadingManager(AbstractReadingManager):
    """ Concrete Implementation of Pressure reading manager """

    def __init__(self, filename):
        self.reading_type = PressureReading
        super().__init__(filename)
