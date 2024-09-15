import requests
import json

file = open("../secrets2", "r")
api_key = file.read()
file.close()

choosing = True
adding_recipe = True
recipe_options = []
selected_recipes = []
recipes_added = True

def print_recipe_list(recipes):
    n = 1
    for recipe in recipes:
        print(n, recipe["title"])
        n = n + 1

def call_api(url):
    result = requests.get(url)
    return result.json()

def viewing_recipes(initials):
    answer = input("Would you like to view your list of recipes? Y/N ")
    if answer == "Y" or answer == "y":
        file = open(
            f"./{initials}_saved_recipes",
            "r")
        saved_recipes = json.loads(file.read())
        file.close()
        for saved_recipe in saved_recipes:
            print(saved_recipe["title"], saved_recipe["url"])



first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

user_details = {
    "first_name" : first_name,
    "last_name" : last_name,
    "initials": f"{first_name[:1]}{last_name[:1]}"
}

while choosing == True:
    recipe_options = []
    adding_recipe = True
    ingredients = input("What ingredients would you like to use to make a recipe? (please use a comma to separate ingredients) ")
    recipe_return = call_api(f"https://api.spoonacular.com/recipes/findByIngredients?apiKey={api_key}&ingredients={ingredients}&number=10")


    n = 1
    for recipe in recipe_return:
        #The below is appending the information extracted from the API (the title and the id)
        # putting it in the recipe_options list for later use. the {} is creating the dictionary, with the key and value
        recipe_options.append({"id":recipe["id"], "title":recipe["title"], "url":""})
        print(n, recipe["title"])
        n = n + 1

    while adding_recipe == True:
        chosen_recipe = int(input("Which recipe would you like to know more about? Please enter a number "))
        # Take the recipe_options list, take the chosen_recipe number and - 1 because a list is zero indexed and we added 1 previously
        recipe_details = call_api(f"https://api.spoonacular.com/recipes/{recipe_options[chosen_recipe-1]["id"]}/information?apiKey={api_key}")

        recipe_options[chosen_recipe - 1]["url"] = recipe_details["sourceUrl"]
        print(f"This recipe will take {recipe_details["readyInMinutes"]} minutes and makes {recipe_details["servings"]} servings. For more information click {recipe_details["sourceUrl"]}")

        recipe_list_question = input("Would you like to keep this recipe? Y/N ")
        if recipe_list_question == "N" or recipe_list_question == "n":
            adding_recipe = False
            end = input("Would you like to look for more recipes with the same ingredients? Y/N ")
            if end == "Y" or end == "y":
                adding_recipe = True
                choosing = True
            else:
                beginning = input("Would you like to look for recipes with different ingredients? Y/N ")
                if beginning == "Y" or beginning == "y":
                    choosing = True
                    adding_recipe = False
                else:
                    viewing_recipes(user_details["initials"])
                    ask_again = input("Would you like to find recipes with new ingredients? Y/N ")
                    if ask_again == "Y" or ask_again == "y":
                        choosing = True
                        adding_recipe = False

                    else:
                        choosing = False
                        adding_recipe = False

        else:
            selected_recipes.append(recipe_options[chosen_recipe - 1])
            file = open(f"./{user_details["initials"]}_saved_recipes", "w")
            file.write(json.dumps(selected_recipes))
            file.close()
            recipes_added = input("Would you like to look for more recipes with the same ingredients? Y/N ")
            if recipes_added == "Y" or recipes_added == "y":
                choosing = True
                print_recipe_list(recipe_return)

            else:
                viewing_recipes(user_details["initials"])

                ask_again = input("Would you like to find recipes with new ingredients? Y/N ")
                if ask_again == "Y" or ask_again == "y":
                    choosing = True
                    adding_recipe = False

                else:
                    choosing = False
                    adding_recipe = False

print("Thank you for using this program")