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
        print("Succesfully read temperature and humidity")
        result = {
                "temperature": temperature,
                "humidity": humidity
                }
        return result
    except RuntimeError as e:
        print("Reading from DHT failure: ", e.args)
        return "error"
