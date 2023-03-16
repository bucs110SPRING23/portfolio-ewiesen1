import pygame
pygame.init()

def threenp1(n):
    count = 0
    while n > 1.0:
       count = count + 1
       if n % 2 == 0:
        n = int(n / 2)
       else:
        n = int(3 * n + 1)
    return count

def threenp1range(upper_limit):
    threenplus1_iters_dict = {}
    for n in range (2, upper_limit+1):
        threenplus1_iters_dict[n] = threenp1(n)
    return threenplus1_iters_dict, threenplus1_iters_dict.items()
    
    
def main():
    upper_limit = int(input("Enter an upper limit:"))
    n = int(input("Enter a start number:"))
    print(threenp1range(upper_limit))
    print(threenp1(n))

def graph_coordinates(theenplus1_iters_dict):
    screen = pygame.display.set_mode()
    screen.fill("mistyrose")
    screen_size = screen.get_size()
    dimensions = [screen_size[0], screen_size[1]]
    #coor = threenp1range()
    #threenp1range()
    #threenplus1_iters_dict[n] = threenp1(n)
    pygame.draw.lines(screen, "black", True,)

main()




