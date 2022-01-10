import paho.mqtt.client as mqtt
import time
myClient = mqtt.Client() # Create client object
myClient.username_pw_set("introkurs", "ht21")
myClient.connect("130.239.163.210", 1883)

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    if GPIO.input(12):
        myClient.publish("larm", "grupp13")
        time.sleep(1)

# Main program loop
while(1):
    time.sleep(0.1) # Sleep for a second
