import requests
import json

#The below allows the API key to be stored separately from the main code in a file that will not be uploaded to github.
file = open("../secrets2", "r")
api_key = file.read()
file.close()

# The below are reusable variables that are used in the while loops and 2 lists that are used to store information returned from the
# API that can then be printed for the user.
choosing = True
adding_recipe = True
recipe_options = []
selected_recipes = []
recipes_added = True

#The below function prints the list of 10 recipes for the user and assigns a number to each one to make picking a
# recipe more user friendly. The +1 is required due to lists being 0 indexed. I have reused this code in multiple places
# so I can ask the user if they would like to see the same list again.
def print_recipe_list(recipes):
    n = 1
    for recipe in recipes:
        print(n, recipe["title"])
        n = n + 1

# The below functions allows me to call the API and have the results returned in a json format. I have reused this code twice as I have
# called 2 different APIs
def call_api(url):
    result = requests.get(url)
    return result.json()


# The below is a function to view the recipes you have chosen to "keep" , the information is stored in another file as a
# dictionary and then returned in a more readable format. This function is used in a few places
def viewing_recipes(initials):
    answer = input("Would you like to view your list of recipes? Y/N ")
    if answer == "Y" or answer == "y":
        # The below opens a file with the users initials, the path is relative to make sure it is reusable. The file is
        # created with these initials elswhere in the code
        file = open(
            f"./{initials}_saved_recipes",
            "r")
        saved_recipes = json.loads(file.read())
        file.close()
        for saved_recipe in saved_recipes:
            print(saved_recipe["title"], saved_recipe["url"])


# The below captures teh first and last name of the user, this allows me to use string slicing to take the initials of the person
# The file with saved recipes will be assigned to their initials.
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

# The below is the dictionary to store the above data and initials
user_details = {
    "first_name" : first_name,
    "last_name" : last_name,
    "initials": f"{first_name[:1]}{last_name[:1]}"
}

# The below is the first while loops, it sets choosing and adding recipes to True to give a condition that allows the while loop
# to continue going. Further down the code I set both these variables to False to stop the loop based on different answers to input.
while choosing == True:
    recipe_options = []
    adding_recipe = True
    ingredients = input("What ingredients would you like to use to make a recipe? (please use a comma to separate ingredients) ")
    # Below is the first use of a function to call the api, based on the list of ingredients provided by the user.
    recipe_return = call_api(f"https://api.spoonacular.com/recipes/findByIngredients?apiKey={api_key}&ingredients={ingredients}&number=10")

    # The below is similar to the function created above to produce the list of recipes, however I didn't use the function here
    # because the first time round the information returned from the API needs to be added to a list in a dictionary format to
    # capture the ID and, title and URL. The ID is required to call the second API for more information on a recipe but it is
    # Not user friendly to ask people to input a whole ID number rather than a list number.
    n = 1
    for recipe in recipe_return:
        #The below is appending the information extracted from the API (the title and the id)
        # putting it in the recipe_options list for later use. the {} is creating the dictionary, with the key and value
        recipe_options.append({"id":recipe["id"], "title":recipe["title"], "url":""})
        print(n, recipe["title"])
        n = n + 1

    # Below is the second while loop, this is the bulk of the question asking
    while adding_recipe == True:
        chosen_recipe = int(input("Which recipe would you like to know more about? Please enter a number "))
        # The below is the second API call, this takes the ID stored in the dictionary and calls the second API to get more information on the recipe chosen
        recipe_details = call_api(f"https://api.spoonacular.com/recipes/{recipe_options[chosen_recipe-1]["id"]}/information?apiKey={api_key}")
        # Take the recipe_options list, take the chosen_recipe number and - 1 because a list is zero indexed and we added 1 previously
        recipe_options[chosen_recipe - 1]["url"] = recipe_details["sourceUrl"]
        print(f"This recipe will take {recipe_details["readyInMinutes"]} minutes and makes {recipe_details["servings"]} servings. For more information click {recipe_details["sourceUrl"]}")

        # The below uses if else statements to move through questions and logiv
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
                    # Below is my function to view the details written to the saved recipes file
                    viewing_recipes(user_details["initials"])
                    ask_again = input("Would you like to find recipes with new ingredients? Y/N ")
                    if ask_again == "Y" or ask_again == "y":
                        choosing = True
                        adding_recipe = False

                    else:
                        choosing = False
                        adding_recipe = False

        else:
            # The below saves the recipe chosen to the file
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