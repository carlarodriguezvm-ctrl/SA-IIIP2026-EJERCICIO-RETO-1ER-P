import tkinter as tk
from serial import Serial
import time

puertoCom = "COM5" 
arduino = Serial(port=puertoCom, baudrate=9600, timeout=1)
time.sleep(2)

ventana = tk.Tk()
ventana.title("Control Led")
ventana.geometry("250x200")

estadoLed = False
# arduino.write(b'0')

def leerMensajeArduino():
    mensajeLed = arduino.readline().decode().strip()
    print(mensajeLed)
    return mensajeLed


def controlBoton():
    global estadoLed

    if estadoLed:
        estadoLed = False
        botonLed1.config(text="Encender Led")
        arduino.write(b'0')
    else:
        estadoLed = True
        botonLed1.config(text="Apagar Led")
        arduino.write(b'1')

    lblmensaje.config(text=leerMensajeArduino())


botonLed1 = tk.Button(
    ventana,
    text="Encender Led",
    font=("Arial", 14),
    command=controlBoton
)

botonLed1.place(x=40, y=60)

lblmensaje = tk.Label(ventana, text="-")
lblmensaje.place(x=40, y=160)

ventana.mainloop()