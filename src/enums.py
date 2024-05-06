from enum import Enum, auto


class StateEnum(Enum):
    TODO: auto()
    IN_PROGRESS: auto()
    REVIEW: auto()
    DONE: auto()