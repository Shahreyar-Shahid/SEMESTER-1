print("Welcome to PizzaMelt!")

print("I will guide you through the steps for making pizza, including your choices.")

step1 = input("Which dough do you want, thin or thick? ")
while step1.lower() not in ["thin", "thick"]:
    step1 = input("Invalid input. Please choose either 'thin' or 'thick' dough: ")

print(f"You have chosen to go with {step1} dough.")

print("We have 4 types of ingredients: Cheese, Ketchup, Tomato, Chicken. You can only choose 3 types.")

ingredients = ["cheese", "ketchup", "tomato", "chicken"]

def get_ingredient(prompt):
    ingredient = input(prompt).lower()
    while ingredient not in ingredients:
        ingredient = input("Invalid ingredient. Please choose from Cheese, Ketchup, Tomato, Chicken: ").lower()
    return ingredient

print("Take the dough and put it on the counter.")
ingredient1 = get_ingredient("What ingredient do you want to add first? ")
ingredient2 = get_ingredient("What is the second ingredient? ")
ingredient3 = get_ingredient("What is the third ingredient? ")
print(f"You have chosen these ingredients: {ingredient1}, {ingredient2}, and {ingredient3}.")

print("Now, put it in the oven at 450 degrees Celsius.")
temperature = input("What temperature should the oven be set to for heating? ")
while temperature != "450":
    temperature = input("Invalid input. The correct temperature is 450 degrees Celsius. What temperature should the oven be set to for heating? ")
print("Sounds good! This temperature will work!")

print("Now, let the pizza bake for 30 minutes.")

pizza_time = input("How much time did you bake the pizza for? ")
while pizza_time != "30":
    pizza_time = input("Invalid input. The correct baking time is 30 minutes. How much time did you bake the pizza for? ")
print("Pizza is ready!")
