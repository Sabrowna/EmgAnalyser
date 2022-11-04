from ActionSender import *
from EmgReader import *
from EmgTransformer import EmgTransformer


class EmgController():
    def __init__(self, actionSender: IActionSender, adc: IEmgReader, configPath) -> None:
        self.lastgrip = 'stop'
        self.actionSender = actionSender
        self.emgTransformer = EmgTransformer('pair', adc, configPath)

    def getNewAction(self):
        while True:
            grip = self.emgTransformer.handleSensorValues()
            if (grip != None):
                if (self.lastgrip != grip):
                    print('new grip registered')
                    print(grip)
                    self.actionSender.sendAction(grip)
                    break


#sensorValues = {0: 2.25, 1: 0.99, 2: 2.63, 3: 0.95}
sensorValues = {0: 2.25, 1: 0.99}
actionSender = FakeActionSender()
emgReader = FakeAdc(sensorValues)

configPath = 'testconfig.ini'
e = EmgController(actionSender, emgReader, configPath)
e.getNewAction()
