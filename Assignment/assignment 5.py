hat_list = [1, 2, 3, 4, 5]
user_input_number = int(input("enter a number to replace the middle number in the array above"))
hat_list[len(hat_list) // 2] = user_input_number 
print("the new list with middle number replaced is:", hat_list)
hat_list[len(hat_list) // 2] = user_input_number 
print("The new list with middle number replaced is:", hat_list)

hat_list.pop(-1) 

print("The list with the last number popped off is ", hat_list)
print("The list with the last number popped off is ", hat_list)

print("The length  of the ramainiing array is:",len(hat_list))




