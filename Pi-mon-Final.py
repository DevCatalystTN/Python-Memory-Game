from random import randint              #Allows LEDs to turn on randomly
from gpiozero import LED, Button        #Manages buttons and LEDs
from time import sleep                  #Allows program to pause



red = LED(21)           #Sets the correct GPIO pins for each LED
green = LED(10)  
blue = LED(11)
yellow = LED(17)

# List containing all of the LEDs.
leds = [red, green, blue, yellow]

redB = Button(13)       #Sets GPIO pins for each button
greenB = Button(5)
blueB = Button(27)
yellowB = Button(2)



# The following functions handle button presses.
# The pressed button blinks.  If it was the correct
# button, a "Correct!" message is printed and the
# index is increased.  Otherwise, "Incorrect!" is
# printed and the 'notFailed' boolean is set to 
# false, ending the game.
def redPressed():
    global index
    global notFailed
    
    red.on()
    sleep(.25)
    red.off()
    
    if memory[index] == red:
        print("Correct!")
        index += 1
    else:
        print("Incorrect!")
        notFailed = False

def greenPressed():
    global index
    global notFailed

    green.on()
    sleep(.25)
    green.off()
    
    if memory[index] == green:
        print("Correct!")
        index += 1
    else:
        print("Incorrect!")
        notFailed = False
        
def bluePressed():
    global index
    global notFailed

    blue.on()
    sleep(.25)
    blue.off()
    
    if memory[index] == blue:
        print("Correct!")
        index += 1
    else:
        print("Incorrect!")
        notFailed = False
        
def yellowPressed():
    global index
    global notFailed

    yellow.on()
    sleep(.25)
    yellow.off()
    
    if memory[index] == yellow:
        print("Correct!")
        index += 1
    else:
        print("Incorrect!")
        notFailed = False




user = input("enter 'y' to play... ")       #Asks the user to play

if user == 'y':
    playing = True
else: playing = False

# This list will hold the randomly selected 
# leds to be pressed in order.
memory = []

while playing:          #First loop allows multiple games to be played

    level = 0           #Reset level indicator
    notFailed = True    #Boolean to handle end of game
    
    while notFailed:    #Each iteration of this loop handles a level
    
        # Increase level counter by one, then print current level. (Game will start at level 1)
        level += 1
        print("Begin level " + str(level))
    
        # Turns all LEDs on, then turns them off.
        for led in leds:
            led.on()
        sleep(.5)
        for led in leds:
            led.off()
        sleep(1)
        
        # Generates a random integer from 0 to the length of 
        # the 'leds' list.  That integer is used to select an 
        # LED and add it to the end of the 'memory' list.
        randomLED = leds[randint(0,len(leds)-1)]
        memory.append(randomLED)
        
        # This for loop blinks each LED in 'memory' in order.
        for led in memory:
            led.on()
            sleep(.25)
            led.off()
            sleep(.25)
        
        # 'index' keeps track of our location in the 'memory' list.
        # If the correct button is pressed, 'index' increases by one. (see the functions above)
        index = 0
    
    
        # This loop listens for a button to be pressed. Then is calls the associated function
        # that determines if the correct button was pressed and increases 'index'
        while index < len(memory) and notFailed:
      
            redB.when_pressed = redPressed
            greenB.when_pressed = greenPressed
            blueB.when_pressed = bluePressed
            yellowB.when_pressed = yellowPressed
    
    # Game has ended. Clear the list holding LED order, print final level, and ask to play again.
    memory.clear()
    redB.when_pressed = None
    greenB.when_pressed = None
    blueB.when_pressed = None
    yellowB.when_pressed = None
    
    for i in range(3):
        for led in leds:
            led.on()
        sleep(.2)
        for led in leds:
            led.off()
        sleep(.2)
        
    print("You made it to level " + str(level) + "!")
    user = input("enter 'y' to play again... ")
    if user != 'y':
        playing = False

print("Goodbye!")
