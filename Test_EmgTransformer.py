import unittest
import EmgTransformer
from EmgReader import *
from ActionEnum import ActionEnum
from DTO_Action import DTO_Action
from Test_Fakes import *


class TransformerTest(unittest.TestCase):
    # Naming convention: test_<testmethod>_<doing>_<expected result>
    def test_handleSensorValues_sendingClose2sensors_CloseActions(self):
        # In order to receive close, sensor 2 must send over 2V and sensor 1 should send under 2V

        # Arrange
        configPath = 'test_2sensors.ini'
        sensorValues = {0: 0.01, 1: 2.53}
        enum = ActionEnum
        dto = DTO_Action()

        emgReader = FakeAdc(sensorValues)
        transformer = EmgTransformer.EmgTransformer(
            'pair', emgReader, configPath)

        # Act
        result = transformer.handleSensorValues()
        dto.actions[0] = enum.close
        dto.actions[1] = enum.close
        dto.actions[2] = enum.close
        dto.actions[3] = enum.stop
        dto.actions[4] = enum.stop

        # Assert
        self.assertEqual(result, dto.actions)

    def test_handleSensorValues_sendingClose0sensors_defaultAction(self):
        # What happens when no sensors is received from config

        # Arrange
        configPath = 'test_0sensors.ini'
        sensorValues = {0: 0.01, 1: 2.53}
        emgReader = FakeAdc(sensorValues)
        transformer = EmgTransformer.EmgTransformer(
            'pair', emgReader, configPath)
        enum = ActionEnum
        dto = DTO_Action()
        dto.actions[0] = enum.stop
        dto.actions[1] = enum.stop
        dto.actions[2] = enum.stop
        dto.actions[3] = enum.stop
        dto.actions[4] = enum.stop

        # Act
        result = transformer.handleSensorValues()

        # Assert
        self.assertEqual(result, dto.actions)

    def test_handleSensorValues_sendingValuesUnder2V_defaultAction(self):
        # What happens when no sensors is received from config

        # Arrange
        configPath = 'test_2sensors.ini'
        sensorValues = {0: 0.01, 1: 1.53}
        enum = ActionEnum
        dto = DTO_Action()

        emgReader = FakeAdc(sensorValues)
        transformer = EmgTransformer.EmgTransformer(
            'pair', emgReader, configPath)

        # Act
        result = transformer.handleSensorValues()
        dto.actions[0] = enum.stop
        dto.actions[1] = enum.stop
        dto.actions[2] = enum.stop
        dto.actions[3] = enum.stop
        dto.actions[4] = enum.stop

        # Assert
        self.assertEqual(result, dto.actions)

    def test_handleSensorValues_sendingValuesOver2V_defaultAction(self):
        # What happens when no sensors is received from config

        # Arrange
        configPath = 'test_2sensors.ini'
        sensorValues = {0: 2.01, 1: 2.53}
        enum = ActionEnum
        dto = DTO_Action()

        emgReader = FakeAdc(sensorValues)
        transformer = EmgTransformer.EmgTransformer(
            'pair', emgReader, configPath)

        # Act
        result = transformer.handleSensorValues()
        dto.actions[0] = enum.stop
        dto.actions[1] = enum.stop
        dto.actions[2] = enum.stop
        dto.actions[3] = enum.stop
        dto.actions[4] = enum.stop

        # Assert
        self.assertEqual(result, dto.actions)

    def test_handleSensorValues_sendingOpenValues_Open(self):
        # What happens when no sensors is received from config

        # Arrange
        configPath = 'test_2sensors.ini'
        sensorValues = {0: 2.01, 1: 0.53}
        enum = ActionEnum
        dto = DTO_Action()

        emgReader = FakeAdc(sensorValues)
        transformer = EmgTransformer.EmgTransformer(
            'pair', emgReader, configPath)

        # Act
        result = transformer.handleSensorValues()
        dto.actions[0] = enum.open
        dto.actions[1] = enum.open
        dto.actions[2] = enum.open
        dto.actions[3] = enum.stop
        dto.actions[4] = enum.stop

        # Assert
        self.assertEqual(result, dto.actions)

    def test_handleSensorValues_4sensors_OpenOpen(self):
        # What happens when no sensors is received from config

        # Arrange
        configPath = 'test_4sensors.ini'
        sensorValues = {0: 2.01, 1: 0.53, 2: 2.01, 3: 0.53}
        enum = ActionEnum
        dto = DTO_Action()

        emgReader = FakeAdc(sensorValues)
        transformer = EmgTransformer.EmgTransformer(
            'pair', emgReader, configPath)

        # Act
        result = transformer.handleSensorValues()
        dto.actions[0] = enum.open
        dto.actions[1] = enum.open
        dto.actions[2] = enum.open
        dto.actions[3] = enum.stop
        dto.actions[4] = enum.close

        print('result: ' + str(result))
        print('actions: ' + str(dto.actions))

        # Assert
        self.assertEqual(result, dto.actions)


        # open, close metoder
        # not applicable
        # for mange sensorer?
        # ------------------ Andre tests ----------------
        # sender kun når der modtages nyt greb
        # Errors
        # serialiserer korrekt
        # error handling on uneven sensornumbers
if __name__ == '__main__':
    unittest.main()
