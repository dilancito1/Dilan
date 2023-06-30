#Trabajo N 4

def promedio():
      nota1 = float(input("ingrese la primera nota"))
      nota2 = float(input("ingrese la segunda nota"))
      nota3 = float(input("ingrese la tercera nota"))

      promedio = (nota1, nota2, nota3) / 3

      if promedio >=3:
            print("El alumno aprobo la materia con un promedio final de:",promedio)
      else:
            print("El alumno debe recursar la materia con un promedio final de:", promedio)
promedio()