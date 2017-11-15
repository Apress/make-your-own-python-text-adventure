import enemies
import random


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):
        pass


class StartTile(MapTile):
    def intro_text(self):
        return """
        You find yourself in a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and foreboding.
        """


class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.50:
            self.enemy = enemies.GiantSpider()
            self.alive_text = "A giant spider jumps down from " \
                              "its web in front of you!"
            self.dead_text = "The corpse of a dead spider " \
                             "rots on the ground."
        elif r < 0.80:
            self.enemy = enemies.Ogre()
            self.alive_text = "An ogre is blocking your path!"
            self.dead_text = "A dead ogre reminds you of your triumph."
        elif r < 0.95:
            self.enemy = enemies.BatColony()
            self.alive_text = "You hear a squeaking noise growing louder" \
                              "...suddenly you are lost in s swarm of bats!"
            self.dead_text = "Dozens of dead bats are scattered on the ground."
        else:
            self.enemy = enemies.RockMonster()
            self.alive_text = "You've disturbed a rock monster " \
                              "from his slumber!"
            self.dead_text = "Defeated, the monster has reverted " \
                             "into an ordinary rock."

        super().__init__(x, y)

    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".
                  format(self.enemy.damage, player.hp))


class VictoryTile(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!


        Victory is yours!
        """

world_map = [
    [None,VictoryTile(1,0),None],
    [None,EnemyTile(1,1),None],
    [EnemyTile(0,2),StartTile(1,2),EnemyTile(2,2)],
    [None,EnemyTile(1,3),None]
]

def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
