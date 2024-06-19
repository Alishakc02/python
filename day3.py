#Print the multiplication table of number n
a=int(input("Enter a number:"))
i=1
while (i<=10):
    print(a*i)
    i=i+1
    
#Print the elements of the following list using a loop
#{1,4,9,16,25,36,49,64,81,100}
count=1
while(count<=10):
    print(count*count)
    count=count+1
    
    
lis=[1,4,9,16,25,36,49,64,81,100]
index=0
while index<len(lis):
    print(lis[index])
    index=index+1
    
nus= (1,4,9,16,25,36,49,64,81,100)
y=49
i=0
while(i<len(nus)):
    if(nus[i] == y):
        print("Key found successfully")
    i=i+1
