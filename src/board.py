from dataclasses import dataclass
from src.ticket import Ticket


@dataclass
class Board:
    tickets: list[Ticket]

    def new_ticket(self):
        return Ticket()