def add(a, b):
    return a + b

while True:
    try:
        num1 = int(input("Please enter your 1st number: "))
        num2 = int(input("Please enter your 2nd number: "))

        print(add(num1, num2))
    except ValueError:
        print("You must enter a number.")    
