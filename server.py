from flask import Flask, render_template
from flask_socketio import SocketIO
import wiringpi
import threading
# One of the following MUST be called before using IO functions:
b1 = 2;
b2 = 5;
wiringpi.wiringPiSetup()      # For sequential pin numbering
wiringpi.pinMode(b1, 0) 
wiringpi.pinMode(b2, 0) 

app = Flask('app',static_url_path='', 
            static_folder='templates')

@app.route('/')
def index():
  return render_template('index.html')

socketio = SocketIO(app)

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

def record_loop():
    while True:
      b1Value = wiringpi.digitalRead(b1)*-1
      b2Value = wiringpi.digitalRead(b2)*-1
      socketio.emit("UpdatedKeys",[b1Value,b2Value])

if __name__ == '__main__':
  t = threading.Thread(target=record_loop, args=[0])
  t.start()
  socketio.run(app, host='0.0.0.0')