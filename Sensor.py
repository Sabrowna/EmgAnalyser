class Sensor:
    def __init__(self) -> None:
        self.tensionTime = None
        self.relaxTime = None
        self.hasRelaxed = False
        self.direction = None
        self.motorConfig = None

    def getTensionTime(self):
        return self.tensionTime

    def setTensionTime(self, time):
        self.tensionTime = time

    def getRelaxTime(self):
        return self.relaxTime

    def setRelaxTime(self, time):
        self.relaxTime = time

    def getHasRelaxed(self):
        return self.hasRelaxed

    def setHasRelaxed(self, hasRelaxed):
        self.hasRelaxed = hasRelaxed

    def getMotorDirection(self):
        return self.direction

    def setMotorDirection(self, direction):
        self.direction = direction

    def getMotorControlConfig(self):
        return self.motorConfig

    def setMotorControlConfig(self, motorConfig):
        self.motorConfig = motorConfig