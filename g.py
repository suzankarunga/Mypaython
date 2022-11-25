class Engeneer:
    def __init__ ( self , name ,age ,salary, companyName ):
          self.name = name
          self.age = age
          self.salary = salary
          self.companyName = companyName


    @property
    def company(self) :
        return self.companyName
    @company.setter
    def company(self, companyName):
        self.companyName = companyName

EO = Engeneer("phillp" ,34 ,2100 ,"Total Oil anad gas Company")
print(EO.name ,"works with" , EO.company ,"aged" ,EO.age ,"Earns $" , EO.salary ,"per month.")
EO.company ="South Africa Gold Minners "
print(EO.name ,"works with " ,EO.company , "aged", EO.age,"earns $" ,EO.salary,"per month.")



