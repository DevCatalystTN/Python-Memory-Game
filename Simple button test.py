from gpiozero import LED, Button


led = LED(21)
button = Button(13)

while True:
    button.when_pressed = led.on
    button.when_released = led.off
    
