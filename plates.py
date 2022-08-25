#Python3 program that checks if the number plates of
#vehicles are valid

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    ...
    
main()