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
        return threenplus1_iters_dict
    
def main():
    #threenp1(100)
    print(threenp1range(100))
    print(threenp1(100))

main()

screen = pygame.display.set_mode()
screen_size = screen.get_size()
dimensions = [screen_size[0], screen_size[1]]
screen.fill("mistyrose")

def graph_coordinates(theenplus1_iters_dict):
    