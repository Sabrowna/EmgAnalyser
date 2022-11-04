class PseudoClass():
    def __init__(self) -> None:
        pass
        # Initalizing adc
        # Initializing actionEnum
        # Initializing dtoAction
        # Read configuration file and set self.config + sensorAmount
        # Define either pairedSensor-method or SingleSensor-method

    def readConfigFile(self):
        pass
        # read file from a path (not from a specifik user on specifik pc)
        # return object containing the file

    def createActionDto(self, motorDirection, motorRange):
        pass
        # for motor in range(motorRange):
        # if (motorDirection == 'o')
        #self.dtoAction.actions[motor] = self.actionEnum.open
        # elif (motorDirection == 'c')
        #self.dtoAction.actions[motor] = self.actionEnum.close
        # elif (motorDirection == 's')
        #self.dtoAction.actions[motor] = self.actionEnum.stop
        # return self.dtoAction.actions

    def handlePairedSensorValues(self):
        pass
        # read sensor values
        #emgValues = self.adc.readSensor(self.sensorAmount)
        # Iterate over every 2nd sensor

        # for sensor in range(len(emgValues))
        # if the value of sensor 1 and 2 both are > 2
        # Do nothing
        # elif the value is > 2
        #createActionDto(config.direction, motorRange)
        # example open motor 1, 2, 3
        # elif the value is < 2
        #createActionDto(stop, motorRange)
        # example stop motor 1, 2, 3123

    def handleSingleSensorValues(self):
        pass
        # elif the value is > 2
        #createActionDto(open/close, motorRange)
        # example open motor 1, 2, 3
        # elif the value is < 2
        #createActionDto(stop, motorRange)
        # example stop motor 1, 2, 3
