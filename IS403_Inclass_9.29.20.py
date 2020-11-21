class Person:
    def __init__ (self, fName, lName):
        self.first_name = fName
        self.last_name = lName

    def get_name(self):
        return (self.first_name)

class Customer(Person):
    def __init__ (self, fName, lName, age):
        super().__init__(fName, lName)
        self.first_name = "Darla"

def myFunct():
    dName = "Allan"
    print(sFood)

sFood = "Spam and Eggs"
myFunct()


oPerson = Person("Aubrey", "Farnbach")
oPerson.first_name = "Spanky"