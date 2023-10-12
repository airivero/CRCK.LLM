import tkinter as tk
from tkinter import Scrollbar, Text, Entry
import privateGPT 

def enviar_mensaje():
    mensaje = entrada.get()
    resp = privateGPT.main(mensaje)
    if mensaje:
        chat.config(state=tk.NORMAL)
        chat.insert(tk.END, "You: " + mensaje + "\n")
        chat.insert(tk.END, "CRCK: " + resp + "\n")
        chat.config(state=tk.DISABLED)
        entrada.delete(0, tk.END)

# Crear la ventana de chat
ventana = tk.Tk()
ventana.title("CRCK")



# Crear el área de chat
chat = Text(ventana, state=tk.DISABLED, )
chat.pack(fill=tk.BOTH, expand=True)

# Agregar una barra de desplazamiento
scrollbar = Scrollbar(ventana)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=chat.yview)

# Crear un Frame para el campo de entrada y el botón
entrada_frame = tk.Frame(ventana)
#entrada_frame.pack(fill=tk.BOTH, expand=True)
entrada_frame.pack(fill=tk.BOTH, expand=False)

#entrada = Entry(entrada_frame, justify='right')
entrada = Entry(entrada_frame, justify='right', font=("Helvetica", 12))
entrada.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


enviar_boton = tk.Button(entrada_frame, text="Send", command=enviar_mensaje)
enviar_boton.pack(side=tk.RIGHT)



ventana.mainloop()