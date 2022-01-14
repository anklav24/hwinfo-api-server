#!/usr/bin/env/ python3
# coding=utf-8

import os
import subprocess

import flask
import requests

# Connection
REMOTE_HWINFO_IP = '127.0.0.1'  # Default: 127.0.0.1
REMOTE_HWINFO_PORT = 60005  # Default: 60005

FLASK_HOST = "0.0.0.0"  # Default: 0.0.0.0
FLASK_PORT = 50000  # Default: 50000

flask_app = flask.Flask(__name__)
flask_app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
flask_app.config["JSON_SORT_KEYS"] = False

# noinspection HttpUrlsUsage
REMOTE_HWINFO_URL = f'http://{REMOTE_HWINFO_IP}:{REMOTE_HWINFO_PORT}/json.json'


def run_processes():
    os.startfile('HWiNFO32.exe', show_cmd=False)
    os.startfile('remotehwinfo.exe',
                 arguments=f"-port {REMOTE_HWINFO_PORT} -log 0 -hwinfo 1 -gpuz 0 -afterburner 0",
                 show_cmd=False)
    subprocess.run('tasklist /fi "imagename eq HWiNFO32.exe"')
    subprocess.run('tasklist /fi "imagename eq remotehwinfo.exe"')
    print()


def kill_processes():
    os.system("taskkill /f /im remotehwinfo.exe")
    os.system("taskkill /f /im HWiNFO32.exe")


def change_reading_types(json_data):
    reading_types = {'0': 'None', '1': 'Temp', '2': 'Voltage',
                     '3': 'Fan', '4': 'Current', '5': 'Power',
                     '6': 'Clock', '7': 'Usage', '8': 'Other'}
    for index, value in enumerate(json_data['readings']):
        json_data['readings'][index]['readingTypeName'] = reading_types[str(value['readingType'])]
    return json_data


def get_modified_json():
    json_data = requests.get(REMOTE_HWINFO_URL, verify=False, timeout=5).json()['hwinfo']

    for sensor_index, hardware in enumerate(json_data['sensors']):
        json_data['sensors'][sensor_index]['sensorIndex'] = sensor_index

    for reading_index, reading in enumerate(json_data['readings']):
        json_data['readings'][reading_index]['readingIndex'] = reading_index

    change_reading_types(json_data)
    return json_data


@flask_app.route('/')
def get_all_values():
    return flask.jsonify(get_modified_json())


@flask_app.route("/status")
def status():
    try:
        get_modified_json()
        json = {"code": 200, "message": "All systems are working"}
    except requests.exceptions.ConnectionError as error:
        json = {"code": 500, "message": f'{error} (try to check connection with remotehwinfo.exe)'}
    except Exception as error:
        json = {"code": 500, "message": f'{error} (try to check connection with HWiNFO32.exe)'}

    return flask.jsonify(json)


@flask_app.route('/hardware_inventory')
def get_hardware_inventory():
    """Get a list of hardware on the PC as a text separated by newlines"""
    json_data = get_modified_json()

    ignore_list = ('Memory Timings', 'RTSS',
                   'Drive: Msft Virtual Disk',
                   'Windows Hardware Errors (WHEA)')
    hardware_list = list()

    for sensor_index, hardware in enumerate(json_data['sensors']):

        if hardware['sensorNameUser'] not in ignore_list:
            tmp_str = f"{hardware['sensorNameUser']}\n"
            hardware_list.append(tmp_str)
            hardware_list.sort()

    return "".join(hardware_list)


def get_lld_sensors():
    json_data = get_modified_json()

    datalist = list()
    for hardware in json_data['sensors']:
        for reading in json_data['readings']:
            if reading['sensorIndex'] == hardware['sensorIndex']:
                datadict = {"{#SENSORNAMEUSER}": hardware['sensorNameUser'],
                            "{#SENSORINDEX}": hardware['sensorIndex'],
                            "{#LEBALUSER}": reading['labelUser'],
                            "{#READINGINDEX}": reading['readingIndex'],
                            "{#READINGID}": reading['readingId'],
                            "{#READINGTYPENAME}": reading['readingTypeName'],
                            "{#READINGTYPE}": reading['readingType'],
                            "{#VALUE}": reading['value'],
                            "{#UNIT}": reading['unit']}
                datalist.append(datadict)
    return datalist


@flask_app.route("/hardware_lld")
def scan_hardware_lld():
    sensors = get_lld_sensors()
    for sensor in sensors:
        del sensor["{#VALUE}"]
    return flask.jsonify(sensors)


@flask_app.route("/value_lld/<int:reading_index>")
def get_value_lld(reading_index):
    sensors = get_lld_sensors()
    debug = flask.request.args.get('debug', default="False", type=str)

    if debug == "True":
        for sensor in sensors:
            if sensor["{#READINGINDEX}"] == reading_index:
                return flask.jsonify(sensors[reading_index])

    for sensor in sensors:
        if sensor["{#READINGINDEX}"] == reading_index:
            return flask.jsonify(sensor["{#VALUE}"])


@flask_app.route("/docs", methods=['GET'])
def get_docs():
    """Print available methods. """

    func_dict = {}
    for rule in flask_app.url_map.iter_rules():
        if rule.endpoint != 'static':
            if flask_app.view_functions[rule.endpoint].__doc__ is None:
                func_dict[rule.rule] = ''
            else:
                func_dict[rule.rule] = flask_app.view_functions[rule.endpoint].__doc__

    sorted_list = sorted(func_dict.items(), key=lambda value: len(value[0]))
    sorted_dict = dict(sorted_list)

    # return dict(sorted_list)
    return flask.render_template('results.html', sorted_dict=sorted_dict)


if __name__ == '__main__':
    try:
        run_processes()
        flask_app.run(host=FLASK_HOST, port=FLASK_PORT)
        kill_processes()
    except Exception as e:
        print(e)
