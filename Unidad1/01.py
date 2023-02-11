##1 Funciones con n parámetros
# Escribir un programa que contenga una función que reciba n parámetros de tipo numérico y calcule el producto total.


def SumNParams(*nums):
    return sum(nums)

print(SumNParams(10,20,30,40,10,5))
