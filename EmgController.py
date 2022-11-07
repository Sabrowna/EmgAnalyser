from ActionSender import IActionSender
from EmgTransformer import ITransformer
from DTO_Action import *


class EmgController():
    def __init__(self, actionSender: IActionSender, transformer: ITransformer) -> None:
        dto = DTO_Action()
        self.lastgrip = dto.actions
        print(self.lastgrip)
        self.actionSender = actionSender
        self.emgTransformer = transformer
        self.sameGripRegistered = True

    def getNewAction(self):
        grip = self.emgTransformer.handleSensorValues()
        if (grip != None):
            if (self.lastgrip != grip):
                print('new grip registered')
                print(grip)
                self.actionSender.sendAction(grip)
