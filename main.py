import pygame
pygame.init()
Screen_Dimensions = pygame.display.set_mode((1920,1880))
background = pygame.image.load("backgroundhouse.jpg")
NextRoomButton =  pygame.image.load("other_room_button.png")
#Custom_Font= pygame.font('timesnewroman', 32)
Custom_Font = pygame.font.SysFont(("timesnewroman"), 40, 30, 20)
message = Custom_Font.render("INVENTORY", True, (0,0,0))
while True:
    Scaled_Background = pygame.transform.scale(background, (1950, 1000))
    Screen_Dimensions.blit(Scaled_Background, (0,0))
    pygame.draw.circle(Screen_Dimensions, (195, 94, 36), (1860, 60), 48, 10)
    pygame.draw.circle(Screen_Dimensions, (195, 94, 36), (1860, 180), 48, 10)
    pygame.draw.circle(Screen_Dimensions, (195, 94, 36), (1740, 60), 48, 10)
    Screen_Dimensions.blit(message, (1410,30))
    Screen_Dimensions.blit(NextRoomButton,(1200,200))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
#364 x 280
