# class Person:
#   def __init__(self, first_name, last_name, place):
#     self.firstname = first_name
#     self.lastname = last_name
#     self._place = place

#   def printname(self):
#     print(self.firstname, self.lastname)


# obj = Person("Huseyn", "Mammadov", "Baku")
# obj.printname()

# class  Student(Person):
#     def __init__(self, first_name, last_name,age):
#         self.firstname=first_name
#         self.lastname=last_name
#         self.age=age

# x = Student("Yusif", "Osmanov",21)

# x.printname()
# print(obj._place)


from abc import abstractmethod, ABC

class Person(ABC):
    def ad(self):
        print("My mane is Person")
class Huseyn(Person):
    pass
