from app import app
from app.third_party.process_control import kill_processes, run_processes

from config import FLASK_HOST, FLASK_PORT, REMOTE_HWINFO_PORT

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config["JSON_SORT_KEYS"] = False
app.config["FLASK_ENV"] = 'development'

if __name__ == '__main__':
    try:
        run_processes(REMOTE_HWINFO_PORT)
        app.run(host=FLASK_HOST, port=FLASK_PORT)
        kill_processes()
    except Exception as e:
        print(e)
