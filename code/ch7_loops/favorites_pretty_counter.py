def pretty_print_ordered(to_print):
    i = 1
    for item in to_print:
        print(i + ". " +  str(item))
        i = i + 1

favorites = []
more_items = True
while more_items:
    user_input = input("Enter something you like: ")
    if user_input == '':
        more_items = False
    else:
        favorites.append(user_input)

print("Here are all the things you like!")
pretty_print_ordered(favorites)
