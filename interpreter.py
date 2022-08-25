#pytho3 program that calculates various 
#expression depending on the math expression given

user_expression = input("Enter math expression:")
x,y,z = user_expression.split(" ")

new_x = float(x)
new_z = float(z)

if y == "+":
    results = new_x + new_z
if y == "-":
    results = new_x - new_z
if y == "*":
    results = new_x * new_z
if y == "/":
    results = new_x / new_z

print(round(results,1))
 