import tkinter as tk
from tkinter import Scrollbar, Text, Entry
import privateGPT
import threading
from PIL import Image, ImageTk
import pyttsx3

# Crea un motor de síntesis de voz
engine = pyttsx3.init()

def enviar_mensaje(event=None):
    # Deshabilitar la entrada y el botón mientras se procesa
    entrada.config(state=tk.DISABLED)
    enviar_boton.config(state=tk.DISABLED)
    
    mensaje = entrada.get()
    
    def procesar_respuesta():
        resp = privateGPT.main(mensaje)
        chat.config(state=tk.NORMAL)
        chat.insert(tk.END, "You: " + mensaje + "\n", "query")
        chat.insert(tk.END, "CRCK: " + resp + "\n", "answer")
        chat.config(state=tk.DISABLED)

        # Habilitar la entrada y el botón nuevamente
        entrada.config(state=tk.NORMAL)
        enviar_boton.config(state=tk.NORMAL)

        # Limpiar el campo de entrada
        entrada.delete(0, tk.END)

        # Convierte y habla la respuesta del chatbot
        engine.say(resp)
        engine.runAndWait()
    
    # Crear un hilo para procesar la respuesta
    thread = threading.Thread(target=procesar_respuesta)
    thread.start()

# Crear la ventana de chat
ventana = tk.Tk()
ventana.title("CRCK")
ventana.geometry("900x700")

# Cargar una imagen en formato .png
imagen = Image.open('C:/Users/Bao5y/Desktop/CRCK.LLM-main/icono.png')
imagen = imagen.resize((32, 32))  # Ajusta el tamaño de la imagen
icono = ImageTk.PhotoImage(imagen)

# Establecer la imagen como icono de la ventana
ventana.iconphoto(False, icono)

# Crear un Frame para el chat
chat_frame = tk.Frame(ventana)
chat_frame.pack(fill=tk.BOTH, expand=True)

# Crear el área de chat
chat = Text(chat_frame, state=tk.DISABLED)
chat.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Agregar una barra de desplazamiento al área de chat
scrollbar = Scrollbar(chat_frame, command=chat.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat.config(yscrollcommand=scrollbar.set)

# Configurar etiquetas de formato
chat.tag_config("query", foreground="black")
chat.tag_config("answer", foreground="red")

# Crear un Frame para el campo de entrada y el botón
entrada_frame = tk.Frame(ventana)
entrada_frame.pack(fill=tk.BOTH, expand=False)

entrada = Entry(entrada_frame, justify='right', font=("Arial", 14))
entrada.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
entrada.bind("<Return>", enviar_mensaje)

enviar_boton = tk.Button(entrada_frame, text="Send", command=enviar_mensaje)
enviar_boton.pack(side=tk.RIGHT)

ventana.mainloop()
