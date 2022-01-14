import logging

FLASK_PORT = 50000  # Default: 50000
FLASK_HOST = "0.0.0.0"  # Default: 0.0.0.0
REMOTE_HWINFO_PORT = 60005  # Default: 60005
REMOTE_HWINFO_IP = '127.0.0.1'  # Default: 127.0.0.1

# Third-party loggers
logging.getLogger('werkzeug').setLevel(logging.INFO)
