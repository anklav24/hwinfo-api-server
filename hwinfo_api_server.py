import threading

import pytest
from waitress import serve

from api import app
from api.third_party.process_control import kill_processes, run_processes
from config import DEVELOP_ENV, FLASK_HOST, FLASK_PORT, REMOTE_HWINFO_PORT

if __name__ == '__main__':
    try:
        run_processes(REMOTE_HWINFO_PORT)

        thread = threading.Thread(target=pytest.main, args=[['-v']])
        thread.start()

        if DEVELOP_ENV:
            app.run(host=FLASK_HOST, port=FLASK_PORT)
        else:
            serve(app, host=FLASK_HOST, port=FLASK_PORT)

        kill_processes()
    except Exception as e:
        app.logger.exception(e)
