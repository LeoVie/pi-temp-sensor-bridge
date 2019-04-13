import unittest
from Classes.Configuration import Configuration
from Classes.ConfigurationLoader import ConfigurationLoader
import os


class ConfigurationLoaderTest(unittest.TestCase):
    def test_loads_configuration(self) -> None:
        configuration = ConfigurationLoader.load_configuration(self, os.path.abspath('testdata/config_good.yml'))

        self.assertIsInstance(configuration, Configuration)

    def test_loads_configuration_with_expected_sensor_type(self) -> None:
        configuration = ConfigurationLoader.load_configuration(self, os.path.abspath('testdata/config_good.yml'))

        expected = 11
        actual = configuration.sensor_type

        self.assertEqual(expected, actual)

    def test_loads_configuration_with_expected_gpio_pin(self) -> None:
        configuration = ConfigurationLoader.load_configuration(self, os.path.abspath('testdata/config_good.yml'))

        expected = 4
        actual = configuration.gpio_pin

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
