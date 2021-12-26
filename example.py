import neopixel

numLEDs = 23
cBlue   = (  0,   0, 255)
cCyan   = (  0, 255, 255)
cGreen  = (  0, 255,   0)

                # numLEDs, state machine?, GPIO Pin, 'mode'
pixels = Neopixel(numLEDs,          0,     0,        "RGB")

for lp in range(numLEDs):
    pixels.set_pixel(lpLED, cBlue)
pixels.show()
