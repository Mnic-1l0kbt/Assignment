#Python3 program that accepts define coins
#return both remaining amount and change owed.
coke_price = 50

while coke_price > 0:
    print(f"Coke price: {coke_price}")
    coin = int(input("Insert a coin:"))
    if coin in [25,10,5]:
         coke_price -= coin 

#To calculate the change owed after inserting coins
change_owed = abs(coke_price)
print(f"Change owed: {change_owed}")


