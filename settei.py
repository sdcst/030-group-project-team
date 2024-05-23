import time

import area
import chelp
import surfacearea
import volume
import flaan_modules
import perimeter
import tax
import compoundinterest
import halflife
import simpleinterest
import GDP
import mean
import pythagorean

def title():
    print("\n              _                            _        \n__      _____| | ___ ___  _ __ ___   ___  | |_ ___  \n\\ \\ /\\ / / _ \\ |/ __/ _ \\| '_ ` _ \\ / _ \\ | __/ _ \\ \n \\ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | \n  \\_/\\_/ \\___|_|\\___\\___/|_| |_| |_|\\___|  \\__\\___/ \n                                                    \n           _            _       _             \n  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ \n / __/ _` | |/ __| | | | |/ _` | __/ _ \\| '__|\n| (_| (_| | | (__| |_| | | (_| | || (_) | |   \n \\___\\__,_|_|\\___|\\__,_|_|\\__,_|\\__\\___/|_|   \n                                              ")
    time.sleep(1)
def userDs():
    a = str(input("Do you want to continue using the caluculator? (Y or N): "))
    e = 0
    if a == "Y" or a == "y":
        print("\n"*50)
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
        print("This calculator has the following functionalities:\n[0] help\n[1] Find the area of a shape\n[2] find surface area of cube or sphere\n[3] find volume of a cube\n[4] find if a triangle is acute, right, or obtuse using it's sides\n[5] find the perimeter of a rectangle, triangle, or circle\n[6] find the Δv of a rocket in a vacuum\n[7] tax calculator for BC, Canada\n[8] Compound Interest Calculator\n[9] Halflife (chemestry) Calculator\n[10] Simple Interest Calculator\n[11] GDP calculator\n[12] find average of a set of numbers\n[13] pythagorean theorum\n[e] exit")
        uw = str(input("To select an option, enter the number associated with the option: "))
        print("\n"*100)
        if uw == "0":
            chelp.chelp()
            done = 1
        elif uw == "1":
            area.area()
            done = 1
        elif uw == "2":
            surfacearea.surfacearea()
            done = 1
        elif uw == "3":
            volume.volume()
            done = 1
        elif uw == "4":
            flaan_modules.triconpute()
            done = 1
        elif uw == "5":
            perimeter.perimeter()
            done = 1
        elif uw == "6":
            flaan_modules.deltaV()
            done = 1
        elif uw == "7":
            tax.tax()
            done = 1
        elif uw == "8":
            compoundinterest.calculate_compound_interest()
            done = 1
        elif uw == "9":
            halflife.hldo()
            done = 1
        elif uw == "10":
            simpleinterest.simple_interest()
            done = 1
        elif uw == "11":
            GDP.GDP()
            done = 1 
        elif uw == "12":
            mean.mean()
            done = 1 
        elif uw == "13":
            pythagorean.pythagorean()
            done = 1
        elif uw == "e":
            print("oki doki, bye bye")
            exit()
        else:
            print("\n"*50)
            print("error: invalid input, try again")
            time.sleep(1)
            print("\n"*50)

