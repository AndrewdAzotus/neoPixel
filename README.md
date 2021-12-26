# neoPixel
MicroPython code to control strips of NeoPixels, WS2812

I did not write this, and I wanted to apply my change to whereever I got it from.
However, I could not find the original source so I was unable to apply it there.

Rather than lose it or keep it to myself, I released it here.

basically, use it like this:

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
