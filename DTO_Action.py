from dataclasses import dataclass
from ActionEnum import ActionEnum


@dataclass
class DTO_Action:
    def __init__(self) -> None:
        self.actions = [ActionEnum.stop, ActionEnum.stop,
                        ActionEnum.stop, ActionEnum.stop, ActionEnum.stop]
