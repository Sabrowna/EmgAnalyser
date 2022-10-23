import configparser
# from ActionSender import ActionSender
from EmgTransformer import EmgTransformer
import ActionEnum
import DTO_Action


class EmgController():
    # def __init__(self) -> None:
    #     # Fake code
    #     sensors = {
    #         'sensor0': 3,
    #         'sensor1': {'motors': [1, 2, 3, 4, 5],
    #                     'gripMove': 'e'},
    #         'sensor2': {'motors': [1, 2, 3, 4, 5],
    #                     'gripMove': 'f'}}

    #     self.length = len(sensors)
    #     print('length: ' + str(self.length))

    #     # Testing fake code
    #     print(sensors['sensor2'])
    #     print(sensors['sensor2']['motors'])
    #     print(sensors['sensor2']['motors'][0])
    #     print(sensors['sensor2']['gripMove'])

    # TODO This one needs to be implemented
    def readConfigFile():
        configParser = configparser.RawConfigParser()
        configFilePath = r"C:\Users\Bruger\Documents\7. semester\Bachelor\SW\EmgAnalyser\config.txt"
        configParser.read(configFilePath)

        sensorAmount = configParser.get('system', 'sensors')
        adcAmount = configParser.get('system', 'adc')
        return sensorAmount, adcAmount

    def setLength(self, length):
        self.length = length

    def getLength(self):
        return self.length

    def getAdc(self):
        self.adc = Adc()
        return self.adc

    def getNewAction(self):
        # TODO I should pass on the number of channels from this method
        lastGrip = EmgTransformer().getNewAction()
        while True:
            grip = EmgTransformer().getNewAction()
            if (grip != None and lastGrip != None):
                if (lastGrip != grip):
                    print('new grip registered')
                    self.matchCommand(grip)
                    break
                lastGrip = grip

    def matchCommand(self, grip):
        # myDTO = DTO_Action()
        # a = ActionSender()

        match grip:
            case "open":
                theEnum = ActionEnum.ActionEnum.open
            case "close":
                theEnum = ActionEnum.ActionEnum.close
            case "stop":
                theEnum = ActionEnum.ActionEnum.stop
            case "na":
                theEnum = ActionEnum.ActionEnum.na

        for i in range(2):
            DTO_Action.DTO_Action.actions[i] = theEnum
        for i in range(2, 5):
            DTO_Action.DTO_Action.actions[i] = ActionEnum.ActionEnum.na
        print('sending dto enum ')
        print(DTO_Action.DTO_Action.actions)
        # a.sendAction(myDTO)
        # ActionSender.sendAction(myDTO)


e = EmgController()
e.getNewAction()
