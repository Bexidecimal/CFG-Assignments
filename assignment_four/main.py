import requests, json
from logo import skeleton, skeleton_head
from pprint import pprint

def get_monsters():

    endpoint = "http://127.0.0.1:5000/monsters"
    return requests.get(endpoint).json()

def delete_monster_by_id(id):
    endpoint = f"http://127.0.0.1:5000/monster/{id}"
    return requests.delete(endpoint).json()

def add_monster(monster_dict):
    endpoint = "http://127.0.0.1:5000/monster"
    result = requests.post(endpoint, headers={'content-type': 'application/json'}, data=json.dumps(monster_dict))
    return result.json()

def get_monster(id):
    endpoint = f"http://127.0.0.1:5000/monster/{id}"
    return requests.get(endpoint).json()

def list_monsters():
    monsters = get_monsters()
    if monsters is None:
        print("We were unable to retrieve our monsters")
    else:
        for monster in monsters:
            print(f"{monster["monster_id"]}. {monster["monster_name"]}")
    return monsters

def welcome():
    skeleton()
    print("Welcome to "+'\033[32;5m'+"'U pay, we Slay!'"+'\033[0m'+" Monster Hunting with a flare")
    print("""Welcome to our monster database! Where all creatures, creepy and crawly are found.
    If you are having a monster problem, you are in the right place to get all the info you need for a quick extermination.""")

def menu():
    print("Please choose an option from the following list")
    print("Option 1: View the monster database")
    print("Option 2: Add a monster")
    print("Option 3: Delete a monster (This option is for employees only! \033[31;5mDON'T TOUCH\033[0m)")

def keep_running():
    choice = input("Do you wish to go back to the start (Y) or stop (N) ")
    if choice == "N" or choice == "n":
        skeleton_head()
        return False
    return True

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
            print(add_monster(monster_dict))


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
