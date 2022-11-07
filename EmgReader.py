from abc import ABC, abstractmethod
import random
import Adafruit_ADS1x15


class IEmgReader(ABC):
    @abstractmethod
    def readSensor(self, channelAmount):
        raise NotImplementedError


class Adc(IEmgReader):
    def __init__(self, adcType) -> None:
        if (adcType == 'ads1015'):
            self.adc = Adafruit_ADS1x15.ADS1015()
        elif (adcType == 'ads1115'):
            self.adc = Adafruit_ADS1x15.ADS1115()

    def readSensor(self, channelAmount):
        emgValuesDict = {}
        emgValuesDict.clear()
        for channel in range(channelAmount):
            self.adc.start_adc(channel)
            emgInVoltage = (self.adc.read_adc(channel)) * (5/2048)
            print('channel' + str(channel) + ': ' + str(emgInVoltage))
            emgValuesDict[channel] = emgInVoltage
        return emgValuesDict
