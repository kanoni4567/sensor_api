import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class AbstractReadingManager:
    """ Reading manager """



    def __init__(self,filename):
        """ Initializes manager """
        if filename == '':
            raise ValueError("Database must be specified")
        engine = create_engine(filename)
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()

    def add_reading(self,reading):
        """ Adds a reading """
        if reading is not None:
            all_readings = self.get_all_readings()
            if len(all_readings) >= 1:
                last_seq_num = all_readings[-1].get_sequence_num()
                if reading.get_sequence_num() <= last_seq_num:
                    reading.set_sequence_num(last_seq_num + 1)
            # print(reading.get_sequence_num())
            self.session.add(reading)
            self.session.commit()
            return reading
        else:
            raise ValueError("Reading cannot be undefined.")

    def update_reading(self,reading):
        """ Updates a reading, returns none if same seq_num is not found """
        if reading is not None:
            id = reading.get_sequence_num()
            found_reading = self.get_reading(id)
            if found_reading is not None:
                self.delete_reading(id)
                self.session.add(reading)
                self.session.commit()
                return reading
        else:
            raise ValueError("Reading cannot be undefined.")

    def delete_reading(self,seq_num):
        """ Deletes a reading """
        deleted_reading = None
        found_reading = self.get_reading(seq_num)
        if found_reading is None:
            return False
        else:
            deleted_reading = found_reading
            self.session.delete(found_reading)
            self.session.commit()
        return deleted_reading

    def get_reading(self,seq_num):
        """ Abstract - Returns a reading based on sequence number """
        found_reading = self.session.query(self.reading_type).filter(self.reading_type.id == seq_num).first()
        if found_reading is not None:
            return found_reading
        else:
            return None

    def get_all_readings(self):
        """ Abstract - Returns all readings """
        all_readings = self.session.query(self.reading_type).all()
        return all_readings

