def volume():
    done = 0
    while done == 0:
        x=input("What is the width? ")
        y=input("What is the length? ")
        h=input("What is the height? ")
        try:
            x = float(x)
            y = float(y)
            h = float(h)
            z=x*y*h
            z=round(z,2)
            print(f"The volume of the cube is {z}")
            done = 1
        except:
            print("error: not a number")

if __name__ == "__main__":
    volume()