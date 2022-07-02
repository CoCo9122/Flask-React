from flask import Flask
from flask_cors import CORS
import os

from exsample1.exsample1 import exsample1_bp
from database import init_db
import models

config_type = {
    "development": "config.Development",
    "testing": "config.Testing",
    "production": "config.Production"
}

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_type.get(os.getenv('FLASK_APP_ENV')))

    init_db(app)
    
    app.register_blueprint(exsample1_bp, url_prefix='/exsample1')

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)