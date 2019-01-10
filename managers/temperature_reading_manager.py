import datetime
from managers.abstract_reading_manager import AbstractReadingManager
from readings.temperature_reading import TemperatureReading

class TemperatureReadingManager(AbstractReadingManager):
    """ Concrete Implementation of Temperature reading manager """

    def __init__(self, filename):
        self.reading_type = TemperatureReading
        super().__init__(filename)
