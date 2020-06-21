asignatura = ["Lengua","Historia","Matematica", "Quimica", "Dibujo", "Biologia"]
print("******  Bienvenido, Siga las instrucciones y Complete el Formulario  ******")
print("*********************************************************")
print(" ")
print("---------------------------------------------------")
nombre = input ("Ingrese su nombre completo: \n")
print("----------------------------------------------------")
materia = input("""Ingrese la materia que le corresponda:

1) Lengua
2) Historia
3) Matematica
4) Quimica
5) Dibujo
6) Biologia
*****************************************************

""")

print("****************************************************")
indice = asignatura.index(materia)
curso = asignatura [indice]

print("----------------------------------------------------")
print("----------------------------------------------------")
print("El alumno:\n", nombre)
print("Estudia actualmente la materia de :\n", curso)
print(" ")
print("----------------------------------------------------")
print("----------------------------------------------------")
