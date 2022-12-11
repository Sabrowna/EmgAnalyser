import unittest
from Transformer import *
from ActionEnum import ActionEnum
from Sensor import *


class FakeEmgReader():
    def readSensor(self, channelAmount):
        return self.emgValuesDict

    def setEmgValues(self, values):
        self.emgValuesDict = values


class TestTransformer(unittest.TestCase):
    def test_singleTensionOneValuesActiveCallAgain2ValuesActive_returnOpenAndStop(self):
        # Arrange
        actionEnum = ActionEnum
        emgReader = FakeEmgReader()
        emgReader.setEmgValues([2, 0, 2, 0])
        transformer = Transformer('testv2_config.ini', emgReader)

        # Act
        actionDto = transformer.observeSensors()
        result = [actionEnum.open, actionEnum.open,
                  actionEnum.stop, actionEnum.stop, actionEnum.stop]

        # Assert
        self.assertEqual(actionDto, result)

    def test_hysteresistest_NotStopping(self):
        # Arrange
        actionEnum = ActionEnum
        emgReader = FakeEmgReader()
        transformer = Transformer('testv2_config.ini', emgReader)
        emgReader.setEmgValues([0, 2, 0, 2])

        # Act
        actionDto = transformer.observeSensors()
        emgReader.setEmgValues([0, 1.5, 0, 0])
        actionDto = transformer.observeSensors()

        result = [actionEnum.close, actionEnum.stop,
                  actionEnum.stop, actionEnum.stop, actionEnum.stop]

        # Assert
        self.assertEqual(actionDto, result)

    # Sometimes succeeds, sometimes fails. Depends on how much time the PC uses to run the method.
    def test_doubleTension_tensionAndRelax_hasRelaxedIsTrue(self):
        # Arrange
        sensor = Sensor()
        emgReader = FakeEmgReader()
        emgReader.setEmgValues([2, 0, 0, 0])
        transformer = Transformer('testv3_config.ini', emgReader)

        # Act
        transformer.observeSensors()
        emgReader.setEmgValues([0, 0, 0, 0])
        transformer.observeSensors()
        result = True

        # Assert
        self.assertEqual(result, transformer.sensorList[0].getHasRelaxed())

    def test_doubleTension_tensionAndRelaxAndTension_TensionActivatedIsTrue(self):
        # Arrange
        sensor = Sensor()
        emgReader = FakeEmgReader()
        emgReader.setEmgValues([2, 0, 0, 0])
        transformer = Transformer('testv3_config.ini', emgReader)

        # Act
        transformer.observeSensors()
        emgReader.setEmgValues([0, 0, 0, 0])
        transformer.observeSensors()
        emgReader.setEmgValues([2, 0, 0, 0])
        transformer.observeSensors()

        result = True

        # Assert
        self.assertEqual(
            result, transformer.sensorList[0].getIsDoubleTensionActivated())

    def test_doubleTension_tensionAndRelaxAndTensionAndRelaxLong_TensionActivatedIsFalse(self):
        # Arrange
        sensor = Sensor()
        emgReader = FakeEmgReader()
        emgReader.setEmgValues([2, 0, 0, 0])
        transformer = Transformer('testv3_config.ini', emgReader)

        # Act
        transformer.observeSensors()
        emgReader.setEmgValues([0, 0, 0, 0])
        transformer.observeSensors()
        emgReader.setEmgValues([2, 0, 0, 0])
        transformer.observeSensors()
        emgReader.setEmgValues([0, 0, 0, 0])
        transformer.observeSensors()
        time.sleep(2)
        transformer.observeSensors()

        result = False

        # Assert
        self.assertEqual(
            result, transformer.sensorList[0].getIsDoubleTensionActivated())


if __name__ == '__main__':
    unittest.main()
