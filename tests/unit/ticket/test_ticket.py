from src.ticket import Ticket


def test_create_ticket():
    ticket_old = Ticket()
    ticket_new = Ticket()
    assert ticket_new.id > ticket_old.id