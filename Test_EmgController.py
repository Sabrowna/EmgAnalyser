import unittest
from EmgController import EmgController
from EmgReader import *
from ActionEnum import ActionEnum
from DTO_Action import DTO_Action
from ActionSender import *
from Test_Fakes import *


class ControllerTest(unittest.TestCase):
    def test_getNewAction_sendSameGrip_NoAction(self):
        # Arrange
        transformer = FakeTransformer()
        actionSender = FakeActionSender()
        controller = EmgController(actionSender, transformer)

        enum = ActionEnum
        dto0 = DTO_Action()
        dto0.actions[0] = enum.stop
        dto0.actions[1] = enum.stop
        dto0.actions[2] = enum.stop
        dto0.actions[3] = enum.stop
        dto0.actions[4] = enum.stop

        # Act
        transformer.setDto(dto0)
        controller.getNewAction()
        result = actionSender.amount

        # Assert
        self.assertEqual(result, 0)

    def test_getNewAction_send1NewGrip_ActionSenderCalled1Time(self):
        # Arrange
        enum = ActionEnum
        dto1 = DTO_Action()

        dto1.actions[0] = enum.open
        dto1.actions[1] = enum.open
        dto1.actions[2] = enum.open
        dto1.actions[3] = enum.close
        dto1.actions[4] = enum.close

        transformer = FakeTransformer()
        actionSender = FakeActionSender()
        controller = EmgController(actionSender, transformer)

        # Act
        transformer.setDto(dto1)
        controller.getNewAction()
        result = actionSender.amount

        # Assert
        self.assertEqual(result, 1)

    def test_getNewAction_send2NewGrips_ActionSenderCalled2Times(self):
        # Arrange
        enum = ActionEnum
        dto1 = DTO_Action()
        dto2 = DTO_Action()

        dto1.actions[0] = enum.open
        dto1.actions[1] = enum.open
        dto1.actions[2] = enum.open
        dto1.actions[3] = enum.close
        dto1.actions[4] = enum.close

        dto2.actions[0] = enum.open
        dto2.actions[1] = enum.open
        dto2.actions[2] = enum.open
        dto2.actions[3] = enum.close
        dto2.actions[4] = enum.stop

        transformer = FakeTransformer()
        actionSender = FakeActionSender()
        controller = EmgController(actionSender, transformer)

        # Act
        transformer.setDto(dto1)
        controller.getNewAction()
        transformer.setDto(dto2)
        controller.getNewAction()
        result = actionSender.amount

        # Assert
        self.assertEqual(result, 2)

    def test_getNewAction_send100NewGrips_ActionSenderCalled100Times(self):
        # Arrange
        enum = ActionEnum
        dto1 = DTO_Action()
        dto2 = DTO_Action()

        dto1.actions[0] = enum.open
        dto1.actions[1] = enum.open
        dto1.actions[2] = enum.open
        dto1.actions[3] = enum.close
        dto1.actions[4] = enum.close

        dto2.actions[0] = enum.open
        dto2.actions[1] = enum.open
        dto2.actions[2] = enum.open
        dto2.actions[3] = enum.close
        dto2.actions[4] = enum.stop

        transformer = FakeTransformer()
        actionSender = FakeActionSender()
        controller = EmgController(actionSender, transformer)

        # Act
        for i in range(50):
            transformer.setDto(dto1)
            controller.getNewAction()
            transformer.setDto(dto2)
            controller.getNewAction()
            i += 1

        result = actionSender.amount

        # Assert
        self.assertEqual(result, 100)


if __name__ == '__main__':
    unittest.main()
