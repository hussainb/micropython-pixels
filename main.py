
import neopixel
import pixel


PIN_NO = 4    #Pin D2 on NodeMCU 
LED_COUNT = 4

np = neopixel.NeoPixel(machine.Pin(PIN_NO), LED_COUNT)


p1 = PixelBlink(0, 255, 165, 0, 700)
p2 = PixelFadeInOut(1, 0, 0, 255, 255, 192, 203, 200, 30)
p3 = PixelBlink(2, 34, 139, 34, 700)
p4 = PixelFadeInOut(3, 255, 255, 0, 0, 255, 255, 200, 30)


while True:
  p1.next()
  p2.next()
  p3.next()
  p4.next()
  np.write()
