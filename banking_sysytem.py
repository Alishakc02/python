def deposit():
   amount=float(input("Enter the amount to be deposited:"))
   if amount<0:
      print("That's not a valid amount.")
      return 0
   else:
      return amount
      
def withdraw():
   amt=float(input("Enter the balance you want to be withdrawn:"))
   if amt >balance:
      print("Not sufficient balance:")
      return 0
   elif amt<0: 
      print("Balance must be greater than 0")
      return 0
   
   else:
      return amt
def display():
   print(f"Your balance is ${balance:.3f}")


         

is_running=True
balance=0
   
print("------WELCOME TO OUR NABIL BANK------")    



while is_running:
   print("1.DEPOSIT\n 2.WITHDRAW\n 3.CHECK THE BALANCE\n 4.EXIT\n")
   choice=int(input("Enter your choice(1-4):"))
      
      
   if choice==1:
      balance+=deposit()
      
   elif choice==2:
      balance-=withdraw()
   elif choice==3:
      display()
   elif choice==4:
      is_running=False
   else:
      print("Invalid Choice\n")
      
print("Thank you for visiting our Bank\n")
print("Have a great day :)")   
   
 