import requests, json
from logo import skeleton, skeleton_head
from pprint import pprint

#The below connects to the endpoint to get all monsters in the DB
def get_monsters():

    endpoint = "http://127.0.0.1:5000/monsters"
    return requests.get(endpoint).json()

# The below connects to the endpoint to delete a singular monster by ID
def delete_monster_by_id(id):
    endpoint = f"http://127.0.0.1:5000/monster/{id}"
    return requests.delete(endpoint).json()

# The below connects to the endpoint to add a monster to the DB and then return the results to show this has been done properly.
def add_monster(monster_dict):
    endpoint = "http://127.0.0.1:5000/monster"
    result = requests.post(endpoint, headers={'content-type': 'application/json'}, data=json.dumps(monster_dict))
    return result.json()

# The below connects to the endpoint to get a singular monster by ID
def get_monster(id):
    endpoint = f"http://127.0.0.1:5000/monster/{id}"
    return requests.get(endpoint).json()

# The below is a function that will check whether a valid input has been given and to print the monster ID and name
def list_monsters():
    monsters = get_monsters()
    if monsters is None:
        print("We were unable to retrieve our monsters")
    else:
        for monster in monsters:
            print(f"{monster["monster_id"]}. {monster["monster_name"]}")
    return monsters

# Below is the welcome message
def welcome():
    skeleton()
    print("Welcome to "+'\033[32;5m'+"'U pay, we Slay!'"+'\033[0m'+" Monster Hunting with a flare")
    print("""Welcome to our monster database! Where all creatures, creepy and crawly are found.
    If you are having a monster problem, you are in the right place to get all the info you need for a quick extermination.""")

# Below is the menu of options
def menu():
    print("Please choose an option from the following list")
    print("Option 1: View the monster database")
    print("Option 2: Add a monster")
    print("Option 3: Delete a monster (This option is for admin only! \033[31;5mDON'T TOUCH\033[0m)")

# Below is the function which checks whether the user wants to continue with other actions and will close the while loop if no longer needed
def keep_running():
    choice = input("Do you wish to go back to the start (Y) or stop (N) ")
    if choice == "N" or choice == "n":
        skeleton_head()
        return False
    return True

# Below is the main code for the user interface, using a while loop and if statements to take the user through a series of options
# to view the info in the DB, add info and delete info as needed.
def run():
    welcome()
    running = True

    while running == True:
        menu()

        option = input("Choose an option 1, 2 or 3? Please input a number. ")

        if option == "1":
            monster = list_monsters()
            if monster:
                which_monster = input("Please enter the number of the monster you wish to view. ")
                pprint(get_monster(which_monster))


        elif option == "2":
            print("Please input the information of your monster when prompted")
            monster_dict = {
                "monster_name" : input("What is the name of your monster? e.g. Ghost. "),
                "country_id" : int(input(
                    "Which country does the monster originate? Please choose a number \n"
                    "1. Haiti\n"
                    "2. Greece\n"
                    "3. Romania\n"
                    "4. America\n"
                    "5. Unknown. "
                )),
                "weakness" : input("What is the monster weak against? e.g. Ghostbuster. "),
                "favourite_food" : input("What is the monsters favourite food? e.g. Cake. "),
                "identifying_features" : input("What are the identifying features of the monster? e.g. Translucent but green. "),
                "url" : input("Please input a website that had more information on your monster. ")
            }
            print(add_monster(monster_dict)) # I added the user input questions to the values in the dictionary to make it a little more efficient


        elif option == "3":
            list_monsters()
            delete_monster = input("Which monster would you like to delete? Please input the monster_id to proceed. ")
            if not delete_monster:
                print("You did not enter a valid input")
            else:
                print(delete_monster_by_id(delete_monster))
        else:
            print("Invalid option. Please select either 1, 2 or 3")

        running = keep_running()

    return "Goodbye, happy hunting"

if __name__ == "__main__":
    print(run())
