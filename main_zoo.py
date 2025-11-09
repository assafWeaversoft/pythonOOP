from Zoo.Animal import Animal
from Zoo.Cage import Cage
from Zoo.Food import Food
newAnimal = Animal("Zebra",True,False,21)
_mamel = True
_vegitarian = True
_preditor = True

print(newAnimal)
newCage = Cage("13FE")
newCage.AddAnimal(newAnimal)


newLion = Animal("Lion",_mamel,_preditor,15)
newMoose = Animal("Moose",_mamel,not _preditor,99)

try:
    kartoshoka = Food("Kartoshka",_vegitarian)
    newMoose.isHungry = True
    newMoose.feed(kartoshoka)
    newLion.feed(Food("Svinya",not _vegitarian))
    newCage.AddAnimal(newLion)
except Exception as ex:
    print(ex)

print(f"Animal Name is {newAnimal.Name}")