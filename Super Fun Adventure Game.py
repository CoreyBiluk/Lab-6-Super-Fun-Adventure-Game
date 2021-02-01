# =-=-=-=-=-=-=-=-=-=-=-=-=
# EETG3024 Lab 6
# Super Fun Adventure Game
# Corey Biluk | W0425561          
# January 29, 2021                
# =-=-=-=-=-=-=-=-=-=-=-=-=

# This is a very short text-based game.
# Audio files are being played by pygame.

## MODULES
import time
import pygame.mixer
#from pygame.mixer import Sound

## Initialize mixer
pygame.mixer.init()                           

## SFX AUDIO FILES
wall = pygame.mixer.Sound('wall.wav')
hum = pygame.mixer.Sound('hum.wav')
whoosh = pygame.mixer.Sound('whoosh.wav')
morning = pygame.mixer.Sound('morning.wav')
floor = pygame.mixer.Sound('wall.wav')
fall = pygame.mixer.Sound('fall.wav')
splat = pygame.mixer.Sound('splat.wav')
death = pygame.mixer.Sound('death.wav')

def game():

## Delay time variables for story flow timing
    dTimeS = 4
    dTimeL = 8   
## Prompt user for name    
    name = input("\n\nPlease enter your name:\n")
    name = name.upper()
## Music starts (1 loop total)
    pygame.mixer.music.load('muzic3a.mp3')
    pygame.mixer.music.play(0)  
## JOKE if dylan tries the game    
    if name == 'DYLAN':             ###--JOKE CODE--TAKE OUT B4 SUBMITTING 
        name = 'Dill Pickle'        ###--JOKE CODE--TAKE OUT B4 SUBMITTING    
## Proper capitalization for user name 
    name = name.capitalize()
## Welcome message
    print("\nWelcome, %s\n\n"% name)
    time.sleep(4.5)
    print("     to\n\n")
    time.sleep(4.5)
    print("Super Fun Adventure Game!!! \n")
    time.sleep(9)
## Loop to print multiple blank lines to blank console window before game starts
    for x in range (20):
        print("\n")
## Ambience starts (infinite loop)    
    pygame.mixer.music.load('ambience.mp3')
    pygame.mixer.music.play(-1)
    time.sleep(dTimeL)
## Game begins
    print("You awaken on the floor of a stone room...\n")
    time.sleep(dTimeS)
    print("You have no idea how you got here...\n")
    time.sleep(dTimeS)
## Prompt user for a choice 
    choice1 = input("What do you do?\n1 - Look around\n2 - Close your eyes and hope this is only a dream\n")
## Determine if user chose option '2'
    if choice1 == '2':
        print("\nYou close your eyes and count to three....\n")
        time.sleep(1)
## For loop for text to count to 3        
        for x in range(3):
            print(x+1)
            time.sleep(0.5)
            print("\n...\n")
            time.sleep(0.5)
        
        print("You open your eyes...\n")
        time.sleep(dTimeS)
        print("This is definitely NOT a dream.\n")
        time.sleep(dTimeL)
## Storyline continues   
    print("\nYou look around...\n")
    time.sleep(dTimeS)
    print("There are no doors or windows in the room.\n")
    time.sleep(dTimeS)
    print('"How did I get here??!!"\n')
    time.sleep(dTimeL)
    print("The north wall has a Button labelled 'X'.\n")
    time.sleep(dTimeS)
    print("The south wall has a button labelled 'O'.\n")
    time.sleep(dTimeS)
## Prompt user for a choice
    choice2 = input("Which button do you choose?\n1 - X\n2 - O\n")
## Determine if user chose option '1'
    if choice2 == '1':
## Stop ambience audio file 
        pygame.mixer.music.stop()
## Print actions and play related sound effects        
        print("The wall opens...\n")
        wall.play()
        time.sleep(dTimeS)
        
        print("Inside the wall is a glowing portal...\n")
        hum.play()
        time.sleep(dTimeL)
        hum.stop()
        
        print("You step into the portal...\n")
        whoosh.play()
        time.sleep(dTimeS)
        
        print("You wake up in your bed...\n")
        morning.play()
        time.sleep(dTimeS)
        morning.stop()
## For loop to generate some dotted lines to add dramatic effect   
        for x in range(3):
            print("...\n")
            time.sleep(1)
            
        print("Was it really just a dream after all???\n")
## Determine if user chose anything other than option '1'
    if choice2 != '1':
## Stop ambience audio file 
        pygame.mixer.music.stop()
## Print actions and play related sound effects  
        print("\nThe floor opens...\n")
        floor.play()
        time.sleep(dTimeS)
        
        print("You fall into the pit...\n")
        fall.play()
        time.sleep(1)
        
        splat.play()
        time.sleep(2)
        splat.stop()  
        print("You died")
        time.sleep(1)
## Play game over sound
        death.play()         
    time.sleep(dTimeS)
## Load music for end of game(1 loop total)
    pygame.mixer.music.load('muzic3a.mp3')
    pygame.mixer.music.play(0)
## Print Credits & Thank you/Replay message  
    print("\nThank you for playing\n")
    time.sleep(4.5)
    print("\nCreated by: Corey\n")
    time.sleep(4.5)
    print("\nSound Design by: Corey\n")
    time.sleep(4.5)
    print("\nMusic by: Corey\n")
    time.sleep(4.5)
    print("Press F5 to play again")
           
if __name__=='__main__':
    game()