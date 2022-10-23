from dataclasses import dataclass
from ActionEnum import ActionEnum


@dataclass
class DTO_Action:
    actions = [ActionEnum.stop, ActionEnum.stop,
               ActionEnum.stop, ActionEnum.stop, ActionEnum.stop]
