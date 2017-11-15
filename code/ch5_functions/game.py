def play():
    print("Escape from Cave Terror!")
    action_input = get_player_command()
    if action_input == 'n' or action_input == 'N':
        print("Go North!")
    elif action_input == 's' or action_input == 'S':
        print("Go South!")
    elif action_input == 'e' or action_input == 'E':
        print("Go East!")
    elif action_input == 'w' or action_input == 'W':
        print("Go West!")
    else:
        print("Invalid action!")


def get_player_command():
    return input('Action: ')


play()
