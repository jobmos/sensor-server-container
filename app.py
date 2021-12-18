# DHT
import adafruit_dht
import board
import time
dht = adafruit_dht.DHT22(board.D4)

# FLASK
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    try:
        temperature = dht.temperature
        humidity = dht.humidity
        message = "Temperature: " + str(temperature) + "C, Humidity: " + str(humidity) + "%"
        return message 
        # Print what we got to the REPL
        print("Temp: {:.1f} *C \t Humidity: {}%".format(temperature, humidity))
    except RuntimeError as e:
        # Reading doesn't always work! Just print error and we'll try again
        print("Reading from DHT failure: ", e.args)
        return "error"

