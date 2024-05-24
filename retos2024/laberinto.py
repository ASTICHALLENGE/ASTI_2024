import sys
import time
from pymata4 import pymata4
import threading
import _thread
import numpy as np

from Controller.MotorControllerV2 import MotorControllerV2 
from Controller.UltrasoundControllerV2 import Ultrasonido 
from Controller.IrControllerV2 import IrControllerV2 
from Controller.ServoControllerV2 import Servo

# Configuración
board = pymata4.Pymata4()
m = MotorControllerV2(board)
u = Ultrasonido(board)

# Variables globales
disLimiteParedFrontal = 25
disLimiteParedLateral = 25
disCen = 100

# Función para determinar dirección de giro
def determinarDireccionGiro():
    distanciaIzquierda = u.measureLeft()
    distanciaDerecha = u.measureRight()
    distanciaCentro = u.measureCenter()
    
    if distanciaIzquierda > (distanciaDerecha and distanciaCentro):
        return "izquierda"
    elif distanciaDerecha > (distanciaIzquierda and distanciaCentro):
        return "derecha"
    elif distanciaCentro > (distanciaDerecha and distanciaIzquierda):
        return "avanzar"

# Función para avanzar en línea recta
def avanzaLineaRecta():
    print("Avanzando en línea recta...")
    while True:
        m.forward()  # Avanzar
        
        distanciaCen = u.measureCenter()  # Medir distancia al frente
        distanciaIzq = u.measureLeft()  # Medir distancia a la izquierda
        distanciaDer = u.measureRight()  # Medir distancia a la derecha
        
        print("Distancia al frente:", distanciaCen)
        print("Distancia a la izquierda:", distanciaIzq)
        print("Distancia a la derecha:", distanciaDer)
        
        if distanciaCen < disLimiteParedFrontal:  # Si detecta un obstáculo al frente
            print("Obstáculo detectado al frente.")
            m.stopcar()  # Detener el avance
            # Determinar hacia dónde girar
            direccionGiro = determinarDireccionGiro()

            if direccionGiro == "izquierda":
                print("Girando a la izquierda...")
                m.turnLeft()  # Girar a la izquierda
            elif direccionGiro == "derecha":
                print("Girando a la derecha...")
                m.turnRight()  # Girar a la derecha
            else: 
                print("Avanzando")
                m.forward()
                
                
            time.sleep(1)  # Tiempo para completar el giro
            
            m.stopcar()  # Detenerse después del giro
            break  # Salir del bucle de avance en línea recta
            
        elif distanciaIzq < disLimiteParedLateral:  # Si detecta un obstáculo a la izquierda
            print("Obstáculo detectado a la izquierda.")
            m.stopcar()
            time.sleep(1)
            m.turnRight()
            time.sleep(0.5)
            m.stopcar()
            break
            
        elif distanciaDer < disLimiteParedLateral:  # Si detecta un obstáculo a la derecha
            print("Obstáculo detectado a la derecha.")
            m.stopcar()
            time.sleep(1)
            m.turnLeft()
            time.sleep(0.5)
            m.stopcar()
            break

# Avanzar durante 1 segundo antes de iniciar el bucle principal
print("Iniciando movimiento hacia adelante...")
m.forward()
time.sleep(1)
m.stopcar()

# Bucle principal
while True:
    avanzaLineaRecta()  # Llamar a la función para avanzar en línea recta

