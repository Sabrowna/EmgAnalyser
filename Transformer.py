from Sensor import Sensor
from ConfigReader import ConfigReader
from DtoCreator import *
import abc
import time
from EmgReader import IEmgReader


class ITransformer(abc.ABC):
    @abc.abstractmethod
    def observeSensors(self):
        raise NotImplementedError


class Transformer():
    def __init__(self, configPath, emgReader: IEmgReader) -> None:
        self.configPath = configPath
        self.sensorList = []
        self.configReader = ConfigReader(configPath)
        self.dtoCreator = DtoCreator()
        self.sensorAmount = self.configReader.getSensorAmount()
        self.activationVoltage = self.configReader.getActivationVoltage()
        self.hysteresisValue = self.configReader.getHysteresisValue()
        self.emgReader = emgReader
        self.__initializeEachSensor()
        print("initialized in transformer")

    def __initializeEachSensor(self):
        for i in range(self.configReader.getSensorAmount()):
            sensor = Sensor()
            motorDirection = self.configReader.getMotorDirections()[i]
            sensorConfig = self.configReader.getSensorConfig()[i]

            sensor.setMotorDirection(motorDirection[1])
            sensor.setSensorsMotorcontrol(sensorConfig[1])
            self.sensorList.append(sensor)

    def observeSensors(self):
        emgValues = self.emgReader.readSensor(self.sensorAmount)

        for i in range(self.sensorAmount):
            if self.sensorList[i].getMotorDirection() == 'd':
                #print('sensor' + str(i+1))
                self.__handleDoubleTensionSensor(
                    self.sensorList[i], emgValues[i])
            else:
                if (i % 2 == 0):
                    self.__handleSingleTensionSensor(
                        self.sensorList[i], self.sensorList[i+1], emgValues[i], emgValues[i+1], self.sensorAmount)
        return self.dtoCreator.getActionDto()

    def __handleDoubleTensionSensor(self, sensor, sensorValue):
        if sensorValue >= 2:
            #print(f'time: {self.__getTimeNow()}\n previous time: {sensor.getPreviousTensionTime()}\n forskel: {self.__getTimeNow() - sensor.getPreviousTensionTime()}')
            if sensor.getIsDoubleTensionActivated() == False:
                print(sensor.getPreviousTensionTime())
                if sensor.getPreviousTensionTime() == 0:
                    sensor.setPreviousTensionTime(self.__getTimeNow())
                if sensor.getHasRelaxed() == True:
                    if (self.__getTimeNow() - sensor.getPreviousTensionTime()) <= 1500:
                        self.__doubleTension(sensor)
                    else:
                        self.__resetDoubleTension(sensor)

                elif self.__getTimeNow() - sensor.getPreviousTensionTime() > 1000:
                    print("self.getTIme > 1000")
                    self.__resetDoubleTension(sensor)

        elif sensorValue < 2:
            #print(f'time: {self.__getTimeNow()}\n previous time: {sensor.getPreviousTensionTime()}\n forskel: {self.__getTimeNow() - sensor.getPreviousTensionTime()}')
            if (self.__getTimeNow() - sensor.getPreviousTensionTime() < 1500):
                if sensor.getRelaxTime() == 0:
                    sensor.setRelaxTime(self.__getTimeNow())
                    sensor.setHasRelaxed(True)
            else:
                sensor.setMotorDirection('s')
                self.__resetDoubleTension(sensor)

    def __handleSingleTensionSensor(self, sensor1, sensor2, emgValue1, emgValue2, sensorAmount):
        if emgValue1 > self.activationVoltage and emgValue2 > self.activationVoltage:
            pass
        elif emgValue1 >= self.activationVoltage and emgValue2 < self.activationVoltage:
            sensor1.setIsActive(True)
            self.dtoCreator.createActionDto(sensor1, False)
        elif emgValue1 < self.activationVoltage and emgValue2 >= self.activationVoltage:
            sensor2.setIsActive(True)
            self.dtoCreator.createActionDto(sensor2, False)
        elif emgValue1 < self.hysteresisValue and emgValue2 < self.hysteresisValue:
            sensor1.setIsActive(False)
            sensor2.setIsActive(False)
            self.dtoCreator.createActionDto(sensor1, False)
            self.dtoCreator.createActionDto(sensor2, False)
        else:
            pass

    def __getTimeNow(self):
        return time.time_ns() / 1000000

    def __doubleTension(self, sensor):
        self.dtoCreator.createActionDto(sensor, True)
        sensor.setIsDoubleTensionActivated(True)
        sensor.setPreviousTensionTime(0)
        sensor.setRelaxTime(0.0)
        sensor.setHasRelaxed(False)

    def __resetDoubleTension(self, sensor):
        sensor.setPreviousTensionTime(0)
        self.dtoCreator.createActionDto(sensor, False)
        sensor.setRelaxTime(0.0)
        sensor.setIsDoubleTensionActivated(False)
        sensor.setHasRelaxed(False)
        sensor.setMotorDirection('d')
