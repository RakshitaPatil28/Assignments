#Single Inheritance Example
class vehicle:
    def __init__ (self,mileage,cost):
        self.mileage=mileage
        self.cost=cost
    def show_details(self):
        print("I am a Vehicle")
        print("Milage of the vehicle is ",self.mileage)
        print("Cost of the vehicle is ",self.cost)
v1=vehicle(200,200)
v1.show_details()


#second example
class Car(vehicle):
    def show_car(self):
        print("I am a car")
c1=Car(200,1200)
c1.show_details()
c1.show_car()

#over_riding init method
class Car(vehicle):
    def __init__(self,mileage,cost,tyres,hp):
        super().__init__(mileage,cost)
        self.tyres=tyres
        self.hp=hp
    def show_car_details(self):
        print("I am a car")
        print("Number of tyres are ",self.tyres)
        print("Value of horse power is ",self.hp)
c1=Car(20,12000,4,300)
c1.show_details()
c1.show_car_details()
