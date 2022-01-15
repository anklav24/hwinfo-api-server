"""For low level discovery in Zabbix"""
import flask

from api import app
from api.json_handler import get_modified_json


def get_lld_sensors() -> list:
    """Preprocess JSON to LLD format. Make names more user-friendly"""
    json_data = get_modified_json()

    datalist = list()
    for hardware in json_data['sensors']:
        for reading in json_data['readings']:
            if reading['sensorIndex'] == hardware['sensorIndex']:
                datadict = {"{#HARDWARENAME}": hardware['sensorNameUser'],
                            "{#HARDWAREINDEX}": hardware['sensorIndex'],
                            "{#SENSORNAME}": reading['labelUser'],
                            "{#SENSORINDEX}": reading['readingIndex'],
                            "{#SENSORTYPENAME}": reading['readingTypeName'],
                            "{#SENSORTYPEINDEX}": reading['readingType'],
                            "{#VALUE}": reading['value'],
                            "{#UNIT}": reading['unit']}
                datalist.append(datadict)
    return datalist


def filter_str_sensors(filter_args: str, sensor_value: str, sensors: list):
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

        return list(map(dict, set(tuple(sorted(d.items())) for d in filtered_sensors)))
    return sensors


@app.route("/hardware_lld", methods=['GET'])
def scan_hardware_lld():
    """Get json for LLD discovery
    sensor_name_user =
    sensor_index =
    label_user =
    reading_type_name =
    reading_index =
    unit = """

    sensor_name_user = flask.request.args.get('sensor_name_user', default='', type=str)
    sensor_index = flask.request.args.get('sensor_index', default='', type=int)
    label_user = flask.request.args.get('label_user', default='', type=str)
    reading_type_name = flask.request.args.get('reading_type_name', default='', type=str)
    reading_index = flask.request.args.get('reading_index', default='', type=str)
    unit = flask.request.args.get('unit', default='', type=str)

    sensors = get_lld_sensors()

    sensors = filter_str_sensors(sensor_name_user, '{#HARDWARENAME}', sensors)
    sensors = filter_str_sensors(label_user, '{#SENSORNAME}', sensors)

    filtered_sensors = []
    if reading_index:
        for sensor in sensors:
            if str(sensor['{#SENSORINDEX}']) in reading_index.split(','):
                filtered_sensors.append(sensor)
            sensors = filtered_sensors

    filtered_sensors = []
    if reading_type_name:
        for sensor in sensors:
            if sensor['{#SENSORTYPENAME}'].lower() == reading_type_name.lower():
                filtered_sensors.append(sensor)
        sensors = filtered_sensors

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
