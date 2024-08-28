"""
Docstring
"""

import json


def adjust_recipe(recipe, quantity):
    adjusted = {}
    for ingredient, q in recipe['ingredients'].items():
        adjusted[ingredient] = q * (quantity / recipe['servings'])

    return {key: (
        adjusted if key == 'ingredients' else quantity if key == 'servings' else value
    )
            for key, value in recipe.items()}


def load_recipe(raw):
    return json.loads(raw)


if __name__ == '__main__':
    # Beispiel für die Datenstruktur eines Rezepts
    recipe_json = '{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, ' \
                  '"Minced Meat": 500}, "servings": 4}'
