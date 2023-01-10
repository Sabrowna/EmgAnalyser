print("line1 main")
from EmgReader import *
from ActionSender import *
from Transformer import *
from EmgController import *

print("line7 main")
emgReader = Adc('ads1115')
actionSender = ActionSender()
configPath = 'config.ini'
transformer = Transformer(configPath, emgReader)


print("line14 main")
e = EmgController(actionSender, transformer)
counter = 0
while True:
    if counter == 100:
        counter = 0
        print("while true")
    e.getNewAction()
    counter += 1
