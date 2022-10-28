import configparser
from nntplib import GroupInfo
import EmgReader


class EmgTransformer():
    newActionReceived = False

    def __init__(self) -> None:
        self.adc = EmgReader.Adc()

    def openGrip(self):
        self.newActionReceived = True
        print('open')
        return "open"

    def closeGrip(self):
        self.newActionReceived = True
        print('close')
        return "close"

    def getNewAction(self):
        a = EmgReader.Adc()
        adcValues = a.readSensor(2)

        for iteration in range(len(adcValues)):
            if (adcValues[iteration] > 2):
                if (iteration == 0):
                    return self.openGrip()
                elif (iteration == 1):
                    return self.closeGrip()

        # Move to convertToAction()?

    def convertGripToActions(self, voltage):
        # 1: loop through sensors
        # 2: for each sensor:
        # - How many motors controlling out of 5?
        # - Grip type? open or closing grip?
        # ----------- MISSING ------------
        # Return ActionDTO
        # Check for voltage - if it is +2, startGrip else stopMotor
        # Which sensor has received something?

        # Reading the file by using a parser
        configParser = configparser.RawConfigParser()
        configFilePath = r"C:\Users\Bruger\Documents\7. semester\Bachelor\SW\EmgAnalyser\config.txt"
        configParser.read(configFilePath)

        # list of actions
        actionlist = []

        # looping through each line in the [sensors] section (all sensors)
        for (sensor, motorControlling) in configParser.items('sensors'):
            print(sensor + ': ' + motorControlling)
            motorlist = motorControlling
            gripType = motorlist[len(motorlist) - 1]

            actionlist.clear()

            # looping through 5 times, one for each motor
            for i in range(1, 6):
                if (int(motorlist[i-1]) == i):
                    actionlist.append(gripType)
                else:
                    actionlist.append('na')

            print('actionlist: ' + str(actionlist))


e = EmgTransformer()
e.convertGripToActions(2)


# read config file
# read all adcs
# if the value from adc is higher than 2
# which sensor are we talking about?
# Is it an opening or closing action?
# How many motors?
# Put it into an action form


def readConfigFile():
    return 'configObj'


def readSensor(self, sensorNum):
    return 'grip'


def processEmgSignal(grip):
    return 'dto action'
