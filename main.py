from EmgReader import *
from ActionSender import *
from Transformer import *
from EmgController import *

emgReader = Adc('ads1115')
actionSender = ActionSender()
configPath = 'config.ini'
transformer = Transformer(configPath, emgReader)


e = EmgController(actionSender, transformer)

while True:
    e.getNewAction()
