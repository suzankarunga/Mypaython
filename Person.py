from signal import default_int_handler

#Using class
class Person:
    #Instance variables/attributes

   def _init_(self,first_name,last_name,age):
    self.first_name=first_name
    self.last_name=last_name
    self.age=age


#Function that returns all in one instead of repeating (#print(person1.first_name)#print(person1.last_name)#print(person1.age))
def _str_(self):
    return f"This person'name is{self.first_name}{self.last_name} and the age is{self.age}"
   
    #Constructing the person
person1= Person('John','Doe',30)
person2=Person('Jane','Doe',16)

#The prints below only work if your not using the def str(self)
print(person1.first_name)
print(person1.last_name)
print(person1.age)

#After using def str(self) you call out the object (Person1)
#print(person1)
#print(person2)