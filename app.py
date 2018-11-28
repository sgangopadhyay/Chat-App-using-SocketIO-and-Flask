# Program : Chat Application using Python3.7, Flask, SocketIO and Bootstrap
# Programmed By : Suman Gangopadhyay
# Email ID : linuxgurusuman@gmail.com
# URL : https://www.linkedin.com/in/sumangangopadhyay/
# Date : 20-Nov-2018
# Language : Python3.6
# Framework : Flask
# Copyright © 2018 Suman Gangopadhyay
from flask import Flask, render_template, url_for, redirect
from flask_socketio import SocketIO, send, emit

app  = Flask(__name__)
app.config['SECRET_KEY'] ='i_love_pizza'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

def message_received():
    print("The message has been received !")

@socketio.on('my event')
def handle_message(json):
    print('received message : ' + str(json))
    socketio.emit('my response', json, callback = message_received)

if __name__ == '__main__':
    socketio.run(app, debug=True)
