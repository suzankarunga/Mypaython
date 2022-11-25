from Menu1 import *
from RestaurantDatabases.payment import *
from Customer import *
from getpass import getpass
class Dashboard:
    def __init__(self,username,password):
        self._username="customer"
        self._password = "customer"
    
    def options (self):
        #  Designing the admin menu
        print("*"*120)
        print("Welcome to fast food restaurant")   
        print("*"*120)   
        
    #    Using Tabulate to display the menu with Customer Login
        print(tabulate([['1', 'Customer Login'], ['2', 'Exit']], headers=['S/N', 'Options']))
       
        option=int(input("Enter your Option:"))
        
        if option == 1:
            
            print("Customer Login")
            self.username = input("Enter username: \n") 
            # Using the getpass module to get the password
            self.password = getpass("Enter password: \n")
            if self.username == "Customer" and self.password == "Customer":
                # print("Welcome to our restaurant")
                print("Welcome our esteemed customer")
                customer = Customer()
                customer.Welcome()              
            else:
                print("Invalid username or password")
                self.options()
        