#7 Formateo y conversiones
# Escribir un programa que muestre un menú con 2 opciones 
# la primera opción “1.- Imprimir YYYY/MM/DD” 
# la segunda “2.- Imprimir MM/DD/YYYY” 
# una vez seleccionada la opción imprimir la fecha del día de hoy en el formato seleccionado.

from datetime import datetime
option = int(input('Opciones para imprimir fecha: \n 1.- Imprimir YYYY/MM/DD \n 2.- Imprimir MM/DD/YYYY \n'))
fecha = datetime.now()
if option ==1:
    
    print('fecha en formato YYYY/MM/DD: ',fecha.strftime('%Y/%m/%d'))
elif option==2:
    print('fecha en formato MM/DD/YYYY: ',fecha.strftime('%m/%d/%Y'))