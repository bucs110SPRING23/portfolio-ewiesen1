import random, math, pygame
pygame.init()

screen = pygame.display.set_mode()
screen_size = screen.get_size()
dimensions = [screen_size[0], screen_size[1]]
#screen_size[0] = x-axis
#screen_size[1] = y-axis
#print(dimensions)

screen.fill("mistyrose")
pygame.draw.circle(screen, "orange",[screen_size[0]/2,screen_size[1]/2],screen_size[1]/2)
pygame.draw.line(screen, "black", [screen_size[0]/2,0], [screen_size[0]/2,screen_size[1]])
pygame.draw.line(screen, "black", [screen_size[0]/2-screen_size[1]/2,screen_size[1]/2], [screen_size[0]/2+screen_size[1]/2,screen_size[1]/2])
pygame.display.flip()
pygame.time.wait(500)

x1 = screen_size[0]/2
y1 = screen_size[1]/2

width = screen_size[1]
for throw in range(10):
    x2 = random.randrange(0,screen_size[0]+1)
    y2 = random.randrange(0,screen_size[1]+1)
    
    distance_from_center = math.hypot(x1-x2, y1-y2) #the distance formula
    is_in_circle = distance_from_center <= width/2 #screen width

    print(is_in_circle)
    if is_in_circle == True:
        pygame.draw.circle(screen, "darkgreen", [x2,y2], 10)
        pygame.display.flip()
        pygame.time.wait(500)
    elif is_in_circle == False:
        pygame.draw.circle(screen, "red", [x2,y2], 10)
        pygame.display.flip()
        pygame.time.wait(500)
pygame.time.wait(2000)


