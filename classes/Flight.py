from classes.Plane import Plane
class Flight:
    FlightNumber: str
    ActivePlane: Plane
    IsInFlight: bool

    def __init__(self,_flightNumber: str,_activePlane:Plane):
        self.FlightNumber=_flightNumber
        self.ActivePlane=_activePlane
        self.IsInFlight=False

    def fly(self):
        if (not self.IsInFlight):
          self.IsInFlight=True
          print("Starting Flying")
    
    def Land(self):
        if (self.IsInFlight):
            self.IsInFlight=False
            print("Stopped Flying")