from EmgReader import *
from ActionSender import *
from EmgTransformer import *
from EmgController import *

actionSender = ActionSender()
emgReader = Adc()
configPath = 'config.ini'
transformer = EmgTransformer('pair', emgReader, configPath)

e = EmgController(actionSender, transformer)

while True:
    e.getNewAction()
