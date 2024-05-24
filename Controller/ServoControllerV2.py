from pymata4 import pymata4
import time

class Servo:
    def __init__(self, boardE):
        self.board = boardE
        self.board.set_pin_mode_servo(35)
        self.board.set_pin_mode_servo(12)
        self.board.servo_write(35, 180)
        self.board.servo_write(12, 255)

    def changeAngle(self, angle):
        angle = int(angle)
        self.board.servo_write(35, angle)
