# class student:
#     pass

# zan = student()
# print(zan)

# Adrian = "Dawin"
# print(Adrian)

# year = 2001
# print(year)

class student:
    pass
    # Define a constructor
    def __init__(self, name, course , access_no):
        self.name = name
        self.course = course
        self.access_no = access_no
        
        print("in this silence")
    def eat(self):
        print("i am going to eat ")
    def sleep(self) :
        print("I am going to sleep") 
    def __str__(self) :
        return f"hey my name is {self.name} and my course is {self.course} and my course is {self.access_no}"


jim = student( "Dellilah" ,"Ggit" , "G3") 
jimmy = student ("Dawin" ,"dhit" ,"r4")

print(jim.access_no)

print(jim)
print(jimmy)




