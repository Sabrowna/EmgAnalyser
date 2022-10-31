from argparse import Action
import configparser
from ActionEnum import *
import enum
from DTO_Action import DTO_Action
import EmgReader


class EmgTransformer():
    newActionReceived = False

    def __init__(self) -> None:
        self.adc = EmgReader.FakeAdc()
        self.actionEnum = ActionEnum
        self.dtoAction = DTO_Action()

    def openGrip(self):
        self.newActionReceived = True
        print('open')
        return "open"

    def closeGrip(self):
        self.newActionReceived = True
        print('close')
        return "close"

    def getNewAction(self):
        a = EmgReader.Adc()
        adcValues = a.readSensor(2)

        for iteration in range(len(adcValues)):
            if (adcValues[iteration] > 2):
                if (iteration == 0):
                    return self.openGrip()
                elif (iteration == 1):
                    return self.closeGrip()

        # Move to convertToAction()?

        # 1: loop through sensors
        # 2: for each sensor:
        # - How many motors controlling out of 5?
        # - Grip type? open or closing grip?
        # ----------- MISSING ------------
        # Return ActionDTO
        # Check for voltage - if it is +2, startGrip else stopMotor
        # Which sensor has received something?

    def readConfigFile(self):
        configParser = configparser.RawConfigParser()
        configFilePath = r"C:\Users\Bruger\Documents\7. semester\Bachelor\SW\EmgAnalyser\config.txt"
        configParser.read(configFilePath)
        print(configParser)
        return configParser

    def readSensor(self, sensorNum):
        return 'grip'

    def processEmgSignal(grip):
        return 'dto action'

    def createActionDto(self, motorlist):
        motorList = {}
        # Add each motor to one space in an array
        print(motorlist[2])
        motorlist[1]

        motorlistTest = [12345]
        print(split(motorlistTest))

        for i in range(5):
            if (motorlist[i] == 'o'):
                self.dtoAction.actions[i] = self.actionEnum.open
            elif (motorlist[i] == 'c'):
                self.dtoAction.actions[i] = self.actionEnum.close
        return self.dtoAction.actions

    def emgFlowControl(self):
        parser = self.readConfigFile()
        sensorAmount = len(parser.items('sensors'))
        print('sensorAmount: ' + str(sensorAmount))
        emgValues = self.adc.readSensor(sensorAmount)

        # for (sensorNum, motorSettings) in parser.items('sensors'):
        for sensor in range(len(emgValues)):
            if emgValues[sensor] > 2:
                print(str(sensor) + ': ' +
                      str(parser.items('sensors')[sensor]))
                motorSettings = parser.items('sensors')[sensor]
                self.createActionDto(motorSettings)
            else:
                print()
                # check what is the configuration for this specifik sensor and set the dtoActions for that


e = EmgTransformer()
e.emgFlowControl()
