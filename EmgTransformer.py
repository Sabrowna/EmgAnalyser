import EmgReader


class EmgTransformer():
    newActionReceived = False

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
