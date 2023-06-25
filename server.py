from flask import Flask, render_template
from flask_socketio import SocketIO
import wiringpi;

wiringpi.wiringPiSetup();

wiringpi.pinMode(2, 1)

app = Flask('app',static_url_path='', 
            static_folder='templates')

@app.route('/')
def index():
  return render_template('index.html')
socketio = SocketIO(app)
on = False;
def Reverse(b):
  if (b):
    return False
  if (b == False):
    return True
def boolToInt(b):
  if (b):
    return 1
  if (b == False):
    return 0
@socketio.on('button')
def buttonMsg(data):
  on = Reverse(on)
  wiringpi.digitalWrite(2, boolToInt(on))


if __name__ == '__main__':
    socketio.run(app)