import random as rand
import sys

def user_list(userlist,username):
        while True:
            if not userlist or username not in userlist:
                print("""Do you want to add username:
                1. Yes
                2. No""")
                reply = input("Option: ")
                if reply == "1":
                    userlist[username] = []
                    return username, userlist
                elif reply == "2":
                    return username, userlist
                else:
                    print("Enter a valid option: ")
            else:
                print(f"Welcome back, {username}!\n")
                return username, userlist

def breakfast(user, userlist):
    Eggs = ["Sunny-Side Up","Boiled Eggs", "Crispy Fried Eggs", "Fluffy Scrambled Eggs"]
    Meat = ["Ham and sausage", "Ham and bacon", "Steak", "Sardines on bread"]
    while True:
        print("""Which of the following selection do you want:
        1. Eggs only
        2. Meat only
        3. Both""")
        option = int(input("Option Selected: ").strip())
        if option in [1, 2, 3]:
            if option == 1:
                breakfast_choice = rand.choice(Eggs)
                breakfast = f"Your breakfast is {breakfast_choice}.\n"
            elif option == 2:
                breakfast_choice = rand.choice(Meat)
                breakfast =  f"Your breakfast is {breakfast_choice}.\n"
            elif option == 3:
                breakfast_choice = (rand.choice(Eggs), rand.choice(Meat))
                breakfast = f"Your breakfasts are {breakfast_choice[0]} and {breakfast_choice[1]}.\n"

            if user not in userlist:
                return breakfast
            else:
                userlist[user].append(breakfast_choice)
                return breakfast
        else:
            print("Please choose a valid option.\n")

def lunch(user, userlist):
    Sandwiches = ["Basil Chicken Sandwiches", "Salad Sandwiches", "Sausage and Pepper Sandwiches", "Shrimp Sandwiches"]
    Burgers = ["Chicken Burger", "Fish Burger", "Pork Burger", "Vegetarian Burger"]
    while True:
        print("""Which of the following selection do you want:
        1. Sandwiches only
        2. Burgers only
        3. Both""")
        option = int(input("Option Selected: ").strip())
        if option in [1, 2, 3]:
            if option == 1:
                lunch_choice = rand.choice(Sandwiches)
                lunch =  f"Your lunch is {lunch_choice}.\n"
            elif option == 2:
                lunch_choice = rand.choice(Burgers)
                lunch = f"Your lunch is {lunch_choice}.\n"
            elif option == 3:
                lunch_choice = (rand.choice(Sandwiches), rand.choice(Burgers))
                lunch = f"Your lunches are {lunch_choice[0]} and {lunch_choice[1]}.\n"

            if user not in userlist:
                return lunch
            else:
                userlist[user].append(lunch_choice)
                return lunch
        else:
            print("Please choose a valid option.\n")

def dinner(user, userlist):
    Rice = ["Chicken Rice", "Coconut Rice", "Risotto", "Nasi Lemak"]
    Noodles = ["Spaghetti", "Laksa", "Pan Fried Noodles", "Ramen"]
    while True:
        print("""Which of the following selection do you want:
        1. Rice only
        2. Noodles only
        3. Both""")
        option = int(input("Option Selected: ").strip())
        if option in [1, 2, 3]:
            if option == 1:
                dinner_choice = rand.choice(Rice)
                dinner = f"Your dinner is {dinner_choice}.\n"
            elif option == 2:
                dinner_choice = rand.choice(Noodles)
                dinner = f"Your dinner is {dinner_choice}.\n"
            elif option == 3:
                dinner_choice = (rand.choice(Rice), rand.choice(Noodles))
                dinner = f"Your dinners are {dinner_choice[0]} and {dinner_choice[1]}.\n"

            if user not in userlist:
                return dinner
            else:
                userlist[user].append(dinner_choice)
                return dinner
        else:
            print("Please choose a valid option.\n")

def mealtime(option, user=None, userlist=None):
    if option == 1:
        return breakfast(user, userlist)
    elif option == 2:
        return lunch(user, userlist)
    else:
        return dinner(user, userlist)

def selection(option):
    return option in ["1", "2", "3", "4"]

def main():
    userlist = {}
    try:
        while True:
            username = input("Enter your username:")
            print()
            user, userlist = user_list(userlist,username)
            if user in userlist and len(userlist[user]) != 0:
                last_meal = userlist[user][-1]
                if isinstance(last_meal, tuple):
                    if len(last_meal) == 2:
                        print("Your last meal was: " + " and ".join(last_meal))
                    elif len(last_meal) == 3:
                        print("Your last meal was: " + ", ".join(last_meal[:-1]) + ", and " + last_meal[-1])
                else:
                    print(f"Your last meal was: {last_meal}")

            while True:
                print("""Please input the Menu options that you would like:
                1. Breakfast
                2. Lunch
                3. Dinner
                4. Exit""")
                option = input("Option Selected: ").strip()
                print()

                if selection(option):
                    if option == "4":
                        sys.exit()
                    print(mealtime(int(option), user, userlist))
                    break
                else:
                    print("Please choose a valid option.\n")
    except KeyboardInterrupt:
        print("Program Exited.")

if __name__ == "__main__":
    main()
