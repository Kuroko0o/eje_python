print("  ******  Bienvenido al Registro de Promedios por Materias Y Alumnos  ******  ")
print(" ")
print ("*******************************************************")
print(" ")
k = input("Ingresar la cantidad deseada de nombres de alumnos y promedios que desea conseguir: \n")
try:
    cant = int(k)
except :
    print("La Cantidad ingresada no es valida! Intentelo nuevamente reiniciando el registro!")

for cuenta in range(cant):
    a = input("Ingresar nombre de alumno completo: \n")
    b = input("Ingresar la materia (Lengua/Historia/Matematica/Geografia/Quimica/ Etc.): \n")
    c = input("Ingresar Calificación del Primer Trimestre: \n")
    d = input("Ingresar Calificación del Segundo Trimestre: \n")
    e = input ("Ingresar Calificación del Tercer Trimestre: \n")
    try:
        n = float(c)
        nu = float(d)
        num = float(e)
    except :
        print("-----------------------------------------------------------------------------")
        print("Valor ingresado en calificación NO es valido, vuelva a intentarlo!")
        print("-----------------------------------------------------------------------------")
        break
    total = (n + nu + num) / 3
    print("---------------------------------------------------------------------------------")
    print(" El alumno: \n", a , "\n tiene un promedio de: \n", total, "\n en la materia: \n", b)
    print("---------------------------------------------------------------------------------")

print("************************************************************")
print("  ****** Sus promedios fueron mostrados, gracias por usar el registro ******")
