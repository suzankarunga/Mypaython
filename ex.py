class Person:

    def __init__(self, name, country):
        self.name = name
        self.country = country


def main():
    first_person = get_person()

    if first_person.name == 'sandra':
        first_person.country = "UG"
    print(
        f"My name is {first_person.name} and my country is {first_person.country} ")


def get_person():
    name = input("What is your name? ")
    country = input("What is your country? ")

    return Person(name, country)


main()