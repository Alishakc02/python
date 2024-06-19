#Conditional Statements
age=12
if(age >= 18):
    print("You are eligible for voting.")

else:
    print("Come next year only if you reached 18 years old.")
    
    
    #Grade students based on marks
#marks >= 90, grade = "A"
#90 > marks >= 80, grade = "B"
#80 > marks >= 70, grade = "C"
#70 > marks, grade = "D"

marks=75
if(marks >=90):
   print("Grade A")
elif(marks>=80 and marks<90):
    print("Grade B")
elif(marks>=70 and marks<80):
    print("Grade C")
else:
    print("Grade D")



#Nesting 
age=23
if(age>=18):
  
    if(age>80):
        print("Can't Drive")
    else:
          print("Can Drive")
else:
    print("Can't Drive")