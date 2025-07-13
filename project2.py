#Cafe Management System
#Dictionary
menu={
    'Pizza':40,
    'Pasta':90,
    'Burger':100,
    'Fried Rice':30,
    'Coffee':45,
    
}
print("Welcome to our newly opened restaurant")
print("Pizza: Rs.40\nPasta: Rs.90\nBurger: Rs.100\nFried Rice: Rs.30\nCoffee: Rs.45\n   ")
order_total=0
while True:
    item_1=input("What you would like to order?")
    if item_1 in menu:
       order_total +=menu[item_1]
       print("Your item {item_1} has been added to the order.")
    else:
        print("Ordered item {item_1} is not available in our restaurant\n Please order something else\n") 
       
       
    another_order=input("Do you like to order another item(yes/no)?")
    if another_order.lower() !='yes':   
       break
        
print("The total amount of items to pay is {order_total} ")        