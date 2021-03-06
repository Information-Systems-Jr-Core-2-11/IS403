from datetime import datetime
# objects declared
class Appointment(object):

    def __init__(self, owner):
        self.owner = owner

    def set_appointment(self, beginDate, endDate, dayRate):
        self.begin_date = beginDate
        self.end_date = endDate
        self.day_rate = dayRate
        self.calc_days()

    def calc_days(self):
        self.total_days = (self.end_date - self.begin_date).days
        if self.total_days <= 0:
            self.total_days = 1
        self.total_cost = self.day_rate * self.total_days
        self.owner.balance = self.total_cost
        

class Customer():
    company_name = 'Critter Watch'

    def __init__(self, fName, lName, sAdd1, sAdd2, sCity, sState, sZip):
        self.first_name = fName
        self.last_name = lName
        self.address1 = sAdd1
        self.address2 = sAdd2
        self.city = sCity
        self.state = sState
        self.zip = sZip

        self.balance = 0.0
        
        self.cust_pet = []
        self.cust_id = self.gen_id()


    # takes the first 3 letters from the first name, first 3 letters from the last name, 
    # and first 5 letters from the address to create the cust_id
    def gen_id(self):
        newID = self.first_name[0:3] + self.last_name[0:3] + self.address1[0:5] 
        return newID.replace(" ","")


    def return_bill(self, petCount, appointmentCount):
        return (f"Customer {self.cust_id} with name {self.first_name} {self.last_name} owes ${self.balance:.2f} for {self.cust_pet[petCount].pet_name}'s stay from {self.cust_pet[petCount].appointment[appointmentCount].begin_date.strftime('%x')} to {self.cust_pet[petCount].appointment[appointmentCount].end_date.strftime('%x')}")


    def make_payment(self, payment):
        self.balance -= payment

    def add_pet(self, newPet):
        self.cust_pet.append(newPet)

      

class Pet():
    
    def __init__(self, name, breed, age, owner):
        self.pet_name = name
        self.breed = breed
        self.age = age
        self.owner = owner
        self.appointment = []

    def set_appointment(self, beginDate, endDate, dayRate):
        self.appointment.append(Appointment(self.owner))
        self.appointment[-1].set_appointment(beginDate, endDate, dayRate)
        




# initialize variables, gather how many times you will iterate the program
numCustomers = input("How many customers would you like to process for Critter Watch? ")
while not numCustomers.isnumeric(): # error check for number of customers
    numCustomers = input("Invalid input. How many customers would you like to process? ")
numCustomers = int(numCustomers)
aoCustomers = []

# For loop iterates however many times user specified. Customers for each iteration are stored in aoCustomers
for customerCount in range(0, numCustomers):
    #Gather customer info and create customer object
    print()
    fName = input(f'Enter the first name of customer {customerCount + 1} ')
    lName = input(f'Enter the last name of customer {customerCount + 1} ')
    sAdd1 = input(f"Enter line 1 of {fName}'s address ")
    sAdd2 = input (f"Enter line 2 of {fName}'s address. If none, just press enter. ")
    sCity = input(f'Enter the city of {fName} ')
    sState = input(f'Enter the state of {fName} ')
    sZip = input(f'Enter the zip of {fName} ')
    print()
    aoCustomers.append(Customer(fName, lName, sAdd1, sAdd2, sCity, sState, sZip))

    numPets = int(input(f"How many pets does {fName} have? "))

    for petCount in range(0, numPets):

        #gather pet info and create pet object
        petName = input(f"Enter the name of {fName}'s pet #{petCount + 1} ") #FIXME: add pet number
        petBreed = input(f"Enter {petName}'s breed ")
        petAge = input(f"Enter {petName}'s age ")
        print()
        currentPet = Pet(petName, petBreed, petAge, aoCustomers[customerCount])

        # add pet object to customer object
        aoCustomers[customerCount].add_pet(currentPet)
        
        numAppointments = int(input(f'How many appointments for {petName}? '))
        for appointmentCount in range(0, numAppointments):
        #Gather appointment info and set appointment (object) in Pet object
            print()
            beginDate = datetime.strptime(input(f"Enter Start date for appointment {appointmentCount + 1} in the format mm/dd/yyyy: "), "%m/%d/%Y")
            endDate = datetime.strptime(input(f"Enter End date for appointment {appointmentCount + 1} in the format mm/dd/yyyy: "), "%m/%d/%Y")
            dayRate = input("Enter the day rate, without a $ symbol. ")
            while not dayRate.isnumeric(): # error check for number of customers
                dayRate = input("Invalid input. Enter the day rate, without a $ symbol. ")
            dayRate = float(dayRate)
            aoCustomers[customerCount].cust_pet[petCount].set_appointment(beginDate, endDate, dayRate)

            #Print the bill, make a payment, and print the bill again
            print()
            print(aoCustomers[customerCount].return_bill(petCount, appointmentCount))
            print()
            custPayment = input("Enter the customer payment, without a $ symbol. ")
            while not custPayment.isnumeric() or not float(custPayment) <= aoCustomers[customerCount].balance: # error check for number of customers
                custPayment = input("Invalid input. Enter the customer payment, without a $ symbol, no greater than the total balance. ")
            custPayment = float(custPayment)
            aoCustomers[customerCount].make_payment(custPayment)
            print()
            print(aoCustomers[customerCount].return_bill(petCount, appointmentCount)) 
            print()


    