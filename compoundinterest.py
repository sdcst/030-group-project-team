def calculate_compound_interest():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the interest rate (in percentage): "))
    time = float(input("Enter the time period (in years): "))
    tc = int(input("Enter the number of times interest is compounded per year: "))
    a = principal * (1 + rate / (100 * tc)) ** (tc * time)
    a = round(a,2)
    ci = a - principal
    ci = round (ci,2)
    print(f"The compound imterest is {ci}, the total amount is {a}")  

def main():
    calculate_compound_interest()
if __name__ == "__main__":
    main() 

