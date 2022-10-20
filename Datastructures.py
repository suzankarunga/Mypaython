# from pickle import TRUE
# from random import random
# from tokenize import Number


# random_number1 =0;
# while True:
#     number1=input("please enter your number.")
#     if int(number1) == random_number1 or number1=='done':
#         break
    
#     print("you have guessed right")
def main() :

    print(f'number entered{get_int()}')
def get_int():
 while True:
   try:
        our_number =int(input("Enter a number."))
        return our_number
   except:
    print("The value is not a number.")
main()