from os import name
import flask
import sys
from flask import Flask, render_template, Response
from flask.templating import render_template_string
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from pygame import mixer
from flask_cors import CORS
import logging
root = logging.getLogger()
root.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)

app = Flask(__name__)
CORS(app)
numm = 0


def return_dict():
    # Dictionary to store music file information
    dict_here = [
        {'id': 1, 'name': '兩隻老虎', 'link': 'music/tigar.mp3'},
        {'id': 2, 'name': '嗡嗡嗡', 'link': 'music/bee.mp3'},
        {'id': 3, 'name': '搖籃曲', 'link': 'music/sleep.mp3'}
    ]
    return dict_here

@app.route('/')
def home():
    return render_template_string(name='123',id='456')


@app.route('/play/sleep')
def playSleep():
    global numm 
    mixer.init()
    mixer.music.set_volume(0.5)
    mixer.music.load('D:/projects/flask-music-streaming-master/music/sleep.wav')
    mixer.music.play()
    numm = 1   
    return "code", 200 


@app.route('/stop')
def stopSleep():
    mixer.init()
    mixer.music.stop()
    return "code", 200

@app.route('/pause/sleep')
def pauseSleep():
    mixer.init()
    mixer.music.pause()
    return "code", 200


@app.route('/unpause/sleep')
def unpauseSleep():
    mixer.init()
    mixer.music.unpause()
    return "code", 200


# 小蜜蜂API


@app.route('/play/bee')
def playBEE():
    global numm
    mixer.init()
    mixer.music.load('D:/projects/flask-music-streaming-master/music/bee.wav')
    mixer.music.play()
    numm = 2
    return "code", 200


@app.route('/pause/bee')
def pauseBEE():
    mixer.init()
    mixer.music.pause()
    return "code", 200


@app.route('/unpause')
def unpauseBEE():
    mixer.init()
    mixer.music.unpause()
    return "code", 200
# tigar api


@app.route('/pause')
def pause():
    mixer.init()
    mixer.music.pause()
    return "code", 200

@app.route('/play/tigar')
def playTigar():
    global numm
    mixer.init()
    mixer.music.load(
        'D:/projects/flask-music-streaming-master/music/tigar.wav')
    mixer.music.play()
    numm = 3
    return "code", 200


@app.route('/pause/tigar')
def pauseTigar():
    mixer.init()
    mixer.music.pause()
    return "code", 200


@app.route('/unpause/tigar')
def unpauseTigar():
    mixer.init()
    mixer.music.unpause()
    return "code", 200


@app.route('/play/star')
def playStar():
    global numm
    mixer.init()
    mixer.music.load(
        'D:/projects/flask-music-streaming-master/music/star.wav')
    mixer.music.play()
    numm = 4
    return "code", 200

@app.route('/next')
def next():
    global numm
    if numm == 1:
        mixer.init()
        mixer.music.pause()
        mixer.music.load(
            'D:/projects/flask-music-streaming-master/music/tigar.wav')
        mixer.music.play()
        numm += 1
        return "code", 200
    if numm == 2:
        mixer.init()
        mixer.music.pause()
        mixer.music.load(
            'D:/projects/flask-music-streaming-master/music/bee.wav')
        mixer.music.play()
        numm += 1
        return "code", 200
    if numm == 3:
        mixer.init()
        mixer.music.pause()
        mixer.music.load(
            'D:/projects/flask-music-streaming-master/music/star.wav')
        mixer.music.play()
        numm +=1
        return "code", 200
    if numm == 4:
        mixer.init()
        mixer.music.pause()
        mixer.music.load(
                'D:/projects/flask-music-streaming-master/music/sleep.wav')
        mixer.music.play()
        numm -=3
        return "code", 200
        
@app.route('/Volume1')
def Volume100():
        mixer.music.set_volume(1)
        return "code", 200


@app.route('/Volume0.9')
def Volume90():
        mixer.music.set_volume(0.9)
        return "code", 200

@app.route('/Volume0.8')
def Volume80():
        mixer.music.set_volume(0.8)
        return "code", 200

@app.route('/Volume0.7')
def Volume70():
        mixer.music.set_volume(0.7)
        return "code", 200

@app.route('/Volume0.6')
def Volume60():
        mixer.music.set_volume(0.6)
        return "code", 200

@app.route('/Volume0.5')
def Volume50():
        mixer.music.set_volume(0.5)
        return "code", 200

@app.route('/Volume0.4')
def Volume40():
        mixer.music.set_volume(0.4)
        return "code", 200

@app.route('/Volume0.3')
def Volume30():
        mixer.music.set_volume(0.3)
        return "code", 200

@app.route('/Volume0.2')
def Volume20():
        mixer.music.set_volume(0.2)
        return "code", 200

@app.route('/Volume0.1')
def Volume10():
        mixer.music.set_volume(0.1)
        return "code", 200

@app.route('/Volume0')
def Volume0():
        mixer.music.set_volume(0)
        return "code", 200

#@app.route('getTime')
#def getTime():
#        mixer.Sound.get_length()
#        return "code", 200


if __name__ == "__main__":
    #app.run(host="163.17.21.41", port=5002)
    port = 5001
    http_server = HTTPServer(WSGIContainer(app))
    logging.debug("Started Server, Kindly visit http://localhost:" + str(port))
    http_server.listen(port)
    IOLoop.instance().start()
