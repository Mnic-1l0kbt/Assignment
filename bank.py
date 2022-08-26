#Python3 program that matches greetings and user
#bank request.

greeting = input("Greeting : ").replace(" ", "").lower()
if greeting.find("hello") != -1:
    print('$0')
elif greeting[0] == "h":
    print('$20')
else :
    print('$100')