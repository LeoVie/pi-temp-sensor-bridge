from Classes.ConfigurationLoader import ConfigurationLoader
from Classes.Measurement import Measurement
import Adafruit_DHT
import sys


class SensorReader:
    configuration = None
    sensor_args = {11: Adafruit_DHT.DHT11,
                   22: Adafruit_DHT.DHT22,
                   2302: Adafruit_DHT.AM2302}

    def measure(self):
        self.configuration = ConfigurationLoader.load_configuration('config.yml')

        if self.configuration.sensor_type in self.sensor_args:
            sensor = self.sensor_args[self.configuration.sensor_type]
            pin = self.configuration.gpio_pin
        else:
            print('Sensor incorrect.')
            sys.exit(1)

        relative_humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

        measurement = Measurement()
        measurement.relative_humidity = relative_humidity
        measurement.temperature = temperature

        return measurement
