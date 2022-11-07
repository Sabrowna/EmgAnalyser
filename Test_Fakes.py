from EmgReader import IEmgReader
from ActionSender import IActionSender
from EmgTransformer import ITransformer
from DTO_Action import *
import configparser


class FakeAdc(IEmgReader):
    def __init__(self, sensorValues) -> None:
        self.sensors = sensorValues

    def readSensor(self, channelAmount):
        emgValuesDict = {}
        emgValuesDict.clear()

        for channel in range(channelAmount):
            emgInVoltage = self.sensors[channel]
            emgValuesDict[channel] = emgInVoltage
        print('dict: ' + str(emgValuesDict))
        return emgValuesDict


class FakeActionSender(IActionSender):
    def __init__(self) -> None:
        self.amount = 0

    def sendAction(self, grip):
        self.amount += 1

    def getActionCalls(self):
        return self.amount


class FakeTransformer(ITransformer):
    def setDto(self, dto: DTO_Action):
        self.dto = dto

    def handleSensorValues(self):
        return self.dto.actions
