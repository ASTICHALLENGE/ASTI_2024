from pymata4 import pymata4
import asyncio
import sys
import time

class Infrarrojo:
    
    def __init__(self, boardE):
      self.board = boardE
      self.board.set_sampling_interval(100)
      self.INFRARROJO_RIGHT = 14
      self.board.set_pin_mode_analog_input(self.INFRARROJO_RIGHT, callback=None, differential=1)
      #self.board.enable_analog_reporting(self.INFRARROJO_RIGHT, callback=self.my_callback, differential=5)
      self.valueR=9999991
      self.INFRARROJO_LEFT = 15
      self.board.enable_analog_reporting(self.INFRARROJO_LEFT, callback=None, differential=5)
    
    def measureRight(self):
      ite = 1
      sum = 0
      for i in range(21):
          value = self.board.analog_read(self.INFRARROJO_RIGHT)
          if value[0]>0:
              sum  = sum + value[0]
              ite = ite + 1
      if ite>1:
          temporal = sum/(ite-1)
          distance = 17569.7/(temporal ** 1.2062)
          distance = int(distance)
          return distance
      else:
          return 9999999

    def measureLeft(self):
      ite = 1
      sum = 0
      for i in range(21):
          value = self.board.analog_read(self.INFRARROJO_LEFT)
          if value[0]>0:
              sum  = sum + value[0]
              ite = ite + 1
      if ite>1:
          temporal = sum/(ite-1)
          distance = 17569.7/(temporal ** 1.2062)
          distance = int(distance)
          return distance
      else:
          return 9999999
