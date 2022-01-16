import pytest
import requests

from config import FLASK_HOST, FLASK_PORT

if FLASK_HOST == '0.0.0.0':
    FLASK_HOST = '127.0.0.1'

keys = ['{#HARDWARENAME}', "{#HARDWAREINDEX}",
        "{#SENSORNAME}", "{#SENSORINDEX}",
        "{#SENSORTYPENAME}", "{#SENSORTYPEINDEX}",
        "{#VALUE}", "{#UNIT}"]


# noinspection HttpUrlsUsage
def get_request(method: str) -> requests.get:
    response = requests.get(f'http://{FLASK_HOST}:{FLASK_PORT}{method}')
    return response


def test_root():
    response = get_request('/')
    assert response.status_code == 200
    assert len(response.json()['sensors']) > 0
    assert len(response.json()['readings']) > 0


def test_docs():
    response = get_request('/docs')
    assert response.status_code == 200

    words = ['table', 'Method', 'Description']
    for word in words:
        assert word in response.text


def test_status():
    response = get_request('/status')
    assert response.status_code == 200
    assert response.json()['message'] == 'All systems are working'


def test_hardware_lld():
    response = get_request('/hardware_lld')
    assert response.status_code == 200
    assert len(response.json()) > 0

    for key in keys:
        assert key in response.json()[0]


def test_hardware_lld_unit():
    response = get_request('/hardware_lld?unit=rpm')
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()[0]["{#UNIT}"].lower() == 'rpm'


def test_hardware_lld_hardware_index():
    args = ('', '1', '4,2,3')
    for arg in args:
        response = get_request(f'/hardware_lld?hardware_index={arg}')
        assert response.status_code == 200
        assert len(response.json()) > 0
        if arg:
            arg = arg.split(',')
            assert response.json()[0]["{#HARDWAREINDEX}"] == int(min(arg))
            assert response.json()[-1]["{#HARDWAREINDEX}"] == int(max(arg))


def test_hardware_inventory():
    response = get_request('/hardware_inventory')
    assert response.status_code == 200
    assert 'System' in response.text


def test_value_lld():
    for query in (1, 58, 100):
        response = get_request(f'/value_lld/{query}')
        assert response.status_code == 200
        assert len(response.text)

    for query in ('3?debug=true', '4?debug=TrUe'):
        response = get_request(f'/value_lld/{query}')
        for key in keys:
            assert key in response.json()


if __name__ == '__main__':
    pytest.main()
