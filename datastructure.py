my_list =[1,"Mukono" ,"Kampala", 4]
# print(my_list[2])
# print(len(my_list))
# print(my_list[-2])
# my_list[0] ="Jinja"
# my_list[-1]="Fort"
# print(my_list)
hostels =["Tupe","pameja","premium","Cronos","sabit"]
print(hostels[-3:-1])
# print(range(0,10))
# print(list(range(0,10,3)))
#  loops
for i in range(0,10):
    print(i)
hostels =["Tupe","pameja","premium","Cronos","sabit"]
for hostel in hostels[0:4]:
    print(hostel)
    
# i= 0
# while i < 3: 

#     print("Am done ...")
#     i =i+1
i=0
while i < len(hostels):
    print(f"hostel number is {i} {hostels[i]}")
    i += 1







