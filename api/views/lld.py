"""For low level discovery in Zabbix"""
import flask

from api import app
from api.json_handler import get_lld_sensors


def filter_str_sensors(filter_args: str, sensor_value: str, sensors: list):
    """Filter LLD JSON with data like hardware names."""
    filter_args = filter_args.lower().strip().replace(' ', '').split(',')
    filtered_sensors = []

    if filter_args:
        for argument in filter_args:
            for sensor in sensors:
                if argument[0:4] == 'not_':

                    if argument[4:] in sensor[sensor_value].lower():
                        continue
                    else:
                        filtered_sensors.append(sensor)

                elif argument in sensor[sensor_value].lower():
                    filtered_sensors.append(sensor)

        return filtered_sensors
    return sensors


def filter_int_sensors(filter_args: str, sensor_key: str, sensors: list):
    """Filter LLD JSON with data like hardware names."""
    filter_args = str(filter_args).lower().strip().replace(' ', '')
    filtered_sensors = []

    if filter_args:
        filter_args = [int(value) for value in filter_args.split(',')]

        for sensor in sensors:
            if sensor[sensor_key] in filter_args:
                filtered_sensors.append(sensors)
        return filtered_sensors

    return sensors


@app.route("/hardware_lld", methods=['GET'])
def scan_hardware_lld():
    """Get json for LLD discovery
    hardware_name =
    hardware_index =
    sensor_name =
    sensor_type_name =
    sensor_index =
    unit = """

    hardware_name = flask.request.args.get('hardware_name', default='', type=str)
    hardware_index = flask.request.args.get('hardware_index', default='', type=str)
    sensor_name = flask.request.args.get('sensor_name', default='', type=str)
    sensor_type_name = flask.request.args.get('sensor_type_name', default='', type=str)
    sensor_index = flask.request.args.get('sensor_index', default='', type=str)
    unit = flask.request.args.get('unit', default='', type=str)

    sensors = get_lld_sensors()

    sensors = filter_str_sensors(hardware_name, '{#HARDWARENAME}', sensors)
    sensors = filter_str_sensors(sensor_name, '{#SENSORNAME}', sensors)
    sensors = filter_str_sensors(sensor_type_name, '{#SENSORTYPENAME}', sensors)
    sensors = filter_str_sensors(unit, '{#UNIT}', sensors)

    sensors = filter_int_sensors(hardware_index, '{#HARDWAREINDEX}', sensors)
    sensors = filter_int_sensors(sensor_index, '{#SENSORINDEX}', sensors)

    filtered_sensors = []
    if unit:
        for sensor in sensors:
            if sensor['{#UNIT}'].lower() == unit.lower():
                filtered_sensors.append(sensor)
            sensors = filtered_sensors

    filtered_sensors = []
    if sensor_index:
        for sensor in sensors:
            if sensor['{#HARDWAREINDEX}'] == sensor_index:
                filtered_sensors.append(sensor)
            sensors = filtered_sensors

    return flask.jsonify(sensors)


@app.route("/value_lld/<int:reading_index>")
def get_value_lld(reading_index):
    sensors = get_lld_sensors()
    debug = flask.request.args.get('debug', default="false", type=str)

    if debug.lower() == "true":
        for sensor in sensors:
            if sensor["{#SENSORINDEX}"] == reading_index:
                return flask.jsonify(sensors[reading_index])

    for sensor in sensors:
        if sensor["{#SENSORINDEX}"] == reading_index:
            return flask.jsonify(sensor["{#VALUE}"])
