class Product:
    def __init__(self,item_name,price,weight,brand):
        self.item_name = item_name
        self.price = price
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    
    def sell(self):
        self.status = "sold"
        return self

    def addTax(self,tax):
        self.price *= 1 + tax
        return self

    def returnItem(self,reason_for_return):
        if reason_for_return == "defective":
            self.status = "defective"
            self.price = 0
        if reason_for_return == "like_new":
            self.status = "for sale"
        if reason_for_return == "opened":
            self.status = "used"
            self.price *= .8
        return self

    def displayInfo(self):
        print("Name:" , self.item_name)
        print("Price:" , self.price)
        print("Weight:" , self.weight)
        print("Brand:" , self.brand)
        print("Status:" , self.status)
        return self

toiletpaper = Product("toilet paper",5,1,"snuggle")
toiletpaper.sell().addTax(0.1).returnItem("opened").displayInfo()