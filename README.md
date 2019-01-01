# Micropython-pixels

Micropython classes to animate neopixels

## Getting Started

Upload the pixel.py to your device using uPyCraft IDE
import pixel in your main.py
follow examples in main.py from the repository

### Prerequisites
Neopixels/ws2812b strip
NodeMCU or ESP32
Basic knowledge of electronics


## Guide to get started with micropython on ESP8266

* [Get started with micropython](https://randomnerdtutorials.com/getting-started-micropython-esp32-esp8266/)


## Docs
Import the pixel module in your main.py
```
import pixel
```
The module exposes the below two classes

* **PixelBlink**

Initialize an Object as shown below

```
p1 = PixelBlink(0, 255, 165, 0, 700)
    """
      @param id: number/location of neopixel LED
      @param R: Red color value
      @param G: Green color value
      @param B: Blue color value
      @param interval: LED On/Off interval
    """
```	
	
The Object p1 now has a method `next()` which when called updates the neopixel LED with its next state


* **PixelFadeInOut**

Initialize an Object as shown below

```
p2 = PixelFadeInOut(1, 0, 0, 255, 255, 192, 203, 200, 30)
    """
      @param id: number/location of neopixel LED
      @param R1: Red color value to begin from
      @param G1: Green color value to begin from
      @param B1: Blue color value to begin from
      
      @param R2: Red color value to end to
      @param G2: Green color value to end to
      @param B2: Blue color value to end to
      @param steps: No of times updates to be performed on LED in given interval
      @param interval: transition to complete in given interval
    """
```	
	
The Object p2 now has a method `next()` which when called updates the neopixel LED with its next state



## Authors

* **Hussain Bharmal** - *Initial work* - [hussainb](https://github.com/hussainb)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

