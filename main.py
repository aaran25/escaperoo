
import pygame
pygame.init()
Screen_Dimensions = pygame.display.set_mode((1920,1880))
background = pygame.image.load("backgroundhouse.jpg")
while True:
    Scaled_Background = pygame.transform.scale(background, (1950, 1000))
    Screen_Dimensions.blit(Scaled_Background, (0,0))
    pygame. draw. circle(Screen_Dimensions, (0,0,255), (150, 50), 1000, 100)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
#364 x 280