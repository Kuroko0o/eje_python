calculo = input("Ingresar el simbolo de la operación que desea realizar: (+,-,*,/) \n")

num = input("Ingresar el número entero a calcular: \n")
num_dos = input("Ingresar el siguiente número entero a calcular: \n")
try:
    n = int(num)
    nu = int(num_dos)
except:
    print("El Valor ingresado no es un número entero")
    quit()

if calculo == "+":
    print("El resultado de la suma es: \n", n + nu)
elif calculo == "-":
    print("El resultado de la resta es: \n", n - nu)
elif calculo == "*":
    print("El resultado de la multiplicación es: \n", n * nu)
elif calculo == "/":
    print("El resultado de la división es: \n", n / nu)
