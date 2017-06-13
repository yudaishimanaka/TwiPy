from __future__ import print_function
import time
from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello():
    return "This is powered by Python backend.<br>" \
		   "Flask + Electron desktop application!!!"

if __name__ == "__main__":
	print('on hello')
	app.run(host="127.0.0.1", port=5000)
