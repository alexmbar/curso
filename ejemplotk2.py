from Tkinter import *

class interfaz:
    def __init__(self,contenedor):
        self.e1 = Label(contenedor, text="Etiqueta 1",fg = "black", bg = "white")
        self.e2 = Label(contenedor, text="Etiqueta 2", fg = "blue", bg = "black")
        self.e3 = Label(contenedor, text= "Etiqueta 3", fg = "green", bg = "red")
        self.e4= Label(contenedor, text ="Etiqueta 4", fg = "yellow", bg ="pink")
        self.e5= Label(contenedor, text="Etiqueta 5", fg ="brown", bg="green")
        self.e6=Label(contenedor,text="ETiqueta 6", fg ="red",bg = "blue")

        self.e1.grid(column=0,row=0)
        self.e2.grid(column=0,row=1)
        self.e3.grid(column=0,row=2)
        self.e4.grid(column=1,row=0)
        self.e5.grid(column=1,row=1)
        self.e6.grid(column=1,row=2)






ventana = Tk()
miInterfaz= interfaz(ventana)
ventana.mainloop()
