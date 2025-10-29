from datetime import date

class Pilot:

    id: int
    Fullname: str
    BirthDate: date
    Rank: str
    age: int

    # This is my constructor function , it will always run when I\
    # init my object
    def __init__(self,_pilotid:int,_pilotFullname:str,_pilotBirthdate: date):
        self.id = _pilotid
        self.Fullname = _pilotFullname
        self.birthdate = _pilotBirthdate

class SuperPilot(Pilot):
    superPilotName: str