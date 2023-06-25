import wiringpi;
import time;

wiringpi.wiringPiSetup();

pin = 2;
run = True;
start = False
wiringpi.pinMode(pin, 1)   
def boolToInt(b):
    if(b):
        return 1
    if(b == False):
       return 0
while run:
    time.sleep(0.5);
    start = not start;
    wiringpi.digitalWrite(pin, boolToInt(start))
