import requests

from config import REMOTE_HWINFO_IP, REMOTE_HWINFO_PORT

# noinspection HttpUrlsUsage
REMOTE_HWINFO_URL = f'http://{REMOTE_HWINFO_IP}:{REMOTE_HWINFO_PORT}/json.json'


def change_reading_types(json_data: dict) -> dict:
    reading_types = {'0': 'None', '1': 'Temp', '2': 'Voltage',
                     '3': 'Fan', '4': 'Current', '5': 'Power',
                     '6': 'Clock', '7': 'Usage', '8': 'Other'}
    for index, value in enumerate(json_data['readings']):
        json_data['readings'][index]['readingTypeName'] = reading_types[str(value['readingType'])]
    return json_data


def get_modified_json() -> dict:
    json_data = requests.get(REMOTE_HWINFO_URL, verify=False, timeout=5).json()['hwinfo']

    for sensor_index, hardware in enumerate(json_data['sensors']):
        json_data['sensors'][sensor_index]['sensorIndex'] = sensor_index

    for reading_index, reading in enumerate(json_data['readings']):
        json_data['readings'][reading_index]['readingIndex'] = reading_index

    change_reading_types(json_data)
    return json_data


def get_lld_sensors() -> list[dict]:
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
