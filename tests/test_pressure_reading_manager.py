from managers.pressure_reading_manager import PressureReadingManager
from readings.pressure_reading import PressureReading
from unittest import TestCase
import inspect
import datetime
import sqlite3
import os

class TestPressureReadingManager(TestCase):
    """ Unit tests for pressure manager """
    TEST_DB = 'sqlite:///test_readings.sqlite'
    TEST_READING = PressureReading(datetime.datetime.strptime("2018-09-23 19:59", "%Y-%m-%d %H:%M"), "ABC Sensor Pres M100", 49.512, 51.841, 100.008, "GOOD")


    def setUp(self):
        """ Set up test environment """
        self.logPoint()
        conn = sqlite3.connect('test_readings.sqlite')
        c = conn.cursor()
        c.execute('''
                  CREATE TABLE temperature_reading
                  (id INTEGER PRIMARY KEY ASC,
                   timestamp DATETIME NOT NULL,
                   model VARCHAR(250) NOT NULL,
                   min_reading NUMBER NOT NULL,
                   avg_reading NUMBER NOT NULL,
                   max_reading NUMBER NOT NULL,
                   status VARCHAR(250) NOT NULL
                  )
                  ''')
        c.execute('''
                  CREATE TABLE pressure_reading
                  (id INTEGER PRIMARY KEY ASC,
                   timestamp DATETIME NOT NULL,
                   model VARCHAR(250) NOT NULL,
                   min_reading NUMBER NOT NULL,
                   avg_reading NUMBER NOT NULL,
                   max_reading NUMBER NOT NULL,
                   status VARCHAR(250) NOT NULL
                  )
                  ''')
        conn.commit()
        conn.close()
        self.test_manager = PressureReadingManager(TestPressureReadingManager.TEST_DB)
        self.test_manager.add_reading(PressureReading(datetime.datetime.strptime("2018-09-23 19:59", "%Y-%m-%d %H:%M"), "ABC Sensor Pres M100", 49.512, 51.841, 100.008, "GOOD"))

    def tearDown(self):
        """ call log message for test"""
        self.logPoint()
        self.test_manager.session.close()
        self.test_manager = None
        os.remove('test_readings.sqlite')


    def logPoint(self):
        """ Log out testing information """
        current_test = self.id().split('.')[-1]
        calling_function = inspect.stack()[1][3]
        print('in %s - %s()' % (current_test, calling_function))

    def test_initializer(self):
        """ Valid argument for initializer """
        test_manager = PressureReadingManager(TestPressureReadingManager.TEST_DB)
        self.assertIsNotNone(test_manager)

    def test_invalid_initializer(self):
        """ Invalid argument for initializer """
        with self.assertRaises(ValueError):
            PressureReadingManager('')

    def test_add_reading(self):
        """ Valid argument for add_reading """
        self.assertIsNotNone(self.test_manager.add_reading(PressureReading(datetime.datetime.strptime("2018-09-23 19:59", "%Y-%m-%d %H:%M"), "ABC Sensor Pres M100", 49.512, 51.841, 100.008, "GOOD")))

    def test_invalid_add_reading(self):
        """ Invalid argument for add_reading """
        with self.assertRaises(ValueError):
            self.test_manager.add_reading(None)

    def test_update_reading(self):
        """ Valid argument for update_reading """
        test_update_reading = PressureReading(datetime.datetime.strptime("2018-09-23 19:59", "%Y-%m-%d %H:%M"), "ABC Sensor Pres M100", 49.512, 51.841, 100.008, "GOOD")
        updated_reading = self.test_manager.update_reading(test_update_reading)
        self.assertIsNotNone(updated_reading)

    def test_invalid_update_reading(self):
        """ Invalid argument for update_reading """
        with self.assertRaises(ValueError):
            self.test_manager.update_reading(None)

    def test_delete_reading(self):
        """ Valid argument for delete_reading """
        self.assertIsNotNone(self.test_manager.delete_reading(1))

    def test_invalid_delete_reading(self):
        """ Invalid argument for delete_reading """
        self.assertFalse(self.test_manager.delete_reading(100))

    def test_get_reading(self):
        """ Valid argument for get_reading """
        self.assertIsNotNone(self.test_manager.get_reading(1))

    def test_invalid_get_reading(self):
        """ Invalid argument for get_reading """
        self.assertIsNone(self.test_manager.get_reading(100))

    def test_get_all_readings(self):
        """ Test for get_all_readings """
        self.assertIsNotNone(self.test_manager.get_all_readings())