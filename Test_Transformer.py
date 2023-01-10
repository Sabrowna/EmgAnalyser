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
        transformer = Transformer('test1_config.ini', emgReader)

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
        transformer = Transformer('test1_config.ini', emgReader)
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
        transformer = Transformer('test2_config.ini', emgReader)

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
        transformer = Transformer('test2_config.ini', emgReader)

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
        transformer = Transformer('test2_config.ini', emgReader)

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

    def test_doubleTension_highHighOnSensor1_dtoOpensMotor1(self):
        # Arrange
        sensor = Sensor()
        enum = ActionEnum
        emgReader = FakeEmgReader()
        emgReader.setEmgValues([2, 0, 0, 0])
        transformer = Transformer('test2_config.ini', emgReader)

        # Act
        transformer.observeSensors()
        time.sleep(1)
        emgReader.setEmgValues([2, 0, 0, 0])
        result = transformer.observeSensors()

        expected = [enum.open, enum.stop, enum.stop, enum.stop, enum.stop]

        # Assert
        self.assertEqual(
            expected, result)

    def test_doubleTension_highManyTimesOnSensor1_dtoOpensMotor1(self):
        # Arrange
        sensor = Sensor()
        enum = ActionEnum
        emgReader = FakeEmgReader()
        emgReader.setEmgValues([2, 0, 0, 0])
        transformer = Transformer('test2_config.ini', emgReader)

        # Act
        transformer.observeSensors()
        time.sleep(1)
        for i in range(10):
            emgReader.setEmgValues([2, 0, 0, 0])
            transformer.observeSensors()

        result = transformer.observeSensors()

        expected = [enum.open, enum.stop, enum.stop, enum.stop, enum.stop]

        # Assert
        self.assertEqual(
            expected, result)

    def test_doubleTension_highLowHighOnSensor1_dtoClosesMotor1(self):
        # Arrange
        sensor = Sensor()
        enum = ActionEnum
        emgReader = FakeEmgReader()
        emgReader.setEmgValues([2, 0, 0, 0])
        transformer = Transformer('test2_config.ini', emgReader)

        # Act
        transformer.observeSensors()
        emgReader.setEmgValues([0, 0, 0, 0])
        transformer.observeSensors()
        emgReader.setEmgValues([2, 0, 0, 0])
        result = transformer.observeSensors()

        expected = [enum.close, enum.stop, enum.stop, enum.stop, enum.stop]

        # Assert
        self.assertEqual(
            expected, result)

    def test_doubleTension_highLowHighWithSleepOnSensor1_dtoClosesMotor1(self):
        # Arrange
        sensor = Sensor()
        enum = ActionEnum
        emgReader = FakeEmgReader()
        emgReader.setEmgValues([2, 0, 0, 0])
        transformer = Transformer('test2_config.ini', emgReader)

        # Act
        transformer.observeSensors()
        time.sleep(0.5)
        emgReader.setEmgValues([0, 0, 0, 0])
        transformer.observeSensors()
        time.sleep(0.5)
        emgReader.setEmgValues([2, 0, 0, 0])
        result = transformer.observeSensors()

        expected = [enum.close, enum.stop, enum.stop, enum.stop, enum.stop]

        # Assert
        self.assertEqual(
            expected, result)

    def test_doubleTension_highLowHighWithTooMuchSleepOnSensor1_dtoOpensMotor1(self):
        # Arrange
        sensor = Sensor()
        enum = ActionEnum
        emgReader = FakeEmgReader()
        emgReader.setEmgValues([2, 0, 0, 0])
        transformer = Transformer('test2_config.ini', emgReader)

        # Act
        transformer.observeSensors()
        emgReader.setEmgValues([0, 0, 0, 0])
        time.sleep(1.5)
        transformer.observeSensors()
        emgReader.setEmgValues([2, 0, 0, 0])
        result = transformer.observeSensors()

        expected = [enum.stop, enum.stop, enum.stop, enum.stop, enum.stop]

        # Assert
        self.assertEqual(
            expected, result)

    def test_doubleTension_highLowHighWithTooMuchSleepOnSensor1GoHigh_dtoOpensMotor1(self):
        # Arrange
        sensor = Sensor()
        enum = ActionEnum
        emgReader = FakeEmgReader()
        emgReader.setEmgValues([2, 0, 0, 0])
        transformer = Transformer('test2_config.ini', emgReader)

        # Act
        transformer.observeSensors()
        emgReader.setEmgValues([0, 0, 0, 0])
        time.sleep(1.5)
        transformer.observeSensors()
        emgReader.setEmgValues([2, 0, 0, 0])
        transformer.observeSensors()
        time.sleep(1)
        result = transformer.observeSensors()

        expected = [enum.open, enum.stop, enum.stop, enum.stop, enum.stop]

        # Assert
        self.assertEqual(
            expected, result)

    def test_doubleTension_highLowHighManyTimesOnSensor1_dtoClosesMotor1(self):
        # Arrange
        sensor = Sensor()
        enum = ActionEnum
        emgReader = FakeEmgReader()
        emgReader.setEmgValues([2, 0, 0, 0])
        transformer = Transformer('test2_config.ini', emgReader)

        # Act
        transformer.observeSensors()
        time.sleep(0.5)
        emgReader.setEmgValues([0, 0, 0, 0])
        transformer.observeSensors()
        time.sleep(0.5)
        emgReader.setEmgValues([2, 0, 0, 0])
        for i in range(10):
            transformer.observeSensors()

        result = transformer.observeSensors()

        expected = [enum.close, enum.stop, enum.stop, enum.stop, enum.stop]

        # Assert
        self.assertEqual(
            expected, result)


if __name__ == '__main__':
    unittest.main()
