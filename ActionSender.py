import abc
import serial
import time
from ActionEnum import *
from DTO_Action import *


class IActionSender(abc.ABC):
    @abc.abstractmethod
    def sendAction(self, action: DTO_Action):
        raise NotImplementedError


class ActionSender(IActionSender):
    def __init__(self) -> None:
        self.arduino = serial.Serial('/dev/ttyS0', baudrate=115200, timeout=1)
        #self.arduino = serial.Serial(port='ACM0', baudrate=9600, timeout=1)

    def sendAction(self, action: DTO_Action):
        serializedAction = self.serialiseAction(action)
        print(f'Sending serialized: {serializedAction}')
        self.arduino.write(bytes(serializedAction, 'utf-8'))
        print('moved on')

    def serialiseAction(self, actionslist):
        i = 0
        serialisedAction = ""

        for motoract in actionslist:
            serialisedAction = serialisedAction + \
                str(i+1) + ":" + motoract.value[0] + ","
            i += 1
        serialisedAction = serialisedAction + ">"
        return serialisedAction
