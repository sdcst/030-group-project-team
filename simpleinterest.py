def simple_interest():

    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the interest rate: "))
    time = float(input("Enter the time period (in years): "))
    i = (principal * (rate/100) * time) / 100
    i = round(i,2)
    ta= (principal + i)
    print(f"The simple interest is: {i}. The total amount is{ta}")
    
def main():
    simple_interest()
if __name__ == "__main__":
    main() 



