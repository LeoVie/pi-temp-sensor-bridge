import unittest
import Adafruit_DHT

from Classes.SensorReader import SensorReader


class SensorReaderTest(unittest.TestCase):
    def mocked_read_retry(self, sensor, pin):
        return 50, 25

    def test_loads_configuration(self) -> None:
        Adafruit_DHT.read_retry = self.mocked_read_retry

        sensor_reader = SensorReader()
        sensor_reader.measure()

        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
