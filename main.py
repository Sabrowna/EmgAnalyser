# from EmgReader import *
# from ActionSender import *
from Test_Fakes import *
from EmgTransformer import *
from EmgController import *

sensorValues = {0: 1.33, 1: 2.45, 2: 0.25, 3: 2.53}
actionSender = FakeActionSender()
emgReader = FakeAdc(sensorValues)
configPath = 'config.ini'
transformer = EmgTransformer('pair', emgReader, configPath)

e = EmgController(actionSender, transformer)

while True:
    e.getNewAction()
