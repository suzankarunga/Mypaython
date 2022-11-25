from Menu1 import *
class Customer(Drinks,Food):
    def __init__(self):
        self.drink = Drinks()
        self.food = Food()
        self.take = 0
        self.apply = 0
        self.Name = " "
        self.tableNumber = 0
    def setName(self,CustomerName):
        self.Name = CustomerName
    def getName(self):
        return self.Name
    def setTable(self,tablenumber):
        self.tableNumber = tablenumber
    def getTable(self):
        return self.tableNumber
        
    # This method is used to get the choice of the customer  
    def choice(self):
        print("Select the type of service you want")
        # Using tabulate to display the menu
        print(tabulate([['1', 'Food'], ['2', 'Drinks']], headers=['S/N', 'Service']))
        self.take = int(input())
        # This is used to check if the customer wants to order food or drink
        if self.take == 1:
            print(self.food.Menu())
            self.apply = int(input("Enter your choice : "))
            self.food.choice(self.apply)
            
            # This is used to check if the customer wants to order more food or drink
            next = input("Do you want to order more food?,or get a drink (y/n) : ")
            if next == 'y':
                self.choice()
        # This is used to check if the customer wants to order drink  
        elif self.take == 2:
            # This is used to display the menu of the drinks
            print(self.drink.Menu())
            # This is used to get the choice of the customer
            self.apply = int(input("Enter your choice : "))
            self.drink.choice(self.apply)
            
            # This is used to check if the customer wants to order more food or drink
            next = input("Do you want to order more drinks?,or get food (y/n) : ")
            if next == 'y':
                self.choice()
        # This method is used to return the Total amount of the customer request
    def Amount(self):
        final =  self.food.getTotal() + self.drink.getTotal()
        return final
    
    
    #This method is used to get the number of people on a table
    def Tables(self):
        RestaurantCustomer=[]
        # This is used to get the number of people on a table
        # Enabling the User to enter their name and Store it in a list
        customername= input("Order Customer's Name: ")
        self.setName(customername)
        RestaurantCustomer.append(customername)
        # This is used to check if the table is available
        # Show Available tables
        print("Available tables are: ")
        print(tabulate([['1', 'Available'], ['2', 'Available'], ['3', 'Available'], ['4', 'Available'], ['5', 'Available'], ['6', 'Available'], ['7', 'Available'], ['8', 'Available'], ['9', 'Available'], ['10', 'Available']], headers=['Table Number', 'Status']))
        TableNumber= int(input("Enter the table number : "))
        # Storing the Taken table in a list
        self.setTable(TableNumber)
        Tables=[1,2,3,4,5,6,7,8,9,10]
        while True:
            if TableNumber in Tables:
                Tables.remove(TableNumber)
                print("Table is available")
                break
            else:
                print("Table is not available")
                TableNumber= int(input("Enter the table number : "))

             #validate if table is booked or not   

    def Payment(self,finalAmount):
        print(f"TotalAmount: {finalAmount}")
        print("Welcome to the payment section")
        print(tabulate([['1', 'Cash'], ['2', 'Card']], headers=['S/N', 'Payment Method']))
        payment = int(input("Enter your choice : "))
        
        if payment == 1:
            print("Cash Payment")
            amount= int(input("Enter the amount : "))
            if amount >= finalAmount:
                    print("Your change is ",amount - finalAmount)
            else:
                print("Insufficient amount")
                Balance= finalAmount - amount
                print("Your balance is ",Balance)
            
        elif payment == 2:
            print("Card Payment")
            amount= int(input("Enter the amount : "))
            if amount >= finalAmount:
                    print("Your change is ",amount - finalAmount)
                    
            else:
                print("Insufficient amount")
                Balance= finalAmount - amount
                print("Your balance is ",Balance)
                
                
                
    def Welcome(self):
        summationz = 0
        storage = []
        self.Tables()
        number = int(input("Enter the number of people on the table : "))
        for i in range(number):
            print("Customer ",i+1)
            self.choice()
            
            storage.append(self.Amount())
            length = len(storage)
            for i in range(length):
                summationz += storage[i]
            print("*"*50)
        print(f"OrderCustomerName:{self.getName()}\nTableNumber:{self.getTable()}\n")
        print("*"*50)
        self.Payment(summationz)
        self.Receipt()
        
    # Ask user if they want to print receipt

    def Receipt(self):
        # Ask user if they want to print receipt
        print("Do you want to print receipt?")
        print(tabulate([['1', 'Yes'], ['2', 'No']], headers=['S/N', 'Choice']))
        
        if int(input("Enter your choice : ")) == 1:
        #    Using the tabulate module to display the receipt
            print("Receipt")
            print("."*50)
            print(tabulate([['OrderCustomerName', self.getName()], ['TableNumber', self.getTable()], ['TotalAmount', self.Amount()]], headers=['Data', 'Details']))
            print("."*50)   
        
                 
        
        
           
