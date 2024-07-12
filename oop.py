
# Thing = Car
class Car:
    def __init__(self,engine,color,type):
        self.engine = engine
        self.color = color
        self.type = type
    
    def park(self):
        print(f'{self.type} is now parked')

    def navigate(self):
        print(f'{self.type} is now in Nav Mode')

my_car = Car(engine="2L",color="red",type="Sedan")
print(my_car) # Object
print(my_car.type)
my_car.park()

his_car = Car(engine="2.5L",color="white",type="SUV")
print(his_car) # Object
his_car.navigate()


# Actions (Methods)
# drive
# navigate
# park



