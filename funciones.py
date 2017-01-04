# Calculo de areas
F=3.141516
#Area del cuadrado
def acuadrado():
    lado = input("Cual es el valor del lado?")
    x = lado**2
    print "\nEl area del cuadrado es", x,"unidades cuadradas"

#Area del triangulo
def atriangulo():
    base = input("Cual es el valor de la base?")
    altura = input("Cual es el valor de la altura")
    y = base * altura /2
    print "\nEl area del triangulo es ", y, "unidades cuadradas"

#Area del circulo
def acirculo():
    radio = input("Cual es el valor del radio?")
    z = (F * radio) ** 2
    print "\nEl area del circulo ", z, "unidades cuadradas"

i=True
while i==True:

    area = input ("\nElije la figura geometrica para calcular su area \nCuadrado  = 1 \nTriangulo = 2 \nCirculo = 3\n")

    if area==1:
        acuadrado()
    elif area==2:
        atriangulo()
    elif area==3:
        acirculo()
    else:
        print "Ingresa una opcion validada"

    i = input ("\nQuieres calcular el area de otra figura? \n Si=True \nNo=False\n1")


