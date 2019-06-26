from gpiozero import LED
from time import sleep
from random import randint

def all_flash():    #a function that flashes all four LEDs
    red.on()
    blue.on()
    yellow.on()
    green.on()
    sleep(.5)
    red.off()
    blue.off()
    green.off()
    yellow.off()
    sleep(.5)


red = LED(21)   #assigns the red LED to its GPIO pin
yellow = LED(17)    #assigns the yellow LED to its GPIO pin
blue = LED(11)  #assigns the blue LED to its GPIO pin
green = LED(10) #assigns the green LED to its GPIO pin

lights = []     #initializes an empty list


while True:     #infinite loop
    new = randint(1,4)  #creates a random value equal to 1, 2, 3, or 4
    lights.append(new)  #adds the random value to the end of the list

    for light in lights:    #loops through the list of values
        if light == 1:      #turns on the red LED
            red.on()
            sleep(.25)
            red.off()
            sleep(.3)
        elif light == 2:    #turns on the yellow LED
            yellow.on()
            sleep(.25)
            yellow.off()
            sleep(.3)
        elif light == 3:    #turns on the blue LED
            blue.on()
            sleep(.25)
            blue.off()
            sleep(.3)
        elif light == 4:    #turns on the green LED
            green.on()
            sleep(.25)
            green.off()
            sleep(.3)
        else:               #catches errors for the LEDs turning on
            print('ERROR')
            break

    all_flash()         #turns on all the lights to note the end of the pattern
    print(len(lights))  
