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


@flask_app.route('/')
def get_json():
    json_data = requests.get(REMOTE_HWINFO_URL, verify=False, timeout=5).json()
    return flask.jsonify(json_data)


@flask_app.route('/hardware')
def scan_hardware():
    json_data = requests.get(REMOTE_HWINFO_URL, verify=False, timeout=5).json()

    ignore_list = ('Memory Timings', 'RTSS',
                   'Drive: Msft Virtual Disk',
                   'Windows Hardware Errors (WHEA)')
    hardware_list = list()

    for sensor_index, hardware in enumerate(json_data['hwinfo']['sensors']):

        if hardware['sensorNameUser'] not in ignore_list:
            tmp_str = f"{hardware['sensorNameUser']}\n"
            hardware_list.append(tmp_str)
            hardware_list.sort()

    return "".join(hardware_list)


@flask_app.route('/hardware_lld')
def scan_hardware_lld():
    json_data = requests.get(REMOTE_HWINFO_URL, verify=False, timeout=5).json()

    datalist = list()
    for sensor_index, hardware in enumerate(json_data['hwinfo']['sensors']):
        json_data['hwinfo']['sensors'][sensor_index]['sensorIndex'] = sensor_index
        datadict = {"{#SENSORINDEX}": sensor_index, "{#SENSORNAMEUSER}": hardware['sensorNameUser']}
        datalist.append(datadict)

    return flask.jsonify(datalist)


@flask_app.route("/values")
def scan_values():
    json_data = requests.get(REMOTE_HWINFO_URL, verify=False, timeout=5).json()

    datalist = list()
    for sensor_index, hardware in enumerate(json_data['hwinfo']['sensors']):
        json_data['hwinfo']['sensors'][sensor_index]['sensorIndex'] = sensor_index
        for value_index, value in enumerate(json_data['hwinfo']['readings']):
            if json_data['hwinfo']['readings'][value_index]['sensorIndex'] == sensor_index:
                datadict = {"{#SENSORNAMEUSER}": hardware['sensorNameUser'],
                            "{#LEBALORIGINAL}": value['labelOriginal'],
                            "{#VALUE}": value['value'],
                            "{#UNIT}": value['unit']}
                datalist.append(datadict)

    return flask.jsonify(datalist)


# TODO: Add /status for zabbix checks about nodata (trigger)


def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)


@flask_app.route("/site-map")
def site_map():
    links = []
    for rule in flask_app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = flask.url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((f'method: {url}', f'function: {rule.endpoint}'))
    # links is now a list of url, endpoint tuples
    return flask.jsonify(links)


if __name__ == '__main__':
    try:
        run_processes()
        flask_app.run(host=FLASK_HOST, port=FLASK_PORT)
        kill_processes()
    except Exception as e:
        print(e)
