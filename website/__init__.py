from flask import Flask
from website.config import Config

application = Flask(__name__)
application.config.from_object(Config)

from website import routes