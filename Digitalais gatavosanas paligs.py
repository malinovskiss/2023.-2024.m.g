import json

class Recipe:
    def __init__(self, title, description, ingredients, steps, cooking_time):
        self.title = title
        self.description = description
        self.ingredients = ingredients
        self.steps = steps
        self.cooking_time = cooking_time

    def display_recipe(self):
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print("Ingredients:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")
        print("Steps:")
        for i, step in enumerate(self.steps, start=1):
            print(f"{i}. {step}")
        print(f"Cooking Time: {self.cooking_time} minutes\n")


class DigitalCookingAssistant:
    def __init__(self):
        self.recipes = []

    def load_recipes(self, filename="recipes.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                for recipe_data in data["recipes"]:
                    recipe = Recipe(**recipe_data)
                    self.recipes.append(recipe)
        except FileNotFoundError:
            print(f"File {filename} not found. No recipes loaded.")

    def save_recipes(self, filename="recipes.json"):
        data = {"recipes": []}
        for recipe in self.recipes:
            recipe_data = {
                "title": recipe.title,
                "description": recipe.description,
                "ingredients": recipe.ingredients,
                "steps": recipe.steps,
                "cooking_time": recipe.cooking_time,
            }
            data["recipes"].append(recipe_data)

        with open(filename, "w") as file:
            json.dump(data, file, indent=2)
        print(f"Recipes saved to {filename}.")

    def add_recipe(self, recipe):
        self.recipes.append(recipe)
        print(f"Recipe '{recipe.title}' added successfully.")

    def display_recipes(self):
        for i, recipe in enumerate(self.recipes, start=1):
            print(f"{i}. {recipe.title}")

    def get_recipe_by_index(self, index):
        try:
            return self.recipes[index - 1]
        except IndexError:
            print("Invalid recipe index.")
            return None


# Example usage:
assistant = DigitalCookingAssistant()
assistant.load_recipes()

while True:
    print("\nDigital Cooking Assistant Menu:")
    print("1. Display Recipes")
    print("2. Add Recipe")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        assistant.display_recipes()
        recipe_index = int(input("Enter the recipe number to view details (0 to go back): "))
        if recipe_index != 0:
            recipe = assistant.get_recipe_by_index(recipe_index)
            if recipe:
                recipe.display_recipe()
    elif choice == "2":
        title = input("Enter recipe title: ")
        description = input("Enter recipe description: ")
        ingredients = input("Enter ingredients (comma-separated): ").split(", ")
        steps = input("Enter cooking steps (comma-separated): ").split(", ")
        cooking_time = int(input("Enter cooking time (in minutes): "))

        new_recipe = Recipe(title, description, ingredients, steps, cooking_time)
        assistant.add_recipe(new_recipe)
        assistant.save_recipes()
    elif choice == "3":
        print("Exiting Digital Cooking Assistant. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
