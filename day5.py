#Print the elements of the following list using a loop

list=[1,4,9,16,25,36,49,64,81,100]
for num in list:
    print(num)
    
#Search for a number x in ths tuple using loop
lists=(1,4,9,16,25,36,49,64,81,100)
x=64
for num in lists:
    if(num == x):
        print("Key found successfully")
    else:
        print("Search failure")    