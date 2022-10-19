import Testdata
from abc import ABC, abstractmethod


# The abstract class from which the sensor can inherit
class AbstractSensor(ABC):
    @abstractmethod
    def readSensor(channel):
        pass


# This is a subclass implementing the AbstractSensor
class Sensor(AbstractSensor):
    def readSensor(channel):
        sensorValue = Testdata.randomDataGenerator()
        print("Reading from channel " + str(channel) +
              " with value: " + str(sensorValue))
        return sensorValue
