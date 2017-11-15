class Food:
    def __init__(self, name, carbs, protein, fat):
        self.name = name
        self.carbs = carbs
        self.protein = protein
        self.fat = fat

    def calories(self):
        return self.carbs * 4 + self.protein * 4 + self.fat * 9


class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def calories(self):
        total = 0
        for ingredient in self.ingredients:
            total = total + ingredient.calories()

        return total

    def __str__(self):
        return self.name

pbj = Recipe("Peanut Butter & Jelly", [
    Food(name="Peanut Butter", carbs=6, protein=8, fat=16),
    Food(name="Jelly", carbs=13, protein=0, fat=0),
    Food(name="Bread", carbs=24, protein=7, fat=2)]
)

omelette = Recipe("Omelette du Fromage", [
    Food(name="Eggs", carbs=3, protein=18, fat=15),
    Food(name="Cheese", carbs=5, protein=24, fat=24)
])

recipes = [pbj, omelette]

for recipe in recipes:
    print("{}: {} calories".format(recipe.name, recipe.calories()))
