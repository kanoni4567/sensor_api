import json
import datetime
from flask import Flask, request
from managers.temperature_reading_manager import TemperatureReadingManager
from managers.pressure_reading_manager import PressureReadingManager
from readings.temperature_reading import TemperatureReading
from readings.pressure_reading import PressureReading

DB_FILE_NAME = "sqlite:///readings.sqlite?check_same_thread=False"

temp_manager = TemperatureReadingManager(DB_FILE_NAME)
pres_manager = PressureReadingManager(DB_FILE_NAME)

app = Flask(__name__)

@app.route('/sensor/<string:sensor_type>/reading', methods = ['POST'])
def add_reading(sensor_type):
    """ Adds a reading """

    if sensor_type == 'temperature':
        content = request.get_json()
        reading = construct_temp_reading(content)
        if reading is not None:
            added_reading = temp_manager.add_reading(reading)
            response = app.response_class(
                response=json.dumps(added_reading.to_json()),
                status=200,
                mimetype='application/json'
            )
        else:
            response = app.response_class(status=400)
    elif sensor_type == 'pressure':
        content = request.get_json()
        reading = construct_pres_reading(content)
        if reading is not None:
            added_reading = pres_manager.add_reading(reading)
            response = app.response_class(
                response=json.dumps(added_reading.to_json()),
                status=200,
                mimetype='application/json'
            )
        else:
            response = app.response_class(status=400)
    else:
        response = app.response_class(status=400)
    return response

@app.route('/sensor/<string:sensor_type>/reading/<int:seq_num>', methods = ['PUT'])
def update_reading(sensor_type, seq_num):
    """ Update a reading """

    if sensor_type == 'temperature':
        content = request.get_json()
        reading = construct_temp_reading(content)
        if reading is not None:
            reading.set_sequence_num(seq_num)
            updated_reading = temp_manager.update_reading(reading)
            if updated_reading is not None:
                response = app.response_class(
                    response=json.dumps(updated_reading.to_json()),
                    status=200,
                    mimetype='application/json'
                )
            else:
                response = app.response_class(status=400)
        else:
            response = app.response_class(status=400)
    elif sensor_type == 'pressure':
        content = request.get_json()
        reading = construct_pres_reading(content)
        if reading is not None:
            reading.set_sequence_num(seq_num)
            updated_reading = pres_manager.update_reading(reading)
            if update_reading is not None:
                response = app.response_class(
                    response=json.dumps(updated_reading.to_json()),
                    status=200,
                    mimetype='application/json'
                )
            else:
                response = app.response_class(status=400)
        else:
            response = app.response_class(status=400)
    else:
        response = app.response_class(status=400)
    return response

@app.route('/sensor/<string:sensor_type>/reading/<int:seq_num>', methods = ['DELETE'])
def delete_reading(sensor_type, seq_num):
    """ Deletes a reading """

    if sensor_type == 'temperature':
        deleted_reading = temp_manager.delete_reading(seq_num)
        if deleted_reading is not None:
            response = app.response_class(
                status=200,
                mimetype='application/json'
            )
        else:
            response = app.response_class(status=400)
    elif sensor_type == 'pressure':
        deleted_reading = pres_manager.delete_reading(seq_num)
        if deleted_reading is not None:
            response = app.response_class(
                status=200,
                mimetype='application/json'
            )
        else:
            response = app.response_class(status=400)
    else:
        response = app.response_class(status=400)
    return response

@app.route('/sensor/<string:sensor_type>/reading/<int:seq_num>', methods = ['GET'])
def get_reading(sensor_type, seq_num):
    """ Get a reading """

    if sensor_type == 'temperature':
        found_reading = temp_manager.get_reading(seq_num)
        if found_reading is not None:
            response = app.response_class(
                response=json.dumps(found_reading.to_json()),
                status=200,
                mimetype='application/json'
            )
        else:
            response = app.response_class(status=400)
    elif sensor_type == 'pressure':
        found_reading = pres_manager.get_reading(seq_num)
        if found_reading is not None:
            response = app.response_class(
                response=json.dumps(found_reading.to_json()),
                status=200,
                mimetype='application/json'
            )
        else:
            response = app.response_class(status=400)
    else:
        response = app.response_class(status=400)
    return response

@app.route('/sensor/<string:sensor_type>/reading/all', methods = ['GET'])
def get_all_reading(sensor_type):
    """ Get all readings """

    if sensor_type == 'temperature':
        found_readings = temp_manager.get_all_readings()
        if len(found_readings) >= 1:
            result_list_json = []
            for found_reading in found_readings:
                result_list_json.append(found_reading.to_json())
            response = app.response_class(
                response=json.dumps(result_list_json),
                status=200,
                mimetype='application/json'
            )
        else:
            response = app.response_class(status=400)
    elif sensor_type == 'pressure':
        found_readings = pres_manager.get_all_readings()
        if len(found_readings) >= 1:
            result_list_json = []
            for found_reading in found_readings:
                result_list_json.append(found_reading.to_json())
            response = app.response_class(
                response=json.dumps(result_list_json),
                status=200,
                mimetype='application/json'
            )
        else:
            response = app.response_class(status=400)
    else:
        response = app.response_class(status=400)
    return response

def construct_temp_reading(content):
    """ Construct a temperature reading object from json """
    try:
        date = datetime.datetime.strptime(content['timestamp'], "%Y-%m-%d %H:%M:%S.%f")
        sensor_name = content['sensor_model']
        lowest_value = content['min_value']
        avg_value = content['avg_value']
        highest_value = content['max_value']
        status = content['status']

        reading = TemperatureReading(date, sensor_name, lowest_value, avg_value, highest_value, status)
    except (KeyError, ValueError):
        reading = None
    return reading

def construct_pres_reading(content):
    """ Construct a pressure reading object from json """
    try:
        date = datetime.datetime.strptime(content['timestamp'], "%Y-%m-%d %H:%M")
        sensor_name = content['sensor_model']
        lowest_value = content['min_value']
        avg_value = content['avg_value']
        highest_value = content['max_value']
        status = content['status']

        reading = PressureReading(date, sensor_name, lowest_value, avg_value, highest_value, status)
    except (KeyError, ValueError):
        reading = None
    return reading

if __name__ == "__main__":
    app.run()