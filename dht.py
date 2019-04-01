# import sys
import Adafruit_DHT
import requests
from w1thermsensor import W1ThermSensor

# Definimos el sensor y el pin al que lo conectamos
sensor = Adafruit_DHT.DHT11
pin = 7
sensor_t = W1ThermSensor()

# Necesario para thinhspeak
api_key = "*****************"
base_url = "https://api.thingspeak.com/update"

#   sensor_args = { '11': Adafruit_DHT.DHT11,
#                    '22': Adafruit_DHT.DHT22,
#                    '2302': Adafruit_DHT.AM2302 }

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
temperature_in_celsius = sensor_t.get_temperature()

# Un-comment the line below to convert the temperature to Fahrenheit.
# temperature = temperature * 9/5.0 + 32

payload = {"api_key":api_key,"field1":temperature_in_celsius,"field2":humidity}
r = requests.get(base_url, params = payload)