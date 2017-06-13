from __future__ import print_function
import twitter
from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('./app.cfg', silent=True)


@app.route("/")
def index():
    return "hello!!"

if __name__ == "__main__":
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
