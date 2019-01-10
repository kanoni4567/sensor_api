from readings.abstract_reading import AbstractReading


class PressureReading(AbstractReading):
    """ Concrete Implementation of a Pressure Reading """

    # CONSTANTS
    __tablename__ = "pressure_reading"
    HIGH_PRESS_ERROR = "HIGH_PRESSURE"
    LOW_PRESS_ERROR = "LOW_PRESSURE"
    STATUS_GOOD = "GOOD"



    def is_error(self):
        """ Returns True if there's a there's an error and False if there's no error """
        if self.status != self.STATUS_GOOD:
            return True

        return False

    def get_error_msg(self):
        """ Returns the error message (or None if not an error) """
        status_display = None

        reading_display_datetime = self.timestamp.strftime('%Y/%m/%d %H:%M')

        reading_seq_num = self.id

        if self.status == self.HIGH_PRESS_ERROR:
            status_display = "High Pressure (100 kPA) at %s, Sequence: %d" % (reading_display_datetime, reading_seq_num)
        elif self.status == self.LOW_PRESS_ERROR:
            status_display = "Low Pressure (0 kPA) at %s, Sequence: %d" % (reading_display_datetime, reading_seq_num)

        return status_display

    def to_json(self):
        """ Returns content of self in json format """
        result = {
            "timestamp": self.get_timestamp().strftime("%Y-%m-%d %H:%M"),
            "sequence_number": self.get_sequence_num(),
            "sensor_model": self.get_sensor_model(),
            "min_value": self.get_min_value(),
            "avg_value": self.get_avg_value(),
            "max_value": self.get_max_value(),
            "status": self.get_status()
        }
        return result
