import sys
import time
from pymata4 import pymata4
import numpy as np

from Controller.MotorControllerV2 import MotorControllerV2 
from Controller.UltrasoundControllerV2 import Ultrasonido 
from Controller.IrControllerV2 import IrControllerV2 
from Controller.ServoControllerV2 import Servo

# Configuración
board = pymata4.Pymata4()
m = MotorControllerV2(board)

def draw():
    m.changeSpeedInd(85, 85, 67, 67)
    m.forward()
    
def giroTraDer():
    m.changeSpeedInd(128, 128, 60, 50)
    m.giroTrasero()
    time.sleep(2.5)
    m.stopcar()
    time.sleep(0.5)
    print("giro ok")
    
def draw2():
    m.changeSpeedInd(85, 85, 69, 69)
    m.backward()
    time.sleep(1.7)

tiempo_inicio = time.time()

while True:
    draw()
    
    if time.time() - tiempo_inicio >= 1.7:
        m.stopcar()
        time.sleep(0.5)
        giroTraDer()
        draw2()
        break
    time.sleep(0.1)
        
print("El bucle se ha detenido despues de 2 segundos.")
m.stopcar()


    
