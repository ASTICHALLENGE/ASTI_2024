from pymata4 import pymata4
import time

class Garra:
    def __init__(self, boardE):
        self.board = boardE
        self.board.set_pin_mode_servo(36)
        self.board.servo_write(36, 100)

    def stop(self):
        self.board.servo_write(36, 100)
    def close_slow(self):
        self.board.servo_write(36, 90)
    def open_slow(self):
        self.board.servo_write(36, 110)
    def open_fast(self):
        self.board.servo_write(36, 120)
    def close_fast(self):
        self.board.servo_write(36, 80)
    
