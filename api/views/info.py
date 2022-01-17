import flask
import requests
from flask import render_template

from api import app
from api.json_handler import get_modified_json


@app.route("/", methods=['GET'])
def get_docs():
    """Print documentation."""
    func_dict = {}
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            if app.view_functions[rule.endpoint].__doc__ is None:
                func_dict[rule.rule] = ''
            else:
                func_dict[rule.rule] = app.view_functions[rule.endpoint].__doc__

    sorted_list = sorted(func_dict.items(), key=lambda value: len(value[0]))
    sorted_dict = dict(sorted_list)

    return render_template('results.html', sorted_dict=sorted_dict)


@app.route('/json')
def get_all_values():
    """Return preprocessed JSON from RemoteHWInfo."""
    return flask.jsonify(get_modified_json())


@app.route("/status")
def get_status():
    """Return {"code": 200, "message": "All systems are working"} if all it's alright."""
    try:
        get_modified_json()
        json = {"code": 200, "message": "All systems are working"}
    except requests.exceptions.ConnectionError as error:
        json = {"code": 500, "message": f'{error} (try to check connection with remotehwinfo.exe)'}
    except Exception as error:
        json = {"code": 500, "message": f'{error} (try to check connection with HWiNFO32.exe)'}

    return flask.jsonify(json)


@app.route('/hardware_inventory')
def get_hardware_inventory():
    """Get a list of hardware on the PC as a text separated by newlines."""
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
