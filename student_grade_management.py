"""
comments 
in dictionary values occur in pair 
left side-key
right side-value

"""
student_grades={}
#Add a student list
def add_student(name, grade):
    student_grades[name]=grade
    print(f"Adeed {name} with a {grade}")

#Update a student list
def update_student(name, grade):
    if name in student_grades:
        student_grades[name]=grade
        print(f"{name} with marks are updated {grade}")
    else:
        print(f"{name} not found!")

  #Delete a student name
def del_students(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been deleted!")
    else:
        print(f"{name} not found!")
        
        #Display the name list
def view_students():
    if student_grades:
        for name,grade in student_grades.items():
            print(f"{name}:{grade}")
    else:
        print("No students found!")
            
            
def main():
    print("\n Student Management System")
    print("1. Add Student\n")
    print("2. Update Student\n")
    print("3. Delete Student\n")
    print("4. Display Student\n ")
    print("5. Exit\n")
        
    while True:
       
        choice=int(input("Enter your choice:"))
        if choice ==1:
            name=input("Enter the student's name:")
            grade=int(input("Enter your grade:"))
            add_student(name, grade)
        elif choice==2:
             name=input("Enter the student's name you want to update:")
             grade=int(input("Enter your grade:"))
             update_student(name, grade)
        elif choice==3:
             name=input("Enter the student's name you want to delete:")
             del_students(name)
        elif choice==4:
            view_students()
        elif choice==5:
            print("Closing the screen")
            break
        else:
            print("Invalid choice!")
            
main()