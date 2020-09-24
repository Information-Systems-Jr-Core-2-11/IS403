from datetime import datetime
class Appointment(object):

    def __init__(self, owner):
        self.owner = owner

    def set_appointment(self, beginDate, endDate, dayRate):
        self.begin_date = beginDate
        self.end_date = endDate
        self.day_rate = dayRate

    def calc_days(self):
        self.total_days = self.end_date - self.begin_date
        

class Customer():
    company_name = 'Critter Watch'

    def __init__(self, custID, fName, lName, sAdd1, sAdd2, sCity, sState, sZip):
        self.first_name = fName
        self.last_name = last_name
        self.address1 = sAdd1
        self.address2 = sAdd2
        self.city = sCity
        self.state = sState
        self.zip = sZip

        self.balance = 0.0
        self.cust_pet = None
        self.cust_id = gen_id(first_name, last_name, address1)

      

class Pet():
    self.appointment = 'Appointment'
    
    def __init__(self, name, breed, age, owner):
        self.pet_name = name
        self.breed = breed
        self.age = age
        self.owner = owner
        