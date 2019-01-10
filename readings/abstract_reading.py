import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship
from base import Base


class AbstractReading(Base):
    """ Temperature Sensor Reading """
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.datetime.now, nullable=False)
    model = Column(String(250), nullable=False)
    min_reading = Column(Float(3), nullable=False)
    avg_reading = Column(Float(3), nullable=False)
    max_reading = Column(Float(3), nullable=False)
    status = Column(String(250), nullable=False)

    def __init__(self, timestamp , model, min_reading, avg_reading, max_reading, status):
        """ Initializes the sensor reading """
        self.id = 1
        self.timestamp = timestamp
        self.model = model
        self.min_reading = min_reading
        self.avg_reading = avg_reading
        self.max_reading = max_reading
        self.status = status

    def get_timestamp(self):
        """ Getter for timestamp """
        return self.timestamp

    def get_sensor_model(self):
        """ Getter for sensor model """
        return self.model

    def get_sequence_num(self):
        """ Getter for sequence number """
        return self.id

    def set_sequence_num(self,num):
        """ Setter for sequence number"""
        self.id = num

    def get_min_value(self):
        """ Getter for the minimum temperature """
        return self.min_reading

    def get_avg_value(self):
        """ Getter for the average temperature """
        return self.avg_reading

    def get_max_value(self):
        """ Getter for the maximum temperature """
        return self.max_reading

    def get_status(self):
        """ Getter for reading status """
        return self.status

    def get_range(self):
        """ Getter for the temperature range """
        return self.max_reading - self.min_reading

    def to_json(self):
        """ Abstract Method - Returns content of self in json format """
        raise NotImplementedError("Must be implemented")

    def is_error(self):
        """ Abstract Method - Is Reading and Error """
        raise NotImplementedError("Must be implemented")

    def get_error_msg(self):
        """ Abstract Method - Get Error Readings """
        raise NotImplementedError("Must be implemented")

