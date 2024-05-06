import itertools
from dataclasses import dataclass, field

from src.enums import StateEnum


@dataclass
class Ticket:
    state: StateEnum = StateEnum.TODO
    id: int = itertools.count().next
