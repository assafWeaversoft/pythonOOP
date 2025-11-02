from classes.Pilot import Pilot,SuperPilot # Here I am importing the Pilot Class
from classes.Plane import Plane
from classes.Flight import Flight
from classes.Passenger import Passenger
from classes.Seat import Seat
from datetime import date

# Here I am instancating the pilot Object
ObjectOfApilot = Pilot(1,"Assaf",date(2025,10,26))
# Here I am instancating the Plane object
ObjectOfAPlane = Plane("NFY279",ObjectOfApilot)
# Here I am instancating the Passanger boarding the plane
_passenger = Passenger(1234,"Michel Smith","ADEX1F")
# Here I am instancating the _seat for my passanger
_seat = Seat(1,2,3,"ClassA",_passenger)
# Here I am Boarding the Passanager and seat to the plane
ObjectOfAPlane.BoardPassangerSeat(_seat)

# Here I am instancating the Flight with plane
_flight = Flight("NYC135",ObjectOfAPlane)

print(f"Going to start flight no: {_flight.FlightNumber}")
_flight.fly()
print(f"Pilot id: {ObjectOfApilot.id}")
print(f"Pilot FullName: {ObjectOfApilot.Fullname}")
print(f"Plane Name: {ObjectOfAPlane.Name}")
_flight.Land()

planesList = []

for _planeObj in planesList:
    if (_planeObj.Name == "Plane-1"):
        print(f"Found {_planeObj.Name}")

planesDict = {}
planesList.append(ObjectOfAPlane)
for i in range(1,10):
    _pilot = None
    _plane = None
    _date  = date(2025,11,2)
    _pilot = Pilot(i,f"Pilot-{i}",_date)
    _plane = Plane(f"Plane-{i}",_pilot)
    print(_plane.Name)
    print(_pilot.Fullname)
    print(_pilot.BirthDate)
    planesList.append(_plane)
    planesDict[_plane.Name] = _plane

print("Done")

for _planeItem in planesList:
    if (_planeItem.Name == "Plane-9"):
        print(f"Found {_planeItem.Name}")

_foundPlane = planesDict["Plane-9"]
print(_foundPlane.Name)