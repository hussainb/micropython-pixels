
import utime
import neopixel

class PixelBlink:
  def __init__(self, id, R, G, B, interval):
    """
      @param id: number/location of neopixel LED
      @param R: Red color value
      @param G: Green color value
      @param B: Blue color value
      @param interval: LED On/Off interval
    """

    self.id = id
    self.R = R
    self.G = G
    self.B = B
    self.lastUpdatedOn = utime.ticks_ms()
    self.interval = interval
    self.pixelOn = False
    
  def next(self):
    tick = utime.ticks_ms()
    
    if tick >= self.lastUpdatedOn + self.interval:
      
      np[self.id] = (self.R if self.pixelOn else 0, self.G if self.pixelOn else 0, self.B if self.pixelOn else 0)
      self.pixelOn = False if self.pixelOn else True
      self.lastUpdatedOn = tick



class PixelFadeInOut:
  def __init__(self, id, R1,G1,B1, R2,G2,B2, steps, interval):
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
    
    self.id = id
    
    self.r1 = R1
    self.g1 = G1
    self.b1 = B1
    
    self.r2 = R2
    self.g2 = G2
    self.b2 = B2
    
    self.steps = steps
    self.interval = interval
    
    self.direction = "to" # to and from
    
    self.tick = utime.ticks_ms()
    self.lastUpdate = utime.ticks_ms()
    self.itr = 1
    
    np[id] = (R1, G1, B1)
    
  def next(self):
    self.tick = utime.ticks_ms()
    
    # if...else for readibility
    if self.direction == "to":
      r1 = self.r1
      g1 = self.g1
      b1 = self.b1

      r2 = self.r2
      g2 = self.g2
      b2 = self.b2
      
    else:
      r1 = self.r2
      g1 = self.g2
      b1 = self.b2

      r2 = self.r1
      g2 = self.g1
      b2 = self.b1 
    
    
    if (self.tick >= self.lastUpdate + self.interval) and self.itr <= self.steps:
      r = ((r1 * (self.steps - self.itr)) + (r2 * self.itr)) / self.steps
      g = ((g1 * (self.steps - self.itr)) + (g2 * self.itr)) / self.steps
      b = ((b1 * (self.steps - self.itr)) + (b2 * self.itr)) / self.steps
      self.itr = self.itr + 1
      self.lastUpdate = utime.ticks_ms()
      
      np[self.id] = (int(r), int(g), int(b))
      
    if self.itr == self.steps:
      self.itr = 0
      
      if self.direction == "to":
        self.direction = "from"
      else:
        self.direction = "to"

