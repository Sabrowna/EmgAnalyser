from abc import ABC, abstractmethod
import Adafruit_ADS1x15


class IEmgReader(ABC):
    @abstractmethod
    def readSensor(channelAmount):
        pass


class Adc(IEmgReader):
    def __init__(self) -> None:
        self.adc = Adafruit_ADS1x15.ADS1015()

    def readSensor(self, channelAmount):
        emgValuesDict = {}
        emgValuesDict.clear()
        for channel in range(channelAmount):
            self.adc.start_adc(channel)
            emgInVoltage = (self.adc.read_adc(channel)) * (5/2048)
            print('channel' + str(channel) + ': ' + str(emgInVoltage))
            emgValuesDict[channel] = emgInVoltage
        return emgValuesDict


class EmgReader():
    def readAdcChannels(channels):
        adc = IEmgReader()
        adcValues = adc.readSensor()

        for adcValue in adcValues:
            print(adcValue)


e = EmgReader()
EmgReader.readAdcChannels(2)
