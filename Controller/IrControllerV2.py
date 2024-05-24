import sys
from pymata4 import pymata4

class IrControllerV2:

  def __init__(self, boardE):
    self.board = boardE
    self.board.set_pin_mode_digital_input(41, callback=None)
    self.board.set_pin_mode_digital_input(42, callback=None)
    self.board.set_pin_mode_digital_input(43, callback=None)
    self.board.set_pin_mode_digital_input(44, callback=None)
    self.board.set_pin_mode_digital_input(45, callback=None)

  '''
  def sts1(self):
    sts1 =  0 if self.board.digital_read(41)[0] else 1
    return sts1
  '''
  #izquierda
  def sts2(self):
    sts2 =  0 if self.board.digital_read(44)[0] else 1
    return sts2

  #centro
  def sts3(self):
    sts3 =  0 if self.board.digital_read(43)[0] else 1
    return sts3

  #derecha
  def sts4(self):
    sts4 =  0 if self.board.digital_read(42)[0] else 1
    return sts4

  '''
  def sts5(self):
    sts5 =  0 if self.board.digital_read(45)[0] else 1
    return sts5
  '''
  
  def sensorval(self):
    sts1 =  0 if self.board.digital_read(41)[0] else 1
    sts2 =  0 if self.board.digital_read(42)[0] else 1
    sts3 =  0 if self.board.digital_read(43)[0] else 1
    sts4 =  0 if self.board.digital_read(44)[0] else 1
    sts5 =  0 if self.board.digital_read(45)[0] else 1
    sensorval = ''.join([str(sts1), str(sts2), str(sts3), str(sts4), str(sts5)])
    return sensorval
