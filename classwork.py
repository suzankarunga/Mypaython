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