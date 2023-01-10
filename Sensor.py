class Sensor:
    def __init__(self) -> None:
        self.previousTensionTime = 0
        self.relaxTime = 0.0
        self.hasRelaxed = False
        self.direction = None
        self.motorConfig = None
        self.isDoubleTensionActivated = False
        self.isActive = True

    def setPreviousTensionTime(self, time):
        self.previousTensionTime = time

    def getPreviousTensionTime(self):
        return self.previousTensionTime

    def setIsDoubleTensionActivated(self, isDoubleTensionActivated):
        self.isDoubleTensionActivated = isDoubleTensionActivated

    def getIsDoubleTensionActivated(self):
        return self.isDoubleTensionActivated

    def getRelaxTime(self):
        return self.relaxTime

    def setRelaxTime(self, time: float):
        self.relaxTime = time

    def getHasRelaxed(self):
        return self.hasRelaxed

    def setHasRelaxed(self, hasRelaxed):
        self.hasRelaxed = hasRelaxed

    def getMotorDirection(self):
        return self.direction

    def setMotorDirection(self, direction):
        self.direction = direction

    def getSensorsMotorcontrol(self):
        return self.motorConfig

    def setSensorsMotorcontrol(self, motorConfig):
        self.motorConfig = motorConfig

    def getIsActive(self):
        return self.isActive

    def setIsActive(self, isActive):
        self.isActive = isActive
