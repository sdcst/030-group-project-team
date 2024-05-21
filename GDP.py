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
        c=input("Enter the private consumption(C): ")
        i=input("Enter the investment in capital(I): ")
        g=input("Enter the government spending(G): ")
        nx=input("Enter the net export(nx): ")
        try:
            c=float(c)
            i=float(i)
            g=float(g)
            nx=float(nx)
            a=c+i+g+nx
            a=round(a,2)
            print(f"The GDP is {a}")
            done = 1
        except:
            print("error: not a number")

def IncomeApproach():
    done = 0
    while done == 0:
        x=input("Enter the national income: ")
        y=input("Enter the sales taxes: ")
        z=input("Enter the depreciation: ")
        w=input("Enter the net foreign factor income: ")
        try:
            x = float(x)
            y = float(y)
            z = float(z)
            w = float(w)
            a= x+y+z+w
            a=round(a,2)
            print(f"The GDP is {a}")
            done = 1
        except:
            print("error: not a number")

def ProductionApproach():
    done = 0
    while done == 0:
        x=input("Enter the gross value of output: ")
        y=input("Enter the intermediate consumption: ")
        try:
            x = float(x)
            y = float(y)
            z = x-y
            z = round(z,2)
            print(f"The GDP is {z}")
            done = 1
        except:
            print("error: not a number")

if __name__ == "__main__":
    GDP()