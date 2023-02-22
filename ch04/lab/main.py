import random, math, pygame
pygame.init()

screen = pygame.display.set_mode()
screen_size = screen.get_size()
dimensions = [screen_size[0], screen_size[1]]
#screen_size[0] = x-axis
#screen_size[1] = y-axis
#print(dimensions)

#hit_box_width = screen_size[0] / 2
#hit_box_height = screen_size[1]

#hitboxes = {
#    "black": pygame.Rect(0, 0, hit_box_width, hit_box_height),
#    "white": pygame.Rect(0, 0, hit_box_width, hit_box_height)    
#}

#hitboxes["black"].topleft # = hitboxes["red"].topright
#hitboxes["white"].topright #= hitboxes["red"].bottomright
#hitboxes["purple"].topleft = hitboxes["red"].bottomright

screen.fill("steelblue")
pygame.draw.circle(screen, "orange",[screen_size[0]/2,screen_size[1]/2],screen_size[1]/2)
pygame.draw.line(screen, "black", [screen_size[0]/2,0], [screen_size[0]/2,screen_size[1]])
pygame.draw.line(screen, "black", [screen_size[0]/2-screen_size[1]/2,screen_size[1]/2], [screen_size[0]/2+screen_size[1]/2,screen_size[1]/2])
pygame.display.flip()
pygame.time.wait(500)

x1 = screen_size[0]/2
y1 = screen_size[1]/2

points1 = 0
points2 = 0
width = screen_size[1]
for throw in range(10):
    for players in ["player1", "player2"]:
        x2 = random.randrange(0,screen_size[0]+1)
        y2 = random.randrange(0,screen_size[1]+1)
        
        distance_from_center = math.hypot(x1-x2, y1-y2) #the distance formula
        is_in_circle = distance_from_center <= width/2 #screen width

        #print(is_in_circle)
        if is_in_circle == True:
            if players == "player1":
                pygame.draw.circle(screen, "black", [x2,y2], 12)
                pygame.draw.circle(screen, "green", [x2,y2], 9)
                points1 = points1 + 1
            else: 
                pygame.draw.circle(screen, "white", [x2,y2], 12)
                pygame.draw.circle(screen, "green", [x2,y2], 9)
                points2 = points2 + 1

            pygame.display.flip()
            pygame.time.wait(500)

        elif is_in_circle == False:
            if players == "player1":
                pygame.draw.circle(screen, "black", [x2,y2], 12)
                pygame.draw.circle(screen, "red", [x2,y2], 9)
            else: 
                pygame.draw.circle(screen, "white", [x2,y2], 12)
                pygame.draw.circle(screen, "red", [x2,y2], 9)
            pygame.display.flip()
            pygame.time.wait(500)
    
    pygame.time.wait(1000)

print("Player 1 score: ", points1)
print("Player 2 score: ", points2)

if points1>points2:
    text = "Player 1 wins!"
elif points2>points1:
    text = "Player 2 wins!"
else:
    text = "Tie game."


font = pygame.font.Font(None, 48)
text = font.render(text, True, "white")
screen.blit(text, (x1, y1)) # where <x> and<y> are coordinates on screen
pygame.display.flip()
pygame.time.wait(2500)

