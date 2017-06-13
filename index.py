from __future__ import print_function
import time
import twitter
from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('./app.cfg', silent=True)


@app.route("/")
def index():
    return "This is powered by Python backend.<brFlask + Electron desktop application!!!"

if __name__ == "__main__":
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
