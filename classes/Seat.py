from classes.Passenger import Passenger
class Seat:
    id: int
    Row: int
    Column: int
    SeatClass: str
    PassengerSitting: Passenger

    def __init__(self,_id:int,_row:int,_column:int,_seatClass:str,_passengerSitting: Passenger):
        self.id=_id
        self.Row=_row
        self.Column=_column
        self.SeatClass=_seatClass
        self.PassengerSitting=_passengerSitting