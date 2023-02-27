import random
num = random.randrange(1,1001)

#mynums = 2
for x in range (1000): 
    tally = 0
    tally = tally + 1
    guess = int(input("Guess the random number between 1 and 1000. "))
    if guess == num:
        print ("Correct!")
        break #break only breaks out of the closest loop, need multiple breaks for nested loops
    elif guess > num:
        print ("Too high!")
    else:
        print ("Too low!")

    #mynums = mynums + 1
    

print (tally)
print ("The number is ", num, ". It took you ", tally, " guesses to get the answer.")


