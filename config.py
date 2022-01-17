import logging

FLASK_PORT = 50000  # Default: 50000
FLASK_HOST = "0.0.0.0"  # Default: 0.0.0.0
REMOTE_HWINFO_PORT = 60005  # Default: 60005
REMOTE_HWINFO_IP = '127.0.0.1'  # Default: 127.0.0.1

JSONIFY_PRETTYPRINT_REGULAR = True
JSON_SORT_KEYS = False

CSRF_ENABLED = True
THREADS_PER_PAGE = 2

FLASK_ENV = "production"  # development, production
DEVELOPMENT = False  # True, False
DEBUG = False  # True, False
TESTING = False  # True, False

# Suppress WARNING: This is a development server. Do not use it in a production deployment.
DEVELOP_ENV = True  # Select the serve (False) or flask server (True)

# Third-party loggers
logging.getLogger('werkzeug').setLevel(logging.DEBUG)
