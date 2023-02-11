# Manejo de información
#Escribir una función que reciba n parámetros de llave valor 
# e imprima la información en formato “{llave}”: “{Valor}”

def PrintProps(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}: {value}')

PrintProps(a=10,b=5,Jordan='Diaz',Alejandro='main bardo')