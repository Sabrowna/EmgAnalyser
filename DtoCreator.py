from abc import ABC, abstractmethod
from DTO_Action import DTO_Action
from ActionEnum import ActionEnum


class IDtoCreator(ABC):
    @abstractmethod
    def createActionDto(self, sensor, isDoubleTension):
        raise NotImplementedError


class DtoCreator(IDtoCreator):
    def __init__(self) -> None:
        self.dtoAction = DTO_Action()
        self.actionEnum = ActionEnum

    def createActionDto(self, sensor, isDoubleTension):
        motorConfigs = sensor.getSensorsMotorcontrol()
        for i in range(len(motorConfigs)):
            if motorConfigs[i] != None:
                if motorConfigs[i] != '0':
                    # if motorConfigs[i] == '0':
                    #     self.dtoAction.actions[i] = self.actionEnum.stop
                    if (sensor.getMotorDirection() == 'o' and sensor.getIsActive() == True) or (sensor.getMotorDirection() == 'd' and isDoubleTension == False):
                        self.dtoAction.actions[i] = self.actionEnum.open
                    elif (sensor.getMotorDirection() == 'c' and sensor.getIsActive() == True) or (sensor.getMotorDirection() == 'd' and isDoubleTension == True):
                        self.dtoAction.actions[i] = self.actionEnum.close
                    elif sensor.getMotorDirection() == 's' or sensor.getIsActive() == False:
                        self.dtoAction.actions[i] = self.actionEnum.stop
                    else:
                        continue

    def getActionDto(self):
        return self.dtoAction.actions
