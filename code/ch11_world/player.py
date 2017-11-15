import items


class Player:
    def __init__(self):
        self.inventory = [items.Rock(),
                          items.Dagger(),
                          'Gold(5)',
                          'Crusty Bread']

        self.x = 1
        self.y = 2

    def print_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print('* ' + str(item))
        best_weapon = self.most_powerful_weapon()
        print("Your best weapon is your {}".format(best_weapon))

    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None
        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass

        return best_weapon

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)
