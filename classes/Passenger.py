class Passenger:
    id: int
    FullName: str
    ticketNumber: str

    def __init__(self, _id:int,_fullName:str,_ticketNumber:str):
        self.id = _id
        self.FullName = _fullName
        self.ticketNumber = _ticketNumber