# ----- 3rd Party Libraries -----
from flask_restful import Api
from flask import Flask
from flask_apispec.extension import FlaskApiSpec

#  ----- Flask App Setup-----
app = Flask(__name__)
docs = FlaskApiSpec(app)

if __name__ == "__main__":
    app.config['DEBUG'] = True
    app.run(host="0.0.0.0", port=10000, debug=True)