def chelp():
    h = str(input("\nwhatxsf4*````` do you need help with?\n[6] for the rocket Δv module\n[9] for half life calculator\n[11] GDP calculator"))
    if h == "11":
        GDPhelp

def GDPhelp():
    print("There are 3 approaches that you could use for calculating GDP: \nExpenditure Approach, \nIncome Approach, \nProduction/Value-Added Approach. \nBy following the instruction that is provided in the calculator, \nyou will be able to calculate the value of GDP using any of the approaches. ")

if __name__ == "__main__":
    GDPhelp()