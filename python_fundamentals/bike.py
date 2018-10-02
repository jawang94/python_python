class Bike:
    def __init__(self,price,max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
      print(self.price)
      print(self.max_speed)
      print(self.miles)      
      return self

    def ride(self):
      self.miles += 10
      return self

    def reverse(self):
      if(self.miles -5 < 0):
        pass
      else:
        self.miles -= 5
      return self

Bike1 = Bike("$100","50mph")
Bike2 = Bike("$14000","215mph")
Bike3 = Bike("$2000","180mph")

Bike1.ride().ride().ride().reverse().displayInfo()
print("\n")
Bike2.ride().ride().reverse().reverse().displayInfo()
print("\n")
Bike3.reverse().reverse().reverse().displayInfo()

