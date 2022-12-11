from abc import ABC, abstractmethod
import configparser


class IConfigReader(ABC):
    @abstractmethod
    def readConfigFile():
        raise NotImplementedError


class ConfigReader(IConfigReader):
    def __init__(self, configPath) -> None:
        self.configPath = configPath
        self.config = self.readConfigFile()
        self.setSensorAmount()
        self.setMotorDirections()
        self.setSensorConfig()
        self.setActivationVoltage()
        self.setHysteresisValue()

    def readConfigFile(self):
        config = configparser.RawConfigParser()
        config.read(self.configPath)
        return config

    def setSensorAmount(self):
        self.sensorAmount = len(self.config.items('sensors'))

    def getSensorAmount(self):
        return self.sensorAmount

    def setMotorDirections(self):
        self.motorDirections = self.config.items('motordirection')

    def getMotorDirections(self):
        return self.motorDirections

    def setSensorConfig(self):
        self.sensorConfig = self.config.items('sensors')

    def getSensorConfig(self):
        return self.sensorConfig

    def setActivationVoltage(self):
        self.activationVoltage = float(self.config.items('thresholds')[0][1])

    def getActivationVoltage(self):
        return self.activationVoltage

    def setHysteresisValue(self):
        self.hysteresisValue = float(self.config.items('thresholds')[1][1])

    def getHysteresisValue(self):
        return self.hysteresisValue
