from Usuario import *

UserList =[Usuario("admin","123","Jordan Diaz","DIAJ00","Nuevo Laredo","Administrador")]

def Registrar(userList):
        usuario = input('Ingrese usuario: ')
        contrasena = input('Ingrese contraseña: ')
        nombre = input('Ingrese nombre: ')
        curpp = input('Ingrese curp: ')
        ciudad = input('Ingrese ciudad: ')
        for user in userList:
            if user._curp==curpp:
                print('El usuario ya existe')
                return
        unUsuario = Usuario(usuario,contrasena,nombre,curpp,ciudad)
        userList.append(unUsuario)
        print('usuario registrado')



def IniciarSesion(userList):
     us = input('Ingrese usuario: ')
     passw = input('Ingrese contraseña: ')
     for user in userList:
             if user._usuario == us and user._contrasena==passw and user._rol=='cliente':
                  print(f'Inicio de sesión correcto\nDatos de la sesión:\n{user.__str__()}')
                  return
             elif user._usuario == us and user._contrasena==passw and user._rol=='Administrador':
                  MostrarUsuarios(userList)
                  return
     print('Datos incorrectos')

def MostrarUsuarios(userList):
     for user in userList:
          print(user)
while True:
    print('Seleccione una opción del menú:\n1.Registro\n2.Inicio de sesión\n3.Salida\n')
    opc = int(input())
    if opc==1:
       Registrar(UserList)
    elif opc==2:
         IniciarSesion(UserList)

    elif opc==3:
        break
    else:
         print('Seleccione una opción válida ')


