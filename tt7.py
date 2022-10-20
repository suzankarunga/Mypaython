from unicodedata import name


class Item:
    # adding a behaviour
    def __init__(self ,name,quantity):
        self.name =name
        self.quantity =quantity

        print(f"been created my name is {self.name} my quantity is {self.quantity}")

# object creation
car= Item("tesa" ,10000)
ten = Item("taza",30000)