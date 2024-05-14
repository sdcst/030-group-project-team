import area 

def title():
    print("placeholder")
def userDs():
    a = str(input("Do you want to continue using the caluculator? (Y or N): "))
    e = 0
    if a == "Y" or a == "y":
        e = 1
        return e
    elif a == "N" or a == "n":
        e = 0
        print("ok, now exiting")
        return e
    else:
        print("Error: invalid input, will assume \"no\".")
        return e
def selection():
    print("This calculator has the following functionalities:\n[1] Find the area of a square\n[2] circle")
    uw = str(input("To select an option, enter the number associated with the option: "))
    if uw == "1":
        area.area()
    elif uw == "2":
        circumference.circumference()
    else:
        print("error: invalid input, try again")
