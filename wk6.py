
from unicodedata import name

class Person:
 def _int_(self ,name,country)
     self .name = name
     self .country = country


def main():


    
    person = get_person()

    if person.name == 'ken' :
       person.country = 'spain'

    print(f"name is {person[0]} country {person[1]} and")

    
def get_person():
    
        name =input("your name")
        country = input("your country")
        
        return[name ,country]
main()    