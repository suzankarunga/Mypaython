class Person:
    def __init__(self, name ,age ,country):
        self.name = name
        self .age = age
        self.country = country

        @property
        def country(self):
            return self .__country

        @country.setter
        def country(self,value):
            if(value not in ['Uganda' ,'Kenya' ,'Congo']):
                raise('Country not in East Africa')
            self.__country = value

        def __repr__(self) :
            return f'Name is {self.name} age is {self.age} and countr is {self.country}'

        person1 = Person('kendoe' ,28 ,'Uganda')
        person1.name = 'Jimmy' 
        person1.age =16
        person1.country = 'Canada'
        print(person1)  