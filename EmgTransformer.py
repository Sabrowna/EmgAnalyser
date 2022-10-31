import configparser
from ActionEnum import ActionEnum
import EmgReader
from DTO_Action import DTO_Action


class EmgTransformer():
    def __init__(self, sensorMethod, adcType) -> None:
        self.adcType = adcType
        self.adc = EmgReader.FakeAdc()
        self.actionEnum = ActionEnum
        self.dtoAction = DTO_Action()
        self.config = self.readConfigFile()
        self.sensorAmount = len(self.config.items('sensors'))
        self.sensorMethod = sensorMethod

    def readConfigFile(self):
        config = configparser.RawConfigParser()
        config.read('config.ini')
        return config

    def getRange(self, motorSetting):
        tempList = []
        for i in range(len(motorSetting)):
            if (motorSetting[i] != '0'):
                tempList.append(i)
        return tempList

    def createActionDto(self, motorDirection, motorRange):
        for motor in range(len(motorRange)-1):
            print(f'motordirection: {motorDirection}')
            if (motorDirection == 'o'):
                print('equals o')
                self.dtoAction.actions[motorRange[motor]
                                       ] = self.actionEnum.open
            elif (motorDirection == 'c'):
                print('equals c')
                self.dtoAction.actions[motorRange[motor]
                                       ] = self.actionEnum.close
            elif (motorDirection == 's'):
                print('equals s')
                self.dtoAction.actions[motorRange[motor]
                                       ] = self.actionEnum.stop
        print(self.dtoAction.actions)
        return self.dtoAction.actions

    def handlePairedSensorValues(self):
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
                print('1st sensor active')
                motorDirection = sensors[i][1][-1]
                motorRange = self.getRange(((sensors)[i][1]))

            # 2nd sensor in the pair is active
            elif emgValues[i+1] > 2 and emgValues[i] < 2:
                print('2nd sensor active')
                motorDirection = sensors[i+1][1][-1]
                motorRange = self.getRange(((sensors)[i+1][1]))
            elif emgValues[i] < 2 and emgValues[i+1] < 2:
                print('no sensors active')
                motorDirection = 's'
                motorRange = self.getRange(((sensors)[i][1]))

        self.createActionDto(motorDirection, motorRange)

    def handleSingleSensorValues(self):
        print('single sensor value method')
        # elif the value is > 2
        # createActionDto(open/close, motorRange)
        # example open motor 1, 2, 3
        # elif the value is < 2
        # createActionDto(stop, motorRange)
        # example stop motor 1, 2, 3


e = EmgTransformer('pair', 'fakeAdc')
e.readConfigFile()
e.handlePairedSensorValues()
