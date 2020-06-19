print ("  ****** Bienvenido a Calculadora Basica 2020 ******   ")
print (" -------------------------------------------------------- ")
num = input("Ingresar el número entero a calcular: \n")
calculo = input("Ingresar el simbolo de la operación que desea realizar: (+,-,*,/) \n")
num_dos = input("Ingresar el siguiente número a calcular: \n")

try:
    n = float(num)
    nu = float(num_dos)
except:
    print(" -------------------------------------------------------- ")
    print("El Valor ingresado no es un número")
    quit()


if calculo == "+":
    print("El resultado de la suma es: \n", n + nu)
elif calculo == "-":
    print("El resultado de la resta es: \n", n - nu)
elif calculo == "*":
    print("El resultado de la multiplicación es: \n", n * nu)
elif calculo == "/":
    print("El resultado de la división es: \n", n / nu)
else:
    print(" ------------------------------------------------------- ")
    print ("El valor ingresado no es un simbolo de operación matematica")

print (" ---------------------------------------------------------- ")
print ("  ****** Gracias por usar Calculadora Basica 2020 ******")
