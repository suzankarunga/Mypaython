# Here is the code to the MenuItem class
print('********************WELCOME TO BSIT RESTAURANT********************')
print('BELOW IS OUR MENU , MAKE YOUR ORDER PLEASE')

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return self.name + ': UGX ' + str(self.price)
#Encapsulation 
    def get_total_price(self, count):
        total_price = self.price * count

        if count >= 3:
            total_price *= 0.9

        return round(total_price)

# Let's create classes Food and Drink that inherit MenuItem

class Food(MenuItem):
    pass

class Drink(MenuItem):
    pass

# Now we create instances of Food and Drink.

# Create an instance of the Food class and assign it to the food1 variable
# food1=Food('Sandwich',5)

# Call the info method from food1 and output the return value
# print(food1.info())

# Create an instance of the Drink class and assign it to the drink1 variable
# drink1=Drink('Coffee',3)

# Call the info method from drink1 and output the return value
# print(drink1.info())

# Let's add an attribute calorie_count to the food1 instance.
#  Also, create a calorie_info method in Food class to display the calorie count.


class Food(MenuItem):
    # Define the calorie_info method
    def calorie_info(self):
        print('kcal: ' + str(self.calorie_count))

# food1 = Food('Sandwich', 5)

# Set the calorie_count variable of food1 to 330
# food1.calorie_count=330

# Call the calorie_info method from food1
# food1.calorie_info()


# Let's add the calorie count to the info method instead to display all information at one place.

class Food(MenuItem):
    # Define the info method
    def info(self):
        return self.name + ': UGX ' + str(self.price) + ' (' + str(self.calorie_count) + 'kcal)'
        
# food1 = Food('Sandwich', 5)
# food1.calorie_count = 330

# Call the info method from food1 and output the return value
# print(food1.info())

# Now add volume to the info method in the Drink class the same way.

class Drink(MenuItem):
    # Define the info method
    def info(self):
        return self.name + ': UGX ' + str(self.price) + ' (' + str(self.volume) + 'mL)'
    
# Create an instance of the Drink class and assign it to the drink1 variable
# drink1=Drink('Coffee',3)

# Set the volume variable of drink1 to 180
# drink1.volume=180

# Call the info method from drink1 and output the return value
# print(drink1.info())


# We need to be able to assign calorie count while creating an instance. 
# So we need to use the __init__ module like we did in the MenuItem class.

class Food(MenuItem):
    # Define the __init__ method
    def __init__(self,name,price,calorie_count):
        self.name=name
        self.price=price
        self.calorie_count=calorie_count
    
    
    def info(self):
        return self.name + ': UGX ' + str(self.price) + ' (' + str(self.calorie_count) + 'kcal)'
    
    # def calorie_info(self):
        # print('kcal: ' + str(self.calorie_count))
        

# We already have name and price in the parent class Food.
#  They need not be defined again 
# and can be inherited from the parent class using super().


class Food(MenuItem):
    def __init__(self, name, price, calorie_count):
        # Using super() call __init__() from the parent class
        super().__init__(name,price)
        self.calorie_count = calorie_count
    
    def info(self):
        return self.name + ': UGX ' + str(self.price) + ' (' + str(self.calorie_count) + 'kcal)'
    
    def calorie_info(self):
        print('kcal: ' + str(self.calorie_count))
        


# We then Update the Drink class similarly

class Drink(MenuItem):
    # Define the __init__ method
    def __init__(self, name, price, volume):
        super().__init__(name, price)
        self.volume = volume
    
    def info(self):
        return self.name + ': UGX ' + str(self.price) + ' (' + str(self.volume) + 'mL)'
# print('********************WELCOME TO BSIT RESTAURANT********************')

# Add an argument to Drink()
# drink1 = Drink('Coffee', 3,180)
# print(drink1.info())

# Now that we have required classes and methods available, 
# let's create instances and write the code to run the program.
# # Add an argument to Food()

food1 = Food('Chips', 5000, 30)
food2 = Food('Chicken', 6000, 40)
food3 = Food('Sausage', 1000, 80)
food4 = Food('Chaps', 4000, 100)
food5 = Food('fish', 20000, 280)
food6 = Food('Sandwich', 8000, 180)
food7 = Food('Burger', 12000, 240)
food8 = Food('Streetwise', 24000, 100)
food9 = Food('Rice', 3000, 170)
food10 = Food('Pilau', 15000, 140)

foods = [food1, food2, food3,food4,food5,food6,food7,food8,food9,food10,]

drink1 = Drink('Coffee', 6000, 180)
drink2 = Drink('Orange Juice', 3000, 350)
drink3 = Drink('Espresso', 20000, 30)
drink4 = Drink('Soda', 2000, 130)
drink5 = Drink('Water', 1500, 100)
drink6 = Drink('Cocktail', 15000, 70)
drink7 = Drink('Beer', 5000, 430)
drink8 = Drink('Mojito', 16000, 120)
drink9 = Drink('Krusher', 10000, 130)
drink10 = Drink('Icecream', 7000, 340)

drinks = [drink1, drink2, drink3, drink4, drink5, drink6, drink7, drink8, drink9, drink10]
# print('********************WELCOME TO BSIT RESTAURANT********************')
print('Food')
index = 0
for food in foods:
    print(str(index) + '. ' + food.info())
    index += 1

print('Drinks')
index = 0
for drink in drinks:
    print(str(index) + '. ' + drink.info())
    index += 1

print('************PLEASE***********')

food_order = int(input('Enter food item number: '))
selected_food = foods[food_order]

drink_order = int(input('Enter drink item number: '))
selected_drink = drinks[drink_order]

# Take input from the console and assign it to the count variable
count=int(input('How many meals would you like to purchase? (10% off for 3 or more): '))

# Call the get_total_price method from selected_food and from selected_drink
result=selected_food.get_total_price(count)+selected_drink.get_total_price(count)

# Output 'Your total is UGX____'
print('Your total is UGX ' +str(result))
print('Thank you for you')
