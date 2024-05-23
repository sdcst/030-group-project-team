def isfloat(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


def mean():
    num = []
    while True:
        total = 0
        y = 0
        x = input("Enter a number: ")
        if isfloat(x):
            x = float(x)
            num.append(x)
        elif x.lower() == "exit" and num != []:
            for y in range(len(num)):
                total += num[y]
            mean = total/len(num)
            print(f"the total sum of your input is {total}, the mean is {mean}")
            break
        if not isfloat(x):
            print("Invalid input")
    
        


if __name__ == "__main__":
    mean()