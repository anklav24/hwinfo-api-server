"""For low level discovery in Zabbix"""
import flask

from api import app
from api.json_handler import get_lld_sensors


def filter_str_sensors(filter_args: str, sensor_key: str, sensors: list):
    """Filter LLD JSON with data like hardware names."""
    filter_args = filter_args.lower().strip().replace(' ', '')
    filtered_sensors = []

    if filter_args:
        for argument in filter_args.split(','):
            for sensor in sensors:
                if argument[0:4] == 'not_':

                    if argument[4:] in sensor[sensor_key].lower():
                        continue
                    else:
                        filtered_sensors.append(sensor)

                elif argument in sensor[sensor_key].lower():
                    filtered_sensors.append(sensor)

        return filtered_sensors
    return sensors


def filter_int_sensors(filter_args: str, sensor_key: str, sensors: list):
    """Filter LLD JSON with data like hardware names."""
    filter_args = filter_args.lower().strip().replace(' ', '')
    filter_args_one = []
    filter_args_range = []
    filtered_sensors = []

    if filter_args:
        for arg in filter_args.split(','):
            if '-' in arg:
                filter_args_range.append(arg)
            else:
                filter_args_one.append(arg)

        filter_args_one = [int(value) for value in filter_args_one]
        filter_args_range = [[int(value) for value in arg.split('-')] for arg in filter_args_range]

        for sensor in sensors:
            if sensor[sensor_key] in filter_args_one:
                filtered_sensors.append(sensor)

            for arg_range in filter_args_range:
                for sensor_index_arg in range(arg_range[0], arg_range[-1] + 1):
                    if sensor[sensor_key] == sensor_index_arg:
                        filtered_sensors.append(sensor)

        return filtered_sensors
    return sensors


@app.route("/hardware_lld", methods=['GET'])
def scan_hardware_lld():
    """Get json for LLD discovery
    hardware_name
    hardware_index
    sensor_name
    sensor_index
    sensor_type_name
    sensor_type_index
    unit"""

    hardware_name = flask.request.args.get('hardware_name', default='', type=str)
    hardware_index = flask.request.args.get('hardware_index', default='', type=str)
    sensor_name = flask.request.args.get('sensor_name', default='', type=str)
    sensor_index = flask.request.args.get('sensor_index', default='', type=str)
    sensor_type_name = flask.request.args.get('sensor_type_name', default='', type=str)
    sensor_type_index = flask.request.args.get('sensor_type_index', default='', type=str)
    unit = flask.request.args.get('unit', default='', type=str)

    sensors = get_lld_sensors()

    sensors = filter_str_sensors(hardware_name, '{#HARDWARENAME}', sensors)
    sensors = filter_str_sensors(sensor_name, '{#SENSORNAME}', sensors)
    sensors = filter_str_sensors(sensor_type_name, '{#SENSORTYPENAME}', sensors)
    sensors = filter_str_sensors(unit, '{#UNIT}', sensors)

    sensors = filter_int_sensors(hardware_index, '{#HARDWAREINDEX}', sensors)
    sensors = filter_int_sensors(sensor_index, '{#SENSORINDEX}', sensors)
    sensors = filter_int_sensors(sensor_type_index, '{#SENSORTYPEINDEX}', sensors)

    sensors_set = [dict(s) for s in set(tuple(sensor.items()) for sensor in sensors)]
    sensors_sorted = sorted(sensors_set, key=lambda key: (key['{#SENSORINDEX}']))

    return flask.jsonify(sensors_sorted)


@app.route("/value_lld/<sensor_index>")
def get_value_lld(sensor_index: str):
    # noinspection HttpUrlsUsage
    """Get value by sensor_index
    sensor_index: sensor number from range 0 till end
            Type: path parameter

    debug: show the context for a value
            Type: query
            Options: true, false
            Default: false

    Examples:
    http://127.0.0.1:50000/value_lld/189
    http://127.0.0.1:50000/value_lld/155?debug=true
    """
    sensor_index = int(sensor_index)
    debug = flask.request.args.get('debug', default="false", type=str)

    sensors = get_lld_sensors()

    if debug.lower() == "true":
        return flask.jsonify(sensors[sensor_index])

    return flask.jsonify(sensors[sensor_index]["{#VALUE}"])
