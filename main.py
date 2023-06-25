import wiringpi

# One of the following MUST be called before using IO functions:
wiringpi.wiringPiSetup()      # For sequential pin numbering
wiringpi.pinMode(2, 0)  
wiringpi.digitalRead(2)   