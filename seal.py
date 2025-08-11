import sys
print("i can clik")
def click():
    while True:
         a=input("would you like to click")
         if a=="yes" or a=="yeah": print("ok") 
         print("spell click to auto click maybe that will work idk")
         if KeyboardInterrupt=="click":
             import os
             del click()
             click()
             return click
click()