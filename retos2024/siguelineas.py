import time

from pymata4 import pymata4
from Controller.MotorControllerV2 import MotorControllerV2
from Controller.IrControllerV2 import IrControllerV2 
#==========================CONFIGURATION===============================
# Configuración
board = pymata4.Pymata4()
m = MotorControllerV2(board)
i = IrControllerV2(board)
#==========================APP Pruebas=================================

def follow_line():
    
    while True:
      m.changeSpeedInd(120, 120, 70, 70)
      if i.sts4() and i.sts2():  # Si el LED centro está encendido, sigue adelante
        print("parar")
        m.stopcar()
        # Aquí puedes colocar la lógica para avanzar
        time.sleep(1)
      elif i.sts4() or i.sts5():  # Si el LED izquierdo está encendido, gira a la izquierda
        print("Gira a la derecha")
        m.turnRight()
        # Aquí puedes colocar la lógica para girar a la izquierda
        # Por ejemplo, puedes activar un motor para girar a la izquierda durante un tiempo determinado
        # y luego volver a comprobar el estado de los LEDs
        time.sleep(0.1)  # Por ejemplo, girar durante 1 segundo
      elif i.sts2() or i.sts1():  # Si el LED izquierdo está encendido, gira a la izquierda
        print("Gira a la izquierda")
        m.turnLeft()
        # Aquí puedes colocar la lógica para girar a la izquierda
        # Por ejemplo, puedes activar un motor para girar a la izquierda durante un tiempo determinado
        # y luego volver a comprobar el estado de los LEDs
        time.sleep(0.1)  # Por ejemplo, girar durante 1 segundo
      elif i.sts3():  # Si el LED derecho está encendido, gira a la derecha
        print("Sigue adelante")
        m.forward()
        # Aquí puedes colocar la lógica para girar a la derecha
        # Por ejemplo, puedes activar un motor para girar a la derecha durante un tiempo determinado
        # y luego volver a comprobar el estado de los LEDs
        time.sleep(0.1)  # Por ejemplo, girar durante 1 segundo
#       elif i.sts3() == 0 and i.sts2() == 0 and i.sts4() == 0:  # Si el LED derecho está encendido, gira a la derecha
#         print("no detecta nada")
#         count = 0
#         flag = True
#         if flag:
#             m.turnLeft()
#         else:
#             m.turnRight()
#         # Aquí puedes colocar la lógica para girar a la derecha
#         # Por ejemplo, puedes activar un motor para girar a la derecha durante un tiempo determinado
#         # y luego volver a comprobar el estado de los LEDs
#         count += 1
#         if count >= 150:
#             flag = not flag
#             print(flag)
#         time.sleep(0.025)  # Por ejemplo, girar durante 1 segundo
      else:
        print("parar")
        m.changeSpeed(60)
        m.turnLeft()
        time.sleep(0.01)
        
    
        
follow_line()


