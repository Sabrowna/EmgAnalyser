from abc import ABC, abstractmethod
import Adafruit_ADS1x15


class IEmgReader(ABC):
    @abstractmethod
    def readEmgValues(channelAmount):
        pass


class Adc(IEmgReader):
    def __init__(self) -> None:
        self.adc = Adafruit_ADS1x15.ADS1015()

    def readEmgValues(self, channelAmount):
        listOfEmgValues = {}
        listOfEmgValues.clear()
        for localChannel in range(channelAmount):
            self.adc.start_adc(localChannel)
            emgValue = self.adc.read_adc(localChannel)
            emgInVoltage = emgValue * (5/2048)
            print('channel' + str(localChannel) + ': ' + str(emgInVoltage))
            listOfEmgValues[localChannel] = emgInVoltage
