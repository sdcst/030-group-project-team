import math
def area():
    done = 0
    while done == 0:
        g=input("Which area do you wish to calculate? \n(\"[s] square\" or \"[c] circle\" or \"[t] triangle\"): ")
        try:
            if g=="S"or g=="s":
                x=float(input("What is the width? "))
                y=float(input("What is the length? "))
                z=x*y
                z=round(z,2)
                print(f"The area is {z}")
                done=1
            elif g=="C"or g=="c":
                x=float(input("What is the radius of the circle? "))
                y = math.pi * (x ** 2)
                y = round(y,2)
                print(f"The area is {y}")
                done=1
            elif g=="T"or g=="t":
                x=float(input("What is the value of base? "))
                y=float(input("What is the value of height? "))
                z = (x * y)/2
                z=round(z,2)
                print(f"The area is {z}")
                done=1
            else:
                print("error: not a number")
        except:
            print("Undefine")

if __name__ == "__main__":
    area()
