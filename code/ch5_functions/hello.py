def say_hello():
    print("Hello, World!")

say_hello()

answer = input("Would you like another greeting?")
if answer == 'y':
    say_hello()
