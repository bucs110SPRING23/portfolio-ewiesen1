#food_name, cuisine
from advice import Advice
from trump import DTJoke

def main():
    print("We all struggle. To help you feel better, I want to give you some advice.")

    while True:
        choice = input("Press 1 to receive advice. ")

        if choice == "1":
            adv = Advice().get_advice()
            print ("...") #formatting
            print(adv)
            print("...") #formatting
            break
        else:
            print("Invalid choice. Please press 1 to continue. ")

    print("Did this advice help?")

    while True:
        choice2 = input("Yes or No (enter 'y' for yes and 'n' for no). ")

        if choice2.lower() == "y":
            print("See you next time!")
            break
        elif choice2.lower() == "n":
            print("To help you feel better, I will also offer a dumb quote from our former president, Trump.\n... ")
            trump = DTJoke().get_joke()
            print("Trump: ",trump)
            print("...") #formatting
            break
        else:
            print("Invalid choice. Please enter 'y' or 'n to continue. ")

    
if __name__ == "__main__":
    main()