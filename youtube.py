a=input("")
if a=="youtube.com":
 import pygame
 screen = pygame.display.set_mode((657, 560))
 image = pygame.image.load("youtube_logo.webp").convert_alpha()
 screen.blit(image, (160, 300))  # Display the image at (100, 100) on the screen
 pygame.display.flip()  # Update the display to show the image
 while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False