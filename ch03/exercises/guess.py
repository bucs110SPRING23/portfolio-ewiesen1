import random
num = random.randrange(1,11)


for x in range (3): #remember range starts at 0 and goes until 3 but is not inclusive of 3
    guess = int(input("Guess the random number between 1 and 10. "))
    if guess == num:
        print ("Correct!")
        break #break only breaks out of the closest loop, need multiple breaks for nested loops
    elif guess > num:
        print ("Too high!")
    else:
        print ("Too low!")

#could have done it like this
#for x in range (3): #remember range starts at 0 and goes until 3 but is not inclusive of 3
    #if guess != num:
        #guess = int(input("Guess the random number between 1 and 10. "))
        #if guess == num:
        #    print ("Correct!")
        #elif guess > num:
        #    print ("Too high!")
        #else:
        #    print ("Too low!")