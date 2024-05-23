def GDP():
    done = 0
    while done == 0:
        g=input("Which approach do you wish to progress? \n(\"[e] expenditure\" or \"[i] income\" or \"[p] production\"): ")
        if g=="E"or g=="e":
            done=1
            ExpenditureApproach()
        elif g=="I"or g=="i":
            IncomeApproach()
            done=1
        elif g=="P"or g=="p":
            ProductionApproach()
            done=1
        else:
            print("Undefine")
def ExpenditureApproach():
    done = 0
    while done == 0:
        try:
            c=float(input("Enter the private consumption(C): "))
            i=float(input("Enter the investment in capital(I): "))
            g=float(input("Enter the government spending(G): "))
            nx=float(input("Enter the net export(nx): "))
            a=c+i+g+nx
            a=round(a,2)
            print(f"The GDP is {a}")
            done = 1
        except:
            print("error: not a number")

def IncomeApproach():
    done = 0
    while done == 0:
        try:
            x=float(input("Enter the national income: "))
            y=float(input("Enter the sales taxes: "))
            z=float(input("Enter the depreciation: "))
            w=float(input("Enter the net foreign factor income: "))
            a= x+y+z+w
            a=round(a,2)
            print(f"The GDP is {a}")
            done = 1
        except:
            print("error: not a number")

def ProductionApproach():
    done = 0
    while done == 0:
        try:
            x=float(input("Enter the gross value of output: "))
            y=float(input("Enter the intermediate consumption: "))
            z = x-y
            z = round(z,2)
            print(f"The GDP is {z}")
            done = 1
        except:
            print("error: not a number")

if __name__ == "__main__":
    GDP()