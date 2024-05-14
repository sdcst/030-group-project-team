import time

import area
import chelp

def title():
    print("\n              _                            _        \n__      _____| | ___ ___  _ __ ___   ___  | |_ ___  \n\\ \\ /\\ / / _ \\ |/ __/ _ \\| '_ ` _ \\ / _ \\ | __/ _ \\ \n \\ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | \n  \\_/\\_/ \\___|_|\\___\\___/|_| |_| |_|\\___|  \\__\\___/ \n                                                    \n           _            _       _             \n  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ \n / __/ _` | |/ __| | | | |/ _` | __/ _ \\| '__|\n| (_| (_| | | (__| |_| | | (_| | || (_) | |   \n \\___\\__,_|_|\\___|\\__,_|_|\\__,_|\\__\\___/|_|   \n                                              ")
def userDs():
    a = str(input("Do you want to continue using the caluculator? (Y or N): "))
    e = 0
    if a == "Y" or a == "y":
        print("\n\n\n\n\n\n\n\n\n\n")
        e = 1
        return e
    elif a == "N" or a == "n":
        print("ok, now exiting")
        return e
    else:
        print("Error: invalid input, will assume \"no\"; now exiting")
        return e
def selection():
    done = 0
    while done == 0:
        print("This calculator has the following functionalities:\n[0] help\n[1] Find the area of a square\n[2] circle\n[e] exit")
        uw = str(input("To select an option, enter the number associated with the option: "))
        if uw == "0":
            chelp.chelp()
            done = 1
        if uw == "1":
            area.area()
            done = 1
        elif uw == "2":
            circumference.circumference()
            done = 1
        elif uw == "e":
            print("oki doki, bye bye")
            exit()
        else:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\nerror: invalid input, try again")
            time.sleep(1)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

