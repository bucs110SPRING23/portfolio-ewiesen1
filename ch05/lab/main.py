import pygame

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

def graph_coordinates(upper_limit):
    threenplus1_iters_dict = threenp1range(upper_limit)
    coor = threenplus1_iters_dict.items()

    screen = pygame.display.set_mode()
    screen.fill("mistyrose")
    pygame.draw.lines(screen, "black", False, list(coor))
    new_display = pygame.transform.flip(screen, False, True)
    width, height = new_display.get_size()
    new_display = pygame.transform.scale(screen, (width * 5, height * 5))
    screen.blit(new_display, (0, 0))
    max_so_far = (0,0)
    for k,v in coor:
        if v >= max_so_far[1]:
            max_so_far = (k,v)
        else:
            max_so_far = max_so_far
    font = pygame.font.Font(None, 30)
    msg = font.render(str(max_so_far), False, "black", "gray")
    screen.blit(msg, (10,10))
    pygame.display.flip()
    pygame.time.wait(4000)    
    
def main():
    pygame.init()
    upper_limit = int(input("Enter an upper limit:"))
    n = int(input("Enter a start number:"))
    print(threenp1range(upper_limit))
    graph_coordinates(upper_limit)
 
main()




