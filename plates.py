#Python3 program that checks if the number plates of
#vehicles are valid

from curses.ascii import isalpha
from operator import truediv
from this import s

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(string):
    if len(string) < 2 or len(string) >6 :
        return False


    if string[0].isalpha() == False or string[0].isalpha() == False:
        return False
    i = 0
    while i < len(string):
        if string[0] .isalpha() == False:
            if string[i] == '0':
                return False
            else:
                break
    for c in string:
        if c in ['.','','!','?']:
            return False
    return True
main()