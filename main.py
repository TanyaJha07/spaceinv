import pygame

#initialise pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode( (800, 600) )

# Caption and Icon 
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)   

#player
playerimg = pygame.image.load('player.png')
playerX = 20
playerY = 30

def player():
    screen.blit(playerimg, (playerX, playerY))

# GAME LOOP 
running = True
while running:
    
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    player()
    pygame.display.update()







