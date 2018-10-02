class Car:
    def __init__(self,price,speed,fuel,mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 12
        if(self.price > 10000):
            self.tax = 15
        self.displayAll()

    def displayAll(self):
        print(f"Price: {self.price}")
        print(f"Speed: {self.speed}")
        print(f"Fuel: {self.fuel}")
        print(f"Mileage: {self.mileage}")
        print(f"Tax: {float(self.tax)/100}")
        return self
    

Car1 = Car(2000,35,"Full",15)