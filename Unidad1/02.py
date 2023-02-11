#Manejo y manipulación de elementos de una lista
#Escribir un programa que almacene el abecedario en una lista, 
#elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

import string

def AlphabetList():
    return list(string.ascii_lowercase)

Abc = AlphabetList()

for letter in range(len(Abc)):
    if(letter+1) % 3 ==0:
        Abc[letter]=""

Abc = list(filter(len,Abc))
print(Abc)