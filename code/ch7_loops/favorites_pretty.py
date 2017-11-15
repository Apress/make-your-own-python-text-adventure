def pretty_print_unordered(to_print):
    for item in to_print:
        print("* " +  str(item))

favorites = []
more_items = True
while more_items:
    user_input = input("Enter something you like: ")
    if user_input == '':
        more_items = False
    else:
        favorites.append(user_input)

print("Here are all the things you like!")
pretty_print_unordered(favorites)
