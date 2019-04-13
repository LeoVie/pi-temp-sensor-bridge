#!/usr/bin/python

from Classes.SensorReader import SensorReader


def main():
    sensor_reader = SensorReader()
    measurement = sensor_reader.measure()

    json \
        = '{"relative-humidity":' \
        + str(measurement.relative_humidity) \
        + ',' \
        + '"temperature":' \
        + str(measurement.temperature) \
        + '}'

    print(json)


main()
