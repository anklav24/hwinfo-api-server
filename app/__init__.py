from flask import Flask

app = Flask(__name__, template_folder='api/templates', static_folder='api/static')

from app.api import views  # noqa: F401
