import pygame
pygame.init()

screen = pygame.display.set_mode()

screen.fill("blue")
pygame.display.flip()
pygame.time.wait(1000)

screen_size = screen.get_size()

dimensions = [screen_size[0]/2, screen_size[1]/2,250,250]
#display = 50
#display = int(display)
#display = display/4
pygame.draw.circle(screen, "white", [675,500], 150)
#pygame.display.flip()
pygame.draw.circle(screen, "white", [675,300], 100)
#pygame.display.flip()
pygame.draw.circle(screen, "white", [675,170], 50)
#pygame.display.flip()
pygame.draw.circle(screen, "black", [655,150], 5)
#pygame.display.flip()
pygame.draw.circle(screen, "black", [695,150], 5)
pygame.display.flip()
#pygame.draw.circle(screen, "orange", [675,160], 5)
#pygame.display.flip()

#[x,y,width,height]
dimensions =  [675, 160, 4, 15]
pygame.draw.rect(screen, "orange", dimensions)
pygame.display.flip()
#dimensions =  [665, 185, 25, 4]
#pygame.draw.rect(screen, "red", dimensions)
#pygame.display.flip()

pygame.time.wait(3000)
