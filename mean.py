def mean():
    for i in range(3):
        while i >= 0:
            number = []
            number.append(int(input("Enter numbers separated by spaces: ")))
            total = sum(number)
            count = len(number)
            mean = total/count
            print(f"The mean is {mean}")
"""
n = input("Enter # of numbers you want to calculate: ")
try:
    if n == int(n):
        n = int(n)
except:
    print("Invalid input")
    n = input("Enter # of numbers you want to calculate: ")
for i in range(int(n)):
    x = 0
    x = input("Enter a number: ")
    if x == float(x):
        x+=x
        if i == int(n):
            m = x/i
            print(f"sum of your number is {x} and mean is {m}")
    """
    
    
        


if __name__ == "__main__":
    mean()