name = input("Please enter your name: ")
age = input("Please enter your age: ")
try:
    print("You were born in {}.".format(2015 - int(age)))
except ValueError:
    print('Unable to calculate the year you were born, ' \
          + '"{}" is not a number.'.format(age))
