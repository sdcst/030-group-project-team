def area():
    done = 0
    while done == 0:
        x=input("What is the width? ")
        y=input("What is the length? ")
        try:
            x = float(x)
            y = float(y)
            z=x*y
            z=round(z,2)
            print(f"The area is {z}")
            done = 1
        except:
            print("error: not a number")
        

if __name__ == "__main__":
    area()