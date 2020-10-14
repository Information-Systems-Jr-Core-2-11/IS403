# Xingtong Han, Hayden Thomas, Jonah Duffin, Aubrey Farnbach (Wright)
# 10/14/20
# Section 2 Group 11

# Create a new Python application that implements various data structures.
# • Create a variable for a Queue with items of type string
#   o This variable will represent your line of customers waiting outside.
# • Create a variable for a Dictionary with keys of type string and values of type int.
#   o This variable will hold information about each customer
# • Put 100 customers into the queue
#   o You can use the random class to generate random people for your line
# • Add a random number of burgers to the total for each customer. Make sure there
# is a key in the dictionary for each customer before you try incrementing their
# total!
# • Print out each customer and their total burgers eaten.
# NOTE: Remember that a queue in Python is a list data structure.

from queue import Queue
import random
import collections

#Createt a variable for a Queue with items of type string
quCustomer = Queue(0)

#Create a variable for a Dictionary with keys of type string and values of type int
dictCustomer = {}

# • Add a random number of burgers to the total for each customer. Make sure there
# is a key in the dictionary for each customer before you try incrementing their
# total!

def randomName():    
    asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman",
    "Singing Bush"]
    iRandomNum = random.randint(0,8)
    return asCustomers[iRandomNum]

def randomBurgers() :
     return random.randint(1, 20)

# Put 100 customers into the queue
# You can use the random class to generate random people for your line
for i in range(100):
    quCustomer.put(randomName())

for cust in range(1, quCustomer.qsize() + 1):
    currentCustomer = quCustomer.get()
    if currentCustomer not in dictCustomer:
        dictCustomer[currentCustomer] = 0
    
    dictCustomer[currentCustomer] += randomBurgers()
    
# Add a random number of burgers to the total for each customer. Make sure there
# is a key in the dictionary for each customer before you try incrementing their
# total!

#  sort the dictionary in descending order with the most burgers being eaten by a customer at the top
listSortedCustomers = []
listSortedCustomers = sorted(dictCustomer.items(), key=lambda x: x[1], reverse=True)

# Make the customer name an even sized value using the ljust() function with the value of
# 19 as the parameter like customer[0].ljust(19) where customer is each list item object
# in the for loop

# • Print out each customer and their total burgers eaten.
for cust in listSortedCustomers:
    print(f'{cust[0].ljust(19)} {cust[1]} burgers')