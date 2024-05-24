from pymata4 import pymata4
import asyncio
import sys
import time

class MotorControllerV2:
    
    def __init__(self, boardE):
        self.board = boardE
        self.board.set_pin_mode_digital_output(29)
        self.board.set_pin_mode_digital_output(28)
        self.board.set_pin_mode_pwm_output(5)
        
        self.board.set_pin_mode_digital_output(26)
        self.board.set_pin_mode_digital_output(27)
        self.board.set_pin_mode_pwm_output(4)
        
        self.board.set_pin_mode_digital_output(25)
        self.board.set_pin_mode_digital_output(24)
        self.board.set_pin_mode_pwm_output(3)

        self.board.set_pin_mode_digital_output(22)
        self.board.set_pin_mode_digital_output(23)
        self.board.set_pin_mode_pwm_output(2)

        self.automatico = 1
        self.velocityM1 = 254
        self.velocityM2 = 254
        self.velocityM3 = 254
        self.velocityM4 = 254

        self.time_giro_90R=0.83
        self.time_giro_90L=0.80
        self.time_giro_45R=0.53
        self.time_giro_45L=0.53
        
        self.board.pwm_write(5, self.velocityM1)
        self.board.pwm_write(4, self.velocityM2)
        self.board.pwm_write(3, self.velocityM3)
        self.board.pwm_write(2, self.velocityM4)
        
    def forward(self):
        self.board.digital_write(29, 1)
        self.board.digital_write(28, 0)
        self.board.digital_write(26, 0)
        self.board.digital_write(27, 1)
        self.board.digital_write(25, 1)
        self.board.digital_write(24, 0)
        self.board.digital_write(22, 1)
        self.board.digital_write(23, 0)
        
    def backward(self):
        self.board.digital_write(29, 0)
        self.board.digital_write(28, 1)
        self.board.digital_write(26, 1)
        self.board.digital_write(27, 0)
        self.board.digital_write(25, 0)
        self.board.digital_write(24, 1)
        self.board.digital_write(22, 0)
        self.board.digital_write(23, 1)

    def right(self):
        self.board.digital_write(29,1)
        self.board.digital_write(28,0) 
        self.board.digital_write(27,0)
        self.board.digital_write(26,1) 
        self.board.digital_write(24,1)
        self.board.digital_write(25,0)  
        self.board.digital_write(23,0)
        self.board.digital_write(22,1) 

    def left(self):
        self.board.digital_write(28,1)
        self.board.digital_write(29, 0) 
        self.board.digital_write(26,0)
        self.board.digital_write(27,1) 
        self.board.digital_write(24,0)
        self.board.digital_write(25,1)  
        self.board.digital_write(22,0)
        self.board.digital_write(23,1)


    def turnLeft(self):
        self.board.digital_write(28,1)
        self.board.digital_write(29, 0) 
        self.board.digital_write(26,1)
        self.board.digital_write(27,0) 
        self.board.digital_write(25,1)
        self.board.digital_write(24,0) 
        self.board.digital_write(22,1)
        self.board.digital_write(23,0)
        
    def turnRight(self):
        self.board.digital_write(29,1)
        self.board.digital_write(28,0) 
        self.board.digital_write(27,1)
        self.board.digital_write(26,0) 
        self.board.digital_write(24,1)
        self.board.digital_write(25,0) 
        self.board.digital_write(23,1)
        self.board.digital_write(22,0)
        
    def PIVOTTurnL(self):
        self.board.digital_write(28,0)
        self.board.digital_write(29, 0) 
        self.board.digital_write(26,0)
        self.board.digital_write(27,1) 
        self.board.digital_write(25,1)
        self.board.digital_write(24,0) 
        self.board.digital_write(22,0)
        self.board.digital_write(23,0)
        
    def PIVOTTurnR(self):
        self.board.digital_write(28,0)
        self.board.digital_write(29,1) 
        self.board.digital_write(26,0)
        self.board.digital_write(27,0) 
        self.board.digital_write(25,0)
        self.board.digital_write(24,0) 
        self.board.digital_write(22,1)
        self.board.digital_write(23,0)
        
    def PIVOTTurnBR(self):
        self.board.digital_write(28,0)
        self.board.digital_write(29, 0) 
        self.board.digital_write(26,1)
        self.board.digital_write(27,0) 
        self.board.digital_write(25,0)
        self.board.digital_write(24,1) 
        self.board.digital_write(22,0)
        self.board.digital_write(23,0)
        
    def PIVOTTurnBL(self):
        self.board.digital_write(28,1)
        self.board.digital_write(29, 0) 
        self.board.digital_write(26,0)
        self.board.digital_write(27,0) 
        self.board.digital_write(25,0)
        self.board.digital_write(24,0) 
        self.board.digital_write(22,0)
        self.board.digital_write(23,1)
        
    def stopcar(self):
        self.board.digital_write(22, 0)
        self.board.digital_write(23, 0)
        self.board.digital_write(24, 0)
        self.board.digital_write(25, 0)
        self.board.digital_write(26, 0)
        self.board.digital_write(27, 0)
        self.board.digital_write(28, 0)
        self.board.digital_write(29, 0)

    def giroTrasero(self):
        self.board.digital_write(28,0)
        self.board.digital_write(29, 0) 
        self.board.digital_write(26,0)
        self.board.digital_write(27,0) 
        self.board.digital_write(25,0)
        self.board.digital_write(24,1) 
        self.board.digital_write(22,0)
        self.board.digital_write(23,0)


    
    def giro90L(self): # pared Iquierda = 0 Derecha = 1
        self.turnLeft() #slight left turn
        time.sleep(self.time_giro_90L)  
        self.stopcar()
        time.sleep(0.3)

    def giro90R(self): # pared Iquierda = 0 Derecha = 1
        self.turnRight() #slight right turn
        time.sleep(self.time_giro_90R)  
        self.stopcar()
        time.sleep(0.3)

    def giro45L(self): # pared Iquierda = 0 Derecha = 1
        self.turnLeft() #slight left turn
        time.sleep(self.time_giro_45L)  
        self.stopcar()
        time.sleep(0.3)
    
    def giro45R(self): # pared Iquierda = 0 Derecha = 1
        self.turnRight() #slight right turn
        time.sleep(self.time_giro_45R)  
        self.stopcar()
        time.sleep(0.3)

    def changeSpeed(self, speedcar):
        self.velocityM1 = speedcar
        self.velocityM2 = speedcar
        self.velocityM3 = speedcar
        self.velocityM4 = speedcar
        self.board.pwm_write(5, self.velocityM1)
        self.board.pwm_write(4, self.velocityM2)
        self.board.pwm_write(3, self.velocityM3)
        self.board.pwm_write(2, self.velocityM4)
        
    def changeSpeedInd(self, s1, s2, s3, s4):
        self.velocityM1 = s1
        self.velocityM2 = s2
        self.velocityM3 = s3
        self.velocityM4 = s4
        self.board.pwm_write(5, self.velocityM1)
        self.board.pwm_write(4, self.velocityM2)
        self.board.pwm_write(3, self.velocityM3)
        self.board.pwm_write(2, self.velocityM4)
        
    def defaultSpeed(self, speedcar):
        self.velocityM1 = 128
        self.velocityM2 = 128
        self.velocityM3 = 128
        self.velocityM4 = 128
        self.board.pwm_write(5, self.velocityM1)
        self.board.pwm_write(4, self.velocityM2)
        self.board.pwm_write(3, self.velocityM3)
        self.board.pwm_write(2, self.velocityM4)
