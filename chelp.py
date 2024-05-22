def chelp():
    done = 0
    while done == 0:
        h = str(input("\nwhat do you need help with?\n[6] for the rocket Δv module\n[9] for half life calculator\n[11] GDP calculator\ninput here: "))
        if h == "11":
            GDPhelp()
            end()
            done = 1
        elif h == "6":
            DeltaVhelp()
            end()
            done = 1 
        elif h == "9":
            HLhelp()
            end()
            done = 1
        else:
            print("error: you did not enter a valid entry.")
def end():
    input("(press enter to continue: )")
def GDPhelp():

=======
    print("There are 3 approaches that you could use for calculating GDP: \nExpenditure Approach, \nIncome Approach, \nProduction/Value-Added Approach. \nBy following the instruction that is provided in the calculator, \nyou will be able to calculate the value of GDP using any of the approaches. ")
def DeltaVhelp():
    print("The Delta V (displayed as Δv) means \"change in velocity\".\nIn this case, it measures the change of velocety in a rocket in space, accelerating in the same dierction.\nIt takes the thrust ISP (basically, how powerful the engine is, measured in meters per second),\nThe mass of the rocket before the rocket spends it's fuel,\nand the mass of the rocket after it spends it's fuel.")
def HLhelp():
    print("The half life of an atom means the amount of time it takes to loose half of it's mass via decay.\nfor example, if an element has a half life of 2 days, and there is 20 grams of it, after 2 days it will be 10 grams.\nrespectivly, after 4 days, it will be 5 grams, 6 days will be 2.5 grams, etc.")
>>>>>>> 223f7ead568ea55edd63a3f5c8009f85cc849bba
