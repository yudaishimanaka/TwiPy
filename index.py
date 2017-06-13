from flask import Flask
from twitter import *

app = Flask(__name__)
app.config.from_pyfile('./app.cfg', silent=True)


@app.route("/")
def index():
    auth = OAuth(
        consumer_key=app.config['CONSUMER_KEY'],
        consumer_secret=app.config['CONSUMER_SECRET'],
        token=app.config['TOKEN'],
        token_secret=app.config['TOKEN_SECRET']
    )
    twitter_userstream = TwitterStream(auth=auth, domain='userstream.twitter.com')
    for msg in twitter_userstream.user():
        print(msg.get('text'))

if __name__ == "__main__":
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
