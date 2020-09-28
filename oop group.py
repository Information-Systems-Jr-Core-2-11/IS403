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
        self.total_cost = self.day_rate * self.total_days
        

class Customer():
    company_name = 'Critter Watch'

    def __init__(self, fName, lName, sAdd1, sCity, sState, sZip,  sAdd2 = ""):
        self.first_name = fName
        self.last_name = lName
        self.address1 = sAdd1
        self.address2 = sAdd2
        self.city = sCity
        self.state = sState
        self.zip = sZip

        self.balance = 0.0
        self.updated_balance = 0.0
        
        self.cust_pet = None
        self.cust_id = gen_id(first_name, last_name, address1)

        #this instance variable holds the appointment object
        self.appointment = Appointment

    # takes the first 3 letters from the first name, first 3 letters from the last name, 
    # and first 5 letters from the address to create the cust_id
    def gen_id(self, fName, lName, sAdd1):
        self.cust_id = self.first_name[0:3] + self.last_name[0:3] + self.sAdd1[0:5]


    def return_bill(self):
        return ("Customer " + str(self.cust_id) + " with name " + self.first_name + " " + self.last_name + " owes " + self.updated_balance 
               + " for " + self.cust_pet + "'s stay from " + self.appointment.begin_date + " to " + self.appointment.end_date)

    #not really understand the requirment of this one
    def make_payment(self,iBalance):
        self.updated_balance = self.balance - self.iBalance

      

class Pet():
    appointment = 'Appointment'
    
    def __init__(self, name, breed, age, owner):
        self.pet_name = name
        self.breed = breed
        self.age = age
        self.owner = owner




#gather the data for customer
fName = input('Enter the first name of this customer ')
lName = input('Enter the last name of this customer ')
sAdd1 = input('Enter the address of ' + fName + " ")
sCity = input('Enter the city of ' + fName+ " ")
sState = input('Enter the state of ' + fName + " ")
sZip = input('Enter the zip of ' + fName+ " ")

# FIXME: Create customer object here

#not sure whether we should let the the user enter the balance
iBalance = input('Enter how much money ' + fName + ' owes ') # FIXME: might need to calculate the balance based on the days stored

#gather the data for the pet
name = input("Enter the name of " + fName + "'s pet ")
breed = input("Enter the breed of " + name + " ")
age = input("Enter the age of " + name + " ")

# FIXME: push data to pet attribute of customer object

#gather the data for appointment

beginDate = datetime.strptime(input("Enter Start date in the format m/d/y: "), "%m/%d/%Y")
#beginDate = input("Enter the begin date of " + name + "'s latest boarding ")
endDate = datetime.strptime(input("Enter End date in the format m/d/y: "), "%m/%d/%Y")


oCustomer = Customer(fName, lName, sAdd1, sCity, sState, sZip) # need to pass parameters to object during creation
print(oCustomer.return_bill())

#Call the make_payment() method 
oCustomer.make_payment()
#print the current bill again calling the return_bill() method
print(oCustomer.return_bill())
    