import random, math, pygame
pygame.init()

screen = pygame.display.set_mode()
screen_size = screen.get_size()
dimensions = [screen_size[0], screen_size[1]]

x = screen_size[0]
y = screen_size[1]
x1 = screen_size[0]/2
y1 = screen_size[1]/2

#screen.fill("pink")
bet = ""

hitboxes = {
    "white": pygame.Rect(0,0,x1,y),
    "black": pygame.Rect(0,0,x1,y)
}
hitboxes["white"].topleft = hitboxes["black"].topright
colors = {
    "white": (255,255,255),
    "black": (0,0,0)
}
for click,hit in hitboxes.items():
    pygame.draw.rect(screen,colors[click],hit)
    font = pygame.font.Font(None, 48)
    text = "To begin the game, please click the black box if you believe black will win,"
    text = font.render(text, True, "blue")
    screen.blit(text, (10, y1))
   
    text2 = "or click the white box if you believe white will win."
    text2 = font.render(text2, True, "blue")
    screen.blit(text2, (10, y1+50))
     # where <x> and<y> are coordinates on screen
pygame.display.flip()

while bet == "":
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if hitboxes["white"].collidepoint(event.pos):
                bet = "white"
            elif hitboxes["black"].collidepoint(event.pos):
                bet = "black"



screen.fill("mistyrose")
pygame.draw.circle(screen, "orange",[x1, y1], y1)
pygame.draw.line(screen, "black", [x1,0], [x1,y])
pygame.draw.line(screen, "black", [x1-y1,y1], [x1+y1,y1])
pygame.display.flip()
pygame.time.wait(500)

points1 = 0 #blackplayer
points2 = 0 #whiteplayer

width = screen_size[1]
for throw in range(10):
    for players in ["player1","player2"]:
        x2 = random.randrange(0,x+1)
        y2 = random.randrange(0,y+1)
        
        distance_from_center = math.hypot(x1-x2, y1-y2) #the distance formula
        is_in_circle = distance_from_center <= width/2 #screen width

        #print(is_in_circle)
        if is_in_circle == True:
            if players == "player1":
                pygame.draw.circle(screen, "black", [x2,y2],12)
                pygame.draw.circle(screen, "green", [x2,y2], 9)
                points1 = points1 + 1
            else:
                pygame.draw.circle(screen, "white", [x2,y2],12)
                pygame.draw.circle(screen, "green", [x2,y2], 9)
                points2 = points2 + 1
            pygame.display.flip()
            pygame.time.wait(500)
        elif is_in_circle == False:
            if players == "player1":
                pygame.draw.circle(screen, "black", [x2,y2],12)
                pygame.draw.circle(screen, "red", [x2,y2], 9)
            else:
                pygame.draw.circle(screen, "white", [x2,y2],12)
                pygame.draw.circle(screen, "red", [x2,y2], 9)
            pygame.display.flip()
            pygame.time.wait(500)
#player1 = black
if points1>points2:
    if bet == "black":
        text3 = "Black wins! You guessed correctly!"
    else:
        text3 = "Black wins! You guessed wrong."
elif points2>points1:
    if bet == "white":
        text3 = "White wins! You guessed correctly!"
    else:
        text3 = "White wins! You guessed wrong."
else:
    text3 = "Tie game."

font = pygame.font.Font(None, 48)
text3 = font.render(text3, True, "black")
screen.blit(text3, (x1, y1)) # where <x> and<y> are coordinates on screen
pygame.display.flip()
pygame.time.wait(2500)



