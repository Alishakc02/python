#WAP to check if a number entered by the user is odd or even.
num=4

rem= num % 2
if(rem == 0):
    print("It is an even number")
else:
    print("It is an odd number")
    
    
   # WAP to find the greatest of 3 numbers entered by the user.
a=190
b=99
c=783
if(a>b and a>c):
    print("a is the greatest number")
elif(b>a and b>c):
    print("b is the greatest number")
else:
    print("c is the greatest number")
   
   
   
   #WAP to check if a number is a multiple of 7 or not.
num1=70
rem1=num1%7
if(rem1==0):
    print("It is a multiple of 7")
else:
    print("It is not a multiple of 7")
    
    
    
    #Congratulations
word=str(input("Enter your word"))
print(word)
if(word=="love"):
    print("I love you more than I can say.")
elif(word=="miss"):
    print("I really really miss you.")
elif(word=="talk"):
    print("I will talk to you no matter what.")
elif(word=="angry"):
    print("You can't be angry with me.")
else:
    print("No such word. Plese try next time.")
