class Student :
        def __init__ (self,regno,name,age):
         self.age=age
         self.regno=regno
         self.name=name

        def Study(self):
            return "I  am studying "
        def Play(self):
            return "Iam playing"
        def Discuss(self):   
            return "I am Discussing"
        def __str__(self):
            return f"my name is {self.name}"

student_1=Student("sd/18 " ,"Zan" ,23)
       
print(student_1)
# print(student_1.Study)
print(student_1.Play())
print(student_1.Discuss())






        