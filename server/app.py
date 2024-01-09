import os
from dotenv import load_dotenv

from flask import Flask
from flask_cors import CORS

# from models import db
from resources import api


load_dotenv()

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('PRODUCTION_DATABASE_URI')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True  # False for production
app.config["API_CDN_URL"] = os.getenv('CDN_URL')

# initialization db
# db.init_app(app)

# initialization api
api.init_app(app)


if __name__ == "__main__":
    # run `gunicorn app:app -c gunicorn.conf.py` into `/server` in console for deploy it
    app.run(host="0.0.0.0", port=5000)
