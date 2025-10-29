from classes.Pilot import Pilot
from classes.Seat import Seat
from typing import List

class Plane:
    Name: str
    FlightPilot: Pilot
    PlaneSeats: List[Seat] = []

    def __init__(self,_name: str,_pilot:Pilot):
        self.Name=_name
        self.FlightPilot=_pilot

    def BoardPassangerSeat(self,_seat:Seat):
        self.PlaneSeats.append(_seat)
