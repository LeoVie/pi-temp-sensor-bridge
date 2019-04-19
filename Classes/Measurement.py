class Measurement:
    # TODO: define min max
    __relative_humidity = 0
    __temperature = 0

    def set_relative_humidity(self, relative_humidity):
        self.__relative_humidity = relative_humidity

    def get_relative_humidity(self):
        return self.__relative_humidity

    def set_temperature(self, temperature):
        self.__temperature = temperature

    def get_temperature(self):
        return self.__temperature
