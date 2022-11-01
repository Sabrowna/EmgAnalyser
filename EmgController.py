from ActionSender import ActionSender
from EmgTransformer import EmgTransformer


class EmgController():
    def __init__(self) -> None:
        self.lastgrip = 'stop'
        self.actionSender = ActionSender()
        self.emgTransformer = EmgTransformer('pair', 'fakeadc')

    def getNewAction(self):
        while True:
            grip = self.emgTransformer.handleSensorValues()
            if (grip != None):
                if (self.lastgrip != grip):
                    print('new grip registered')
                    print(grip)
                    self.actionSender.sendAction(grip)
                    break


e = EmgController()
e.getNewAction()
