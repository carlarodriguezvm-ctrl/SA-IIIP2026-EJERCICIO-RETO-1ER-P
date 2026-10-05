import tkinter as tk
from serial import Serial
import time
from unittest.mock import MagicMock  # Permite simular el puerto serie sin Arduino físico


MODO_SIMULACION = True  # <-- Cambia a False cuando conectemos el Arduino real

puertoCom = "COM5" 

if not MODO_SIMULACION:
    # --- LO QUE YA TENÍAMOS: Conexión real con el Arduino ---
    arduino = Serial(port=puertoCom, baudrate=9600, timeout=1)
    time.sleep(2)
else:
    # --- SIMULACIÓN (Para probar sin la placa física) ---
    print("PROBANDO EN MODO SIMULACIÓN (Sin Arduino físico)")
    arduino = MagicMock()
    
    # Simula la respuesta exacta que enviaría el Arduino al recibir cada letra
    def simular_respuesta_arduino(comando_bytes):
        respuestas = {
            b'a': b'LED 1 encendido\n',
            b'A': b'LED 1 apagado\n',
            b'b': b'LED 2 encendido\n',
            b'B': b'LED 2 apagado\n',
            b'c': b'LED 3 encendido\n',
            b'C': b'LED 3 apagado\n',
        }
        # Asigna la respuesta simulada al buffer de lectura de la simulación
        arduino.readline.return_value = respuestas.get(comando_bytes, b'Valor no reconocido\n')

    # Vincula la escritura serial con la respuesta simulada
    arduino.write.side_effect = simular_respuesta_arduino

# INTERFAZ GRÁFICA (TKINTER)
ventana = tk.Tk()
ventana.title("Control de LEDs")
ventana.geometry("300x260")

#Teniamos todo lo relacionado con LED1 
estadoLed1 = False

#agregamos variables de estado para LED2 y LED3
estadoLed2 = False
estadoLed3 = False

# --- LO QUE YA TENÍAMOS: Función para leer lo que responde el Arduino ---
def leerMensajeArduino():
    mensajeLed = arduino.readline().decode().strip()
    print("Respuesta recibida del Arduino:", mensajeLed)
    return mensajeLed


# --- LO QUE YA TENÍAMOS: Control del Botón 1 ---
def controlBoton1():
    global estadoLed1

    if estadoLed1:
        estadoLed1 = False
        botonLed1.config(text="Encender LED 1")
        arduino.write(b'A')  # Comando para apagar LED 1
    else:
        estadoLed1 = True
        botonLed1.config(text="Apagar LED 1")
        arduino.write(b'a')  # Comando para encender LED 1

    lblmensaje.config(text=leerMensajeArduino())

# --- LO QUE AGREGAMOS: Control del Botón 2 ---
def controlBoton2():
    global estadoLed2

    if estadoLed2:
        estadoLed2 = False
        botonLed2.config(text="Encender LED 2")
        arduino.write(b'B')  # Comando para apagar LED 2
    else:
        estadoLed2 = True
        botonLed2.config(text="Apagar LED 2")
        arduino.write(b'b')  # Comando para encender LED 2

    lblmensaje.config(text=leerMensajeArduino())

def controlBoton3():
    global estadoLed3

    if estadoLed3:
        estadoLed3 = False
        botonLed3.config(text="Encender LED 3")
        arduino.write(b'C')  # Comando para apagar LED 3
    else:
        estadoLed3 = True
        botonLed3.config(text="Apagar LED 3")
        arduino.write(b'c')  # Comando para encender LED 3

    lblmensaje.config(text=leerMensajeArduino())



#YA TENÍAMOS: Botón para el LED 1 y agregue para boton 2 y 3
botonLed1 = tk.Button(
    ventana,
    text="Encender LED 1",
    font=("Arial", 12),
    width=16,
    command=controlBoton1
)
botonLed1.place(x=70, y=30)

botonLed2 = tk.Button(
    ventana,
    text="Encender LED 2",
    font=("Arial", 12),
    width=16,
    command=controlBoton2
)
botonLed2.place(x=70, y=80)

botonLed3 = tk.Button(
    ventana,
    text="Encender LED 3",
    font=("Arial", 12),
    width=16,
    command=controlBoton3
)
botonLed3.place(x=70, y=130)


#LO QUE YA TENÍAMOS: Etiqueta para mostrar los mensajes recibidos
lblmensaje = tk.Label(ventana, text="-", font=("Arial", 10, "italic"))
lblmensaje.place(x=40, y=190)

ventana.mainloop()