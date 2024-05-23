import math
def pythagorean():
    print("This calculator will help you find the hypotenus of a triangle :)\nplease input the value of the other 2 sides of the triangle in the question that was provided below.")
    done = 0
    while done == 0:
        try:
            x=float(input("What is the value of side A? "))
            y=float(input("What is the value of side B? "))
            z = math.sqrt((x ** 2) + (y ** 2))
            z = round(z,2)
            print(f"The hypotenus of this triangle is {z}")
            done = 1
        except:
            print("error: not a number")

if __name__ == "__main__":
    pythagorean()