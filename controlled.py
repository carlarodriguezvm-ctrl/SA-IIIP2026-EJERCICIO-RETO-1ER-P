from serial import Serial
import time

puertoCom = "COM3" 
arduino = Serial(port=puertoCom, baudrate=9600, timeout=1)
time.sleep(2)

while True:
    comando = input("Ingrese un comando 1=Encender 0=Apagar S=Salir: ")
    if comando == "1":
        arduino.write(comando.encode())
        print("LED encendido")  
    elif comando == "0":
        arduino.write(comando.encode())
        print("LED apagado")
    elif comando == "S":
        print("Saliendo del programa...")
        break