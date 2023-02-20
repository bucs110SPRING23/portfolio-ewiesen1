import random
num = random.randrange(1,11)


for x in range (3):
    guess = int(input("Guess the random number between 1 and 10. "))
    if guess == num:
        print ("Correct!")
        break
    elif guess > num:
        print ("Too high!")
    else:
        print ("Too low!")


    