import unittest

from Classes.Measurement import Measurement


class SensorReaderTest(unittest.TestCase):
    measurement = None

    def setUp(self) -> None:
        self.measurement = Measurement()

    def test_returns_initial_temperature(self):
        expected = 0
        actual = self.measurement.get_temperature()

        self.assertEqual(expected, actual)

    def test_set_temperature(self):
        expected = 10.50
        self.measurement.set_temperature(expected)

        actual = self.measurement.get_temperature()

        self.assertEqual(expected, actual)

    def test_returns_initial_relative_humidity(self):
        expected = 0
        actual = self.measurement.get_relative_humidity()

        self.assertEqual(expected, actual)

    def test_set_relative_humidity(self):
        expected = 45.30
        self.measurement.set_relative_humidity(expected)

        actual = self.measurement.get_relative_humidity()

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
