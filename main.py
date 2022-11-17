from EmgReader import *
from ActionSender import *
from EmgTransformer import *
from EmgController import *

emgReader = Adc('ads1115')
actionSender = ActionSender()
configPath = 'config.ini'
transformer = EmgTransformer('pair', emgReader, configPath)


e = EmgController(actionSender, transformer)

while True:
    e.getNewAction()