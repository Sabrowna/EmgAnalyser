import unittest
from ActionEnum import ActionEnum
from DtoCreator import *


class FakeSensor:
    def __init__(self, controlConfig, motorDirection) -> None:
        self.controlConfig = controlConfig
        self.motorDirection = motorDirection

    def getSensorsMotorcontrol(self):
        return self.controlConfig

    def getMotorDirection(self):
        return self.motorDirection


class DtoCreatorTest(unittest.TestCase):
    def test_actionDto_send1OpenAnd4NaActions_returnSame5Actions(self):
        # Arrange
        actionEnum = ActionEnum
        controlConfig = '10000'
        motorDirection = 'o'
        sensor = FakeSensor(controlConfig, motorDirection)
        dtoCreator = DtoCreator()

        # Act
        dtoCreator.createActionDto(sensor, False)
        result = [actionEnum.open, actionEnum.na,
                  actionEnum.na, actionEnum.na, actionEnum.na]

        # Assert
        self.assertEqual(dtoCreator.getActionDto(), result)

    def test_actionDto_send1CloseAnd4NaActions_returnSame5Actions(self):
        # Arrange
        actionEnum = ActionEnum
        controlConfig = '10000'
        motorDirection = 'c'
        sensor = FakeSensor(controlConfig, motorDirection)
        dtoCreator = DtoCreator()

        # Act
        dtoCreator.createActionDto(sensor, False)
        result = [actionEnum.close, actionEnum.na,
                  actionEnum.na, actionEnum.na, actionEnum.na]

        # Assert
        self.assertEqual(dtoCreator.getActionDto(), result)

    def test_actionDto_send5CloseActions_returnSame5Actions(self):
        # Arrange
        actionEnum = ActionEnum
        controlConfig = '12345'
        motorDirection = 'c'
        sensor = FakeSensor(controlConfig, motorDirection)
        dtoCreator = DtoCreator()

        # Act
        dtoCreator.createActionDto(sensor, False)
        result = [actionEnum.close, actionEnum.close,
                  actionEnum.close, actionEnum.close, actionEnum.close]

        # Assert
        self.assertEqual(dtoCreator.getActionDto(), result)

    def test_actionDto_send5OpenActions_returnSame5Actions(self):
        # Arrange
        actionEnum = ActionEnum
        controlConfig = '12345'
        motorDirection = 'o'
        sensor = FakeSensor(controlConfig, motorDirection)
        dtoCreator = DtoCreator()

        # Act
        dtoCreator.createActionDto(sensor, False)
        result = [actionEnum.open, actionEnum.open,
                  actionEnum.open, actionEnum.open, actionEnum.open]

        # Assert
        self.assertEqual(dtoCreator.getActionDto(), result)

    def test_actionDto_sendCloseActionOnNumber3_Num3IsCloseAction(self):
        # Arrange
        actionEnum = ActionEnum
        controlConfig = '00300'
        motorDirection = 'c'
        sensor = FakeSensor(controlConfig, motorDirection)
        dtoCreator = DtoCreator()

        # Act
        dtoCreator.createActionDto(sensor, False)
        result = [actionEnum.na, actionEnum.na,
                  actionEnum.close, actionEnum.na, actionEnum.na]

        # Assert
        self.assertEqual(dtoCreator.getActionDto(), result)

    def test_actionDto_sendCloseActionOnNumber3And4_Num3And4IsCloseAction(self):
        # Arrange
        actionEnum = ActionEnum
        controlConfig = '00340'
        motorDirection = 'c'
        sensor = FakeSensor(controlConfig, motorDirection)
        dtoCreator = DtoCreator()

        # Act
        dtoCreator.createActionDto(sensor, False)
        result = [actionEnum.na, actionEnum.na,
                  actionEnum.close, actionEnum.close, actionEnum.na]

        # Assert
        self.assertEqual(dtoCreator.getActionDto(), result)


if __name__ == '__main__':
    unittest.main()
