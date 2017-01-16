from Tkinter import *

class interfaz:
    def __init__(self,contenedor):
        self.e1 = Label(contenedor, text="Etiqueta 1",fg = "black", bg = "white")
        self.e2 = Label(contenedor, text="Etiqueta 2", fg = "blue", bg = "black")
        self.e3 = Label(contenedor, text= "Etiqueta 3", fg = "green", bg = "red")

        self.e1.pack(side=TOP)
        self.e2.pack(side=RIGHT)
        self.e3.pack(side=BOTTOM,fill=X)






ventana = Tk()
miInterfaz= interfaz(ventana)
ventana.mainloop()
