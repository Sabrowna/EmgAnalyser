from abc import ABC, abstractmethod
import random
import Adafruit_ADS1x15


class IEmgReader(ABC):
    @abstractmethod
    def readSensor(self, channelAmount):
        raise NotImplementedError


class FakeAdc(IEmgReader):
    def readSensor(self, channelAmount):
        emgValuesDict = {}
        emgValuesDict.clear()
        for channel in range(channelAmount):
            emgInVoltage = (random.randrange(0, 2048)) * (5/2048)
            emgValuesDict[channel] = emgInVoltage
        print('dict: ' + str(emgValuesDict))
        return emgValuesDict


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


# ------------ Apparantly this is not how to do it. Instead you impl. interface in the other class (emg transformer)
# class EmgReader():
#     def readAdcChannels(channels):
#         adc = FakeAdc()
#         adcValues = adc.readSensor(channels)

#         for adcValue in adcValues:
#             print(adcValue)


# e = EmgReader()
# while True:
#     EmgReader.readAdcChannels(2)