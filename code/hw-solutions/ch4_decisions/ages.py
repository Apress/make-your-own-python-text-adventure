age = int(input("What is your age? "))
if age < 18:
    print("You are a child.")
elif 18 < age < 21:
    print("You are an adult, but you cannot purchase alcohol.")
else:
    print("You are an adult.")
if age >= 16:
    print("You are allowed to drive.")
else:
    print("You are not allowed to drive")
