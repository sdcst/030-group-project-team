import math

def tax():
    a=input("Which type of thing did you buy? food [f] or other [o]: ")
    done=0
    while done==0:
        try:
      
         if  a == "food" or a == "F" or a == "f":
            x=float(input("What is the sub total? ($): "))
            tax = x*0.05 
            tax=round(tax,2)
            tt= x + tax
            print(f"The tax is ${round(tax,2)}, the toal is ${round(tt,2)} ")
            done=1
         elif a == "other" or a=="O" or a=="o":
            x =float(input("What is the sub total? ($): "))
            tax = x*0.12
            tax = round(tax,2)
            tt = x + tax
            print(f"The tax is ${round(tax,2)}, the total is ${round(tt,2)}")
            done=1
         else:
            print("invalid option, now exiting")
            done=1
        except:
            print("Error")

if __name__ == "__main__":
    tax()