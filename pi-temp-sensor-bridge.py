#!/usr/bin/python

from Classes.SensorReader import SensorReader
from Classes.ConfigurationLoader import ConfigurationLoader
import requests
import json
import os


def save_measurement():
    configuration = ConfigurationLoader.load_configuration(os.path.abspath('config.yml'))

    sensor_reader = SensorReader()
    measurement = sensor_reader.measure()

    headers = {
        'Content-Type': 'application/json',
    }
    json_data = {
        'relative_humidity': measurement.get_relative_humidity(),
        'temperature': measurement.get_temperature()
    }

    requests.post(
        configuration.api_base_uri + '/measurement',
        data=json.dumps(json_data),
        headers=headers
    )


save_measurement()
