from Sensors import Sensor
import configparser


class EmgReader():
    def readConfigFile():
        configParser = configparser.RawConfigParser()
        configFilePath = r"C:\Users\Bruger\Documents\7. semester\Bachelor\SW\EmgAnalyser\config.txt"
        configParser.read(configFilePath)

        sensorAmount = configParser.get('system', 'sensors')
        adcAmount = configParser.get('system', 'adc')
        return sensorAmount, adcAmount

    def convertBitsToVoltage(self, bits):
        voltage = (5/2048) * bits
        return voltage


e = EmgReader()
sensorNumber = e.readConfigFile()[0]
adcAmount = e.readConfigFile()[1]
bits = Sensor.readSensor(sensorNumber)
voltage = e.convertBitsToVoltage(bits)
