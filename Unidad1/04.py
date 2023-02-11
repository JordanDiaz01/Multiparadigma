#4 Entrada de datos y estructuración.

# Revisar su retícula para escribir un programa que cree un diccionario vacío para que el usuario capture las materias
#  y créditos de su semestre preferido (inferior a 8vo)
#  al final imprimir en el formato “{asignatura}” tiene “{créditos}” créditos. 
# Y la suma de todos los créditos del semestre

semestre={}
print("Escriba omitir para dejar de agregar materias")
while True:
    materia = input('Ingrese nombre de la materia: ')
    if(materia=="omitir"):
        break
    creditos= input('Ingrese creditos: ')
    semestre[materia]=int(creditos)

totalCreditos=0
for materia,creditos in semestre.items():
    totalCreditos+=creditos
    print(f'{materia} tiene {creditos}')

print(f'Total de creditos del semestre: {totalCreditos}')
