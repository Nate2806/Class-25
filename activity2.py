class vehicle:
    def __init__(self,maxspeed,mileage):
        self.maxspeed=maxspeed
        self.mileage=mileage

car1=vehicle(418,89)
car2=vehicle(120,7)
print("The max speed of the 1st car is {0} and the mileage is {1}".format(car1.maxspeed,car1.mileage))