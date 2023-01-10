from ActionSender import IActionSender
from Transformer import ITransformer
from DTO_Action import *


class EmgController():
    def __init__(self, actionSender: IActionSender, transformer: ITransformer) -> None:
        dto = DTO_Action()
        self.lastgrip = dto.actions
        self.actionSender = actionSender
        self.emgTransformer = transformer
        self.sameGripRegistered = True
        print("initialized in controller")

    def getNewAction(self):
        grip = self.emgTransformer.observeSensors()
        if (grip != None):
            if (self.lastgrip != grip):
                print('new grip registered')
                print(f'lastgrip: {self.lastgrip}')
                print(f'grip: {grip}')
                self.lastgrip = grip.copy()
                self.actionSender.sendAction(grip)
