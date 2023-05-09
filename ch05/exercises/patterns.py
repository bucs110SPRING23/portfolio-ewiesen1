def star_pyramid(rows): #rows = levels
    for i in range (1,rows+1):
        print("*" * i) 

def rstar_pyramid(rows):    #rows = levels
    for i in range(rows,0,-1):
        print("*" * i) 

levels = int(input("How many rows are in your pyramid?"))

#range(start, stop, step (step by default is 1))
#scope

star_pyramid(levels)
rstar_pyramid(levels)



    