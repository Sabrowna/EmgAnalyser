import abc
import configparser
from ActionEnum import ActionEnum
from EmgReader import IEmgReader
from DTO_Action import DTO_Action


class ITransformer(abc.ABC):
    @abc.abstractmethod
    def handleSensorValues(self):
        raise NotImplementedError


class EmgTransformer(ITransformer):
    def __init__(self, sensorMethod, adc: IEmgReader, configPath) -> None:
        self.configpath = configPath
        self.adc = adc
        self.actionEnum = ActionEnum
        self.dtoAction = DTO_Action()
        self.config = self.__readConfigFile()
        self.sensorAmount = len(self.config.items('sensors'))
        self.sensorMethod = sensorMethod

    def __readConfigFile(self):
        config = configparser.RawConfigParser()
        config.read(self.configpath)
        return config

    def __getRange(self, motorSetting):
        tempList = []
        for i in range(len(motorSetting)):
            if (motorSetting[i] != '0'):
                tempList.append(i)
        return tempList

    def __createActionDto(self, motorDirection, motorRange):
        for motor in range(len(motorRange)-1):
            if (motorDirection == 'o'):
                self.dtoAction.actions[motorRange[motor]
                                       ] = self.actionEnum.open
            elif (motorDirection == 'c'):
                self.dtoAction.actions[motorRange[motor]
                                       ] = self.actionEnum.close
            elif (motorDirection == 's'):
                self.dtoAction.actions[motorRange[motor]
                                       ] = self.actionEnum.stop
        return self.dtoAction.actions

    def __handlePairedSensorValues(self):
        emgValues = self.adc.readSensor(self.sensorAmount)

        # running in the range of sensorAmounts, with a step of 2
        # Doesn't take the last argument, since it is a letter (o or c)
        for i in range(0, len(emgValues)-1, 2):
            sensors = self.config.items('sensors')

            # i defines which sensor
            if emgValues[i] > 2 and emgValues[i+1] > 2:
                # Do nothing if both sensors in a pair is active
                break

            # 1st sensor in the pair is active
            elif emgValues[i] > 2 and emgValues[i + 1] < 2:
                motorDirection = sensors[i][1][-1]
                motorRange = self.__getRange(((sensors)[i][1]))

            # 2nd sensor in the pair is active
            elif emgValues[i+1] > 2 and emgValues[i] < 2:
                motorDirection = sensors[i+1][1][-1]
                motorRange = self.__getRange(((sensors)[i+1][1]))
            elif emgValues[i] < 2 and emgValues[i+1] < 2:
                motorDirection = 's'
                motorRange = self.__getRange(((sensors)[i][1]))
            self.__createActionDto(motorDirection, motorRange)
        print(self.dtoAction.actions)
        return self.dtoAction.actions

    def __handleSingleSensorValues(self):
        print('single sensor value method')
        # if the value is > 2
        #   createActionDto(open/close, motorRange)
        #   example open motor 1, 2, 3
        # elif the value is < 2
        #   createActionDto(stop, motorRange)
        #   example stop motor 1, 2, 3

    def handleSensorValues(self):
        if (self.sensorMethod == 'pair'):
            # if (self.sensorAmount % 2 != 0):
            #     print(f'uneven sensor number ({self.sensorAmount})')
            #     try:
            #         return self.__handlePairedSensorValues()
            #     except ValueError:
            #         print(
            #             f'The number of sensors is uneven. \nThere might be a mistake in the {self.configPath} either with the amount of sensors or the chosen method ')
            return self.__handlePairedSensorValues()
        elif (self.sensorMethod == 'single'):
            return self.__handleSingleSensorValues()
# e = EmgTransformer('pair', 'fakeAdc')
# e.readConfigFile()
# e.handlePairedSensorValues()
