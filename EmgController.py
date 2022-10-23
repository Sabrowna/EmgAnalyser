import configparser
from re import A

from EmgReader import Adc, IEmgReader


class EmgController():
    def __init__(self) -> None:
        # Fake code
        sensors = {
            'sensor0': 3,
            'sensor1': {'motors': [1, 2, 3, 4, 5],
                        'gripMove': 'e'},
            'sensor2': {'motors': [1, 2, 3, 4, 5],
                        'gripMove': 'f'}}

        self.length = len(sensors)
        print('length: ' + str(self.length))

        # Testing fake code
        print(sensors['sensor2'])
        print(sensors['sensor2']['motors'])
        print(sensors['sensor2']['motors'][0])
        print(sensors['sensor2']['gripMove'])

# TODO This one needs to be implemented
    def readConfigFile():
        configParser = configparser.RawConfigParser()
        configFilePath = r"C:\Users\Bruger\Documents\7. semester\Bachelor\SW\EmgAnalyser\config.txt"
        configParser.read(configFilePath)

        sensorAmount = configParser.get('system', 'sensors')
        adcAmount = configParser.get('system', 'adc')
        return sensorAmount, adcAmount

    def setLength(self, length):
        self.length = length

    def getLength(self):
        return self.length

    def getAdc(self):
        self.adc = Adc()
        return self.adc

    def getNewAction(reader, channels):
        reader.readEmgValues


e = EmgController()
adc = Adc()
e.getNewAction(adc, e.getLength())
