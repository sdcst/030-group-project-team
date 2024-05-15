def perimeter():
    done = 0
    while done == 0:
        p=input("What shape do you want to calculate the perimeter of? \n(\"rectangle\" or \"triangle\" or \"circle\"): ")
        if p=="rectangle"or p=="Rectangle":
            rectangle()
            done=1
        elif p=="triangle"or p=="Triangle":
            triangle()
            done=1
        elif p=="circle"or p=="Circle":
            circle()
            done=1
        else:
            print("Undefine")
def rectangle():
    done = 0
    while done == 0:
        x=input("Enter the length: ")
        y=input("Enter the width: ")
        try:
            x = float(x)
            y = float(y)
            z=(2*x)+(2*y)
            z=round(z,2)
            print(f"The perimeter is {z}")
            done = 1
        except:
            print("error: not a number")

def triangle():
    done = 0
    while done == 0:
        x=input("Enter side A: ")
        y=input("Enter side B: ")
        z=input("Enter side C: ")
        try:
            x = float(x)
            y = float(y)
            z = float(z)
            a= x+y+z
            b=round(a,2)
            print(f"The perimeter is {b}")
            done = 1
        except:
            print("error: not a number")

import math
def circle():
    done = 0
    while done == 0:
        x=input("Enter the radius of the circle: ")
        try:
            x = float(x)
            y=2*math.pi*x
            z=round(y,2)
            print(f"The perimeter is {z}")
            done = 1
        except:
            print("error: not a number")

if __name__ == "__main__":
    perimeter()