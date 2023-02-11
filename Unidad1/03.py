#Entrada de datos y manipulación.

#Escribir un programa que permita al usuario capturar su nombre completo e imprima su nombre de manera inversa letra por letra


def ReverseName(name):
    return name[::-1]

fullname= input("Ingrese nombre completo:")

print(ReverseName(fullname))


