from readings.abstract_reading import AbstractReading


class TemperatureReading(AbstractReading):
    """ Concrete Implementation of a Temperature Reading """

    # CONSTANTS
    __tablename__ = "temperature_reading"
    HIGH_TEMP_ERROR = "HIGH_TEMP"
    LOW_TEMP_ERROR = "LOW_TEMP"
    STATUS_OK = "OK"
    DEGREE_SIGN = u'\N{DEGREE SIGN}'



    def is_error(self):
        """ Returns True if there's a there's an error and False if there's no error """
        if self.status != TemperatureReading.STATUS_OK:
            return True

        return False

    def get_error_msg(self):
        """ Returns the error message (or None if not an error) """
        status_display = None

        reading_display_datetime = self.timestamp.strftime('%Y/%m/%d %H:%M')

        reading_seq_num = self.id

        if self.status == TemperatureReading.HIGH_TEMP_ERROR:
            status_display = "High Temperature (100%cC) at %s, Sequence: %d" % (TemperatureReading.DEGREE_SIGN, reading_display_datetime, reading_seq_num)
        elif self.status == TemperatureReading.LOW_TEMP_ERROR:
            status_display = "Low Temperature (-50%cC) at %s, Sequence: %d" % (TemperatureReading.DEGREE_SIGN, reading_display_datetime, reading_seq_num)

        return status_display

    def to_json(self):
        """ Returns content of self in json format """
        result = {
            "timestamp": self.get_timestamp().strftime("%Y-%m-%d %H:%M:%S.%f"),
            "sequence_number": self.get_sequence_num(),
            "sensor_model": self.get_sensor_model(),
            "min_value": self.get_min_value(),
            "avg_value": self.get_avg_value(),
            "max_value": self.get_max_value(),
            "status": self.get_status()
        }
        return result
