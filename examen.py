edad = input("Ingresa tu edad: ")
"""genero = input("Genero (M/F): ")"""
genero="m"
if(int(edad) >= 18):
     if(genero == "M" or genero == "m"):
          print("ID: " + "MA" + edad + "+")
     else:
          print("ID: " + "FE" + edad + "+")
else:
     if(genero == "F" or genero == "f"):
          print("ID: " + "Fe" + edad + "-")
     else:
          print("ID:12 " + "Ma" + edad + "-")