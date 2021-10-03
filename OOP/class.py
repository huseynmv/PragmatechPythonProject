class Person():
    def __init__(self, name ,age):
        self.name=name
        self.age=age
    @property
    def getname(self):
        print (self.name)


    def setage(self,age):
        self.age=age
    
p1=Person("Huseyn",21)
p1.age=25
print(p1.age)
p1.setage(23)
print(p1.age)


class Restaurant():
    def __init__(self, restaurant_name, cousine_type):
        self.restaurant_name=restaurant_name
        self.cousine_type=cousine_type
    def desribe_restaurant(self):
        print (self.restaurant_name + " " + self.cousine_type)
    
    def open_restaurant(self):
        print (f'{self.restaurant_name} aciqdir')

r1=Restaurant("Fuzzy", "CoffeeShop")
r1.desribe_restaurant()
r1.open_restaurant()

