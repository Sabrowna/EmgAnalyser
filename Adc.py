from abc import ABC, abstractmethod
import Adafruit_ADS1x15


class AbstractAdc(ABC):
    @abstractmethod
    def readAdc(channel, gain):
        pass


class Adc(AbstractAdc):
    def __init__(self, gain, channelAmount) -> None:
        self.adc = Adafruit_ADS1x15.ADS1015
        self.gain = gain

        for channel in range(channelAmount):
            self.adc.start_adc(channel, self.gain)
            print('channel: ' + channel)

    def setAdcValue(self, adcVal):
        self.adcValue = adcVal
        print('set adc to ' + self.adcValue)

    def getAdcValue(self):
        return self.adcValue
# Hvert tal skal tilføjes til en liste

    def readAdc(self, channel):

        localAdcVal = Adafruit_ADS1x15.ADS1015.read_adc(self.adc, channel)
        Adc.setAdcValue(localAdcVal)

        print(str(localAdcVal))


a = Adc(1, 1)
while True:
    a.readAdc(0)
