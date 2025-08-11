import pygame
import sys
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)
a=input("hey")
chrome_options.binary_location = r"C:\Desktop\BraveSoftware\Brave-Browser\Shortcut\Brave"
def warnthunder():
    webdriver.get("https://www.weather.gov/grr/")
    print("hey there is a thunder storm or something like that")
    pygame.init()
    pygame.display.set_mode((657, 560))
    pygame.display.set_caption('thunder!!!!!!1111111!')
    pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
             running=False 
    print("ayyy dawg")
if a=="sos" or a=="help" or a=="there is thunder":
   warnthunder()    