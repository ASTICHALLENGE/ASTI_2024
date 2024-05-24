from pymata4 import pymata4
import time

class Ultrasonido:
    
    def __init__(self, boardE):
      self.board = boardE
      self.DISTANCE_CM = 0

      self.ECHO_PIN_RIGHT = 53
      self.TRIGGER_PIN_RIGHT = 52
      self.ECHO_PIN_CENTER = 51
      self.TRIGGER_PIN_CENTER = 50
      self.ECHO_PIN_LEFT = 49
      self.TRIGGER_PIN_LEFT = 48
      self.ECHO_PIN_BASTON = 47
      self.TRIGGER_PIN_BASTON = 46
      self.ECHO_PIN_BASTON_LEFT = 39
      self.TRIGGER_PIN_BASTON_LEFT = 38
      
        
      self.board.set_pin_mode_sonar(self.TRIGGER_PIN_RIGHT, self.ECHO_PIN_RIGHT)
      self.board.set_pin_mode_sonar(self.TRIGGER_PIN_CENTER, self.ECHO_PIN_CENTER)
      self.board.set_pin_mode_sonar(self.TRIGGER_PIN_LEFT, self.ECHO_PIN_LEFT)
      self.board.set_pin_mode_sonar(self.TRIGGER_PIN_BASTON, self.ECHO_PIN_BASTON)
      self.board.set_pin_mode_sonar(self.TRIGGER_PIN_BASTON_LEFT, self.ECHO_PIN_BASTON_LEFT)
            
    def measureRight(self):
      distance = self.board.sonar_read(self.TRIGGER_PIN_RIGHT)
      return distance[self.DISTANCE_CM]
 
    def measureLeft(self):
      distance = self.board.sonar_read(self.TRIGGER_PIN_LEFT)
      return distance[self.DISTANCE_CM]

    def measureCenter(self):
      distance = self.board.sonar_read(self.TRIGGER_PIN_CENTER)
      return distance[self.DISTANCE_CM]
    
    def measureBaston(self):
      distance = self.board.sonar_read(self.TRIGGER_PIN_BASTON)
      return distance[self.DISTANCE_CM]
    
    def measureBastonLeft(self):
      distance = self.board.sonar_read(self.TRIGGER_PIN_BASTON_LEFT)
      return distance[self.DISTANCE_CM]