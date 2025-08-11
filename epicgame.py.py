import pygame
import sys
# Initialize Pygame
pygame.init()
# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('epic game that exists')
# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
def end():
    import os
    print("")
import pygame, sys
end()
def wait(z): print(f"notifaction: you are waiting {z} seconds")
print("hi")
x=0.09
wait(x)                                                                         
player="[:)]"
wait(x)
print(f"{player}")
wait(x)
keypressedtrue=False
def keypressedhash(w):
     del player 
     player=" [:)]"
     wait(x)
     print(player)
     wait(x)
if keypressedtrue==False:
  wait(x)
  print("press w to make your character move")
elif keypressedtrue==True: 
   print("your a hacker get out")
wait(x)
w="w"
keypressedhash(w)
wait(x)
endofgame=False
if endofgame==True:
    pygame.display.set_caption('the end')
    print("you win the epic game now leave")
    pygame.display.quit()
    pygame.quit()
    sys.exit()