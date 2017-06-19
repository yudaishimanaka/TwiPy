async_mode = None

if async_mode is None:
    try:
        import eventlet
        async_mode = 'eventlet'
    except ImportError:
        pass

    if async_mode is None:
        try:
            from gevent import monkey
            async_mode = 'gevent'
        except ImportError:
            pass

    if async_mode is None:
        async_mode = 'threading'

    print('async_mode is ' + async_mode)

if async_mode == 'eventlet':
    import eventlet
    eventlet.monkey_patch()
elif async_mode == 'gevent':
    from gevent import monkey
    monkey.patch_all()

import json
import time
from threading import Thread
from flask import Flask, render_template, session, request, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect
from tweepy.streaming import StreamListener, Stream
import tweepy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config.from_pyfile('./app.cfg', silent=True)
socketio = SocketIO(app, async_mode=async_mode)
thread = None

auth = tweepy.OAuthHandler(app.config['CONSUMER_KEY'], app.config['CONSUMER_SECRET'])
auth.set_access_token(app.config['TOKEN'], app.config['TOKEN_SECRET'])


class StdOutListner(StreamListener):
    def on_data(self, raw_data):
        try:
            tweet = json.loads(raw_data)
            print(tweet)
            socketio.emit('stream_channel',
                          {'data': tweet},
                          namespace='/user_streaming')
        except ValueError:
            pass

    def on_error(self, status_code):
        print('Error status code', status_code)
        exit()


def background():
    stream = Stream(auth, l, secure=True)
    stream.userstream()


def restapi_timeline():
    api = tweepy.API(auth)
    home_timeline = api.home_timeline(count=30)
    return home_timeline


@app.route('/')
def index():
    global thread
    if thread is None:
        thread = Thread(target=background)
        thread.daemon = True
        thread.start()
    return render_template('index.html', home_timeline=restapi_timeline())

l = StdOutListner()

if __name__ == '__main__':
    socketio.run(app, debug=True, host='127.0.0.1')
