import tkinter as tk
from tkinter import Scrollbar, Text, Entry
import privateGPT
import threading
from PIL import Image, ImageTk
import pyttsx3

# Create a speech synthesis engine
engine = pyttsx3.init()

def enviar_mensaje(event=None):
    # Disable input and button while processing
    entrada.config(state=tk.DISABLED)
    enviar_boton.config(state=tk.DISABLED)
    
    mensaje = entrada.get()
    
    def procesar_respuesta():
        resp = privateGPT.main(mensaje)
        chat.config(state=tk.NORMAL)
        chat.insert(tk.END, "You: " + mensaje + "\n", "query")
        chat.insert(tk.END, "CRCK: " + resp + "\n", "answer")
        chat.config(state=tk.DISABLED)

        # Enable the input and button again
        entrada.config(state=tk.NORMAL)
        enviar_boton.config(state=tk.NORMAL)

        # Clear the input field
        entrada.delete(0, tk.END)

        # Converts and "speaks" the chatbot's response
        engine.say(resp)
        engine.runAndWait()
    
    # Create a thread to process the response
    thread = threading.Thread(target=procesar_respuesta)
    thread.start()

# Create chat window
ventana = tk.Tk()
ventana.title("CRCK")
ventana.geometry("900x700")

# Upload image .png
imagen = Image.open('C:/Users/Bao5y/Desktop/CRCK.LLM-main/icono.png') # Change directory
imagen = imagen.resize((32, 32))  
icono = ImageTk.PhotoImage(imagen)

# Image as icon
ventana.iconphoto(False, icono)

# Create a Frame for chat
chat_frame = tk.Frame(ventana)
chat_frame.pack(fill=tk.BOTH, expand=True)

# Create chat area
chat = Text(chat_frame, state=tk.DISABLED)
chat.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Adding scroll
scrollbar = Scrollbar(chat_frame, command=chat.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat.config(yscrollcommand=scrollbar.set)

# Labels
chat.tag_config("query", foreground="black")
chat.tag_config("answer", foreground="red")

# Create Frame for entry 
entrada_frame = tk.Frame(ventana)
entrada_frame.pack(fill=tk.BOTH, expand=False)

entrada = Entry(entrada_frame, justify='right', font=("Arial", 14))
entrada.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
entrada.bind("<Return>", enviar_mensaje)

enviar_boton = tk.Button(entrada_frame, text="Send", command=enviar_mensaje)
enviar_boton.pack(side=tk.RIGHT)

ventana.mainloop()

