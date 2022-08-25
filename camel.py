#Pythone3 program converting string from
#camel case to snake case.
def change_case (string):
    return ''.join(['_'+ i.lower() if i.isupper()
    else i for i in string]) .lstrip('_')
    

string = input("Enter a variable name :")
print(change_case(string))

