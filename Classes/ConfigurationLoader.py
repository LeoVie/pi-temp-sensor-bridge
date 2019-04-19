from yaml import load
import os

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

from Classes.Configuration import Configuration


class ConfigurationLoader:
    DEFAULT_CONFIGURATION_PATH = os.path.dirname(os.path.abspath(__file__)) + '/../config.yml'

    @staticmethod
    def load_configuration(self, configuration_path=DEFAULT_CONFIGURATION_PATH):
        stream = open(configuration_path, "r", encoding="utf-8")
        configuration_entries = load(stream, Loader=Loader)
        configuration = Configuration()
        if 'api-base-uri' in configuration_entries:
            configuration.api_base_uri = configuration_entries['api-base-uri']
        if 'sensor-type' in configuration_entries:
            configuration.sensor_type = configuration_entries['sensor-type']
        if 'gpio-pin' in configuration_entries:
            configuration.gpio_pin = configuration_entries['gpio-pin']

        stream.close()

        return configuration
