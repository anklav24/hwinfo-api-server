#!/usr/bin/env/ python3
# coding=utf-8

import os

import flask
import requests

# Connection
REMOTE_HWINFO_IP = 'localhost'  # Default: localhost
REMOTE_HWINFO_PORT = '60000'  # Default: 60000
# noinspection HttpUrlsUsage
REMOTE_HWINFO_URL = f'http://{REMOTE_HWINFO_IP}:{REMOTE_HWINFO_PORT}/json.json'

FLASK_PORT = 50000  # Default: 50000
FLASK_HOST = "localhost"  # localhost, 0.0.0.0, 127.0.0.1 Default: localhost

os.startfile('HWiNFO32.exe',
             show_cmd=False)
os.startfile('remotehwinfo.exe',
             arguments=f"-port {REMOTE_HWINFO_PORT} -log 0 -hwinfo 1 -gpuz 0 -afterburner 0",
             show_cmd=False)

flask_app = flask.Flask(__name__)
flask_app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@flask_app.route('/hardware')
def scan_hardware():
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


if __name__ == '__main__':
    try:
        flask_app.run(host=FLASK_HOST, port=FLASK_PORT)
        os.system("taskkill /f /im remotehwinfo.exe")
        os.system("taskkill /f /im HWiNFO32.exe")
    except Exception as e:
        print(e)
