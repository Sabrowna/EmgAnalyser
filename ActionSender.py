import abc
import serial
import time
from ActionEnum import *
from DTO_Action import *


class IActionSender(abc.ABC):
    @abc.abstractmethod
    def sendAction():
        pass


class ActionSender(IActionSender):
    def __init__(self) -> None:
        pass
        self.arduino = serial.Serial(port='COM7', baudrate=9600, timeout=.1)

    def sendAction(self, action: DTO_Action):
        serializedAction = self.serialiseAction(action)
        print(serializedAction)
        self.arduino.write(bytes(serializedAction, 'utf-8'))

    def serialiseAction(self, dto_action: DTO_Action):
        i = 0
        serialisedAction = ""

        for motoract in dto_action.actions:
            serialisedAction = serialisedAction + \
                str(i+1) + ":" + motoract.value[0] + ","
            i += 1
        serialisedAction = serialisedAction + ">"
        return serialisedAction


a = ActionSender()
myDTO = DTO_Action()
theEnum = ActionEnum
while True:
    print("Enter 5 new commands to fill up new dto")
    for i in range(5):
        command = input("Enter command " + str(i+1) + " :")
        match command:
            case "open":
                theEnum = ActionEnum.open
            case "close":
                theEnum = ActionEnum.close
            case "stop":
                theEnum = ActionEnum.stop
            case "na":
                theEnum = ActionEnum.na
        myDTO.actions[i] = theEnum
    a.sendAction(myDTO)
