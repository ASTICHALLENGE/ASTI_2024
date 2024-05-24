import socket
import sys
sys.path.append("../Controller")
from MotorControllerV2 import MotorControllerV2 
from GarraController import Garra 
from pymata4 import pymata4

board = pymata4.Pymata4()
m = MotorControllerV2(board)
g = Garra(board)
s = socket.socket()
s.bind(("",4567))
s.listen(10)

print("Inicia Servidor Socket")
while True:
    (sc,addrc) = s.accept()
    print("Cliente conetado: ", addrc)
    continuar = True
    while continuar:
        dato = sc.recv(64)
        if not dato:
            continuar = False
            print("Cliente desconectado")
        else:
            orden = dato.decode()
            print("Orden: ",orden)
            if  "8" == orden.strip():
                m.forward()
            elif "2" == orden.strip():
                m.backward()
            elif "4" == orden.strip():
                m.left()
            elif "6" == orden.strip():
                m.right()
            elif "5" == orden.strip():
                m.stopcar()
            elif "0" == orden.strip():
                m.turnLeft()
            elif "." == orden.strip():
                m.turnRight()
            elif "7" == orden.strip():
                m.PIVOTTurnL()
            elif "9" == orden.strip():
                m.PIVOTTurnR()
            elif "1" == orden.strip():
                m.PIVOTTurnBL()
            elif "3" == orden.strip():
                m.PIVOTTurnBR()
            elif "gstop" == orden.strip():
                g.stop()
            elif "gopen" == orden.strip():
                g.open_fast()
            elif "gclose" == orden.strip():
                g.close_fast()
            elif "90L" == orden.strip():
                m.giro90L()
            elif "90R" == orden.strip():
                m.giro90R()
            elif "Speed-" == orden[0:6]:
                speedCar = orden.strip()
                speedCar = speedCar[6:]
                speedCar = speedCar.split(sep='.')
                speedCar = speedCar[0]
                speedCar = float(speedCar)
                speedCar = int(speedCar)
                m.changeSpeed(speedCar) 
                
            elif orden == "p":
                m.stopcar()
                #GPIO.cleanup()
                exit(0)

s.close()
print("Fin de programa")