def triangle(a,b,c):
    t = [a,b,c]
    t.sort()
    if t[2] >= (t[1] + t[0]):
        return 0
    else:
        aa = t[0] ** 2
        bb = t[1] ** 2
        cc = t[2] ** 2
        if aa + bb < cc:
            return 3
        elif aa + bb == cc:
            return 2
        elif aa + bb > cc:
            return 1

def triconpute():
    done1 = 0
    print("This calculator will ask for the lenghs of 2 sides, then the lengh of the hypotenuse.")
    while done1 == 0:
        try:
            s1 = float(input("Please enter the lengh of side 1: "))
            s2 = float(input("Please enter the lenght of side 2: "))
            s3 = float(input("Please enter the lenght of the hypotenuse: "))
            done1 = 1
        except:
            print("error: you did not enter a valid number.")
    r = triangle(s1,s2,s3)
    if r == 1:
        print("The triangle is obtuse.")
    elif r == 2:
        print("That is a right triangle.")
    elif r == 3:
        print("The triangle is acute.")
    elif r == 0:
        print("The triangle is not possible.")

def deltaV():
    done=0
    import math
    print("This is a simple deltaV calculator, it assumes that the target spacecraft is in a vaccuum, \nfiring engines in a constant direction, and is not affected by an external SOI.\n")
    while done == 0:
        try:
            isp = float(input("please enter the in-vacuum thrust ISP (specific impulse) of the engine (m/s): "))
            mass_m0 = float(input("please enter the initial mass of the spacecraft before burn time (kg): "))
            mass_m1 = float(input("please enter the final mass of the spacecraft after fuel is expent (kg): "))
            if mass_m0 > mass_m1:
                Δv = math.log(mass_m0/mass_m1)
                Δv = math.log(mass_m0/mass_m1)
                Δv = Δv * isp
                print(f"\nthe change in velocity (Δv) of the spacecraft is {round(Δv,4)} m/s.\n")
                done=1
            elif mass_m0 <= mass_m1:
                print("error: the initial mass must be greater than the end mass")
        except:
            print("error: you have entered an invalid input.")
        