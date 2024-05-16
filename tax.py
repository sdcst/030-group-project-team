import math

def tax():
    a=input("Which type of thing did you buy? food or other")
    done=0
    while done==0:
        try:
      
         if  a == "food":
            x=float(input("What is the sub total?"))
            tax = x*0.05 
            tax=round(tax,2)
            tt= x + tax
            print(f"The tax is {tax}, the toal is {tt} ")
            done=1
         elif a == "other":
            x =float(input("What is the sub total?"))
            tax = x*0.12
            tax = round(tax,2)
            tt = x + tax
            print(f"The tax is {tax}, the total is {tt}")
            done=1
         else:
            print("incorrect")
            done=1
        except:
            print("Error")

if __name__ == "__main__":
    tax()