from Sensor import Sensor
from ConfigReader import ConfigReader
from DtoCreator import *
import abc
import time


class ITransformer(abc.ABC):
    @abc.abstractmethod
    def handleSensorValues(self):
        raise NotImplementedError


class Transformer():
    def __init__(self, configPath, emgReader) -> None:
        self.configPath = configPath
        self.sensorList = []
        self.configReader = ConfigReader(configPath)
        self.dtoCreator = DtoCreator()
        self.sensorAmount = self.configReader.getSensorAmount()
        self.activationVoltage = self.configReader.getActivationVoltage()
        self.hysteresisValue = self.configReader.getHysteresisValue()
        self.emgReader = emgReader
        self.__initializeEachSensor()

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
                self.handleDoubleTensionSensor(
                    self.sensorList[i], emgValues[i])
            else:
                if (i % 2 == 0):
                    self.handleSingleTensionSensor(
                        self.sensorList[i], self.sensorList[i+1], emgValues[i], emgValues[i+1], self.sensorAmount)
        return self.dtoCreator.getActionDto()

    def handleDoubleTensionSensor(self, sensor, sensorValue):
        if sensorValue >= 2:
            if sensor.getIsDoubleTensionActivated() == False:
                print(sensor.getPreviousTensionTime())
                if sensor.getPreviousTensionTime() == 0:
                    sensor.setPreviousTensionTime(self.getTimeNow())
                if sensor.getHasRelaxed() == True:
                    if (self.getTimeNow() - sensor.getPreviousTensionTime()) < 1500:
                        self.doubleTension(sensor)
                    elif (self.getTimeNow() - sensor.getRelaxTime() > 1500):
                        # elif (self.getTimeNow() - sensor.getPreviusTensiontime() > 1500):
                        self.resetDoubleTension(sensor)
                    else:
                        pass
        elif sensorValue < 2:
            print(f'time: {self.getTimeNow()}\n previous time: {sensor.getPreviousTensionTime()}\n forskel: {self.getTimeNow() - sensor.getPreviousTensionTime()}')
            if (self.getTimeNow() - sensor.getPreviousTensionTime() < 1500):
                if sensor.getRelaxTime() == 0:
                    sensor.setRelaxTime(self.getTimeNow)
                    sensor.setHasRelaxed(True)
            else:
                sensor.setMotorDirection('s')
                self.resetDoubleTension(sensor)

    def handleSingleTensionSensor(self, sensor1, sensor2, emgValue1, emgValue2, sensorAmount):
        if emgValue1 > self.activationVoltage and emgValue2 > self.activationVoltage:
            pass
        elif emgValue1 >= self.activationVoltage and emgValue2 < self.activationVoltage:
            self.dtoCreator.createActionDto(sensor1, False)
        elif emgValue1 < self.activationVoltage and emgValue2 >= self.activationVoltage:
            self.dtoCreator.createActionDto(sensor2, False)
        elif emgValue1 < self.hysteresisValue and emgValue2 < self.hysteresisValue:
            sensor1.setMotorDirection('s')
            sensor2.setMotorDirection('s')
            self.dtoCreator.createActionDto(sensor1, False)
            self.dtoCreator.createActionDto(sensor2, False)
        else:
            pass

    def getTimeNow(self):
        return time.time_ns() * 1000

    def doubleTension(self, sensor):
        self.dtoCreator.createActionDto(sensor, True)
        sensor.setIsDoubleTensionActivated(True)
        sensor.setPreviousTensionTime(0)
        sensor.setRelaxTime(0)
        sensor.setHasRelaxed(False)

    def resetDoubleTension(self, sensor):
        sensor.setPreviousTensionTime(self.getTimeNow())
        self.dtoCreator.createActionDto(sensor, False)
        sensor.setRelaxTime(0)
        sensor.setIsDoubleTensionActivated(False)

# sensorValues = {1, 2, 3, 4}
# emgReader = FakeAdc(sensorValues)
# transformer = Transformer('testv2_config.ini', emgReader)
# for i in range(len(transformer.sensorList)):

#     motorControlList = transformer.sensorList[i].getSensorsMotorcontrol()
#     actionlist = []
#     for i in range(len(motorControlList)):
#         if (int(motorControlList[i]) == 0):
#             print(motorControlList[i] + '== 0')
#             actionlist.insert(i, 'stop')
#         else:
#             print(motorControlList[i] + '!= 0')
#             actionlist.insert(i, 'start')
#     for i in range(len(actionlist)):
#         print(f'{i}: {actionlist[i]}')
