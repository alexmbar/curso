from Tkinter import *

class interfaz:
    def __init__(self,contenedor):
        self.e1 = Label(contenedor, text="Etiqueta 1",fg = "black", bg = "white")
        self.e1.place(x=10,y=30,width=120,height=25)







ventana = Tk()
miInterfaz= interfaz(ventana)
ventana.mainloop()
