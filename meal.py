#Python3 program that takes in type and output 
#the meal to be take if breakfast, lunch or dinner.

def main():
    meal_time= input("Enter time:")
    convert(meal_time)

    
def convert(time):
    hours,minute =time.split(":")
    converted_time = float(hours) + (float(minute)/60)
    return(converted_time)

    if meal_time >= 7 and meal_time <= 8:
        print("Breakfast time")
    elif meal_time >= 12 and meal_time <= 13:
        print("Lunch time")
    elif meal_time >= 18 and meal_time <= 19:
        print("Dinner time")



