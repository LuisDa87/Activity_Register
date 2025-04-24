continuar = True
continuar2 = True
info = []

while continuar:

    print("\n--------Gestion de Usuarios----------")
    print("")
    print("1. Ver Usuarios")
    print("2. Actualizar información")
    print("3. Eliminar Usuarios")
    print("4. Agregar Usuarios")
    print("5. Salir")

    opc = int(input("Ingrese una opcion: "))

    if opc == 1:
        print("\n--Estos son todos los usuarios--")
        if len(info) == 0:
            print("--No hay usuarios registrados--")
        else:
            for i in range(len(info)):
                print(f"{i+1}. {info[i][0]}, {info[i][1]} años, {info[i][2]}")
        conti = input("\nIngrese s para continuar o n para finalizar: ")
        if conti == "n" or conti=="N":
            continuar = False

    elif opc == 2:
        print("Actualizar información")
        if len(info) == 0:
            print("\n No hay usuarios registrados para actualizar\n")
        else:
            for i in range(len(info)):
                print(f"{i+1}. {info[i][0]}, {info[i][1]} años, {info[i][2]}")
            
            indice = int(input("Ingrese el número del usuario a actualizar: ")) - 1
            
            if 0 <= indice < len(info):
                print(f"Actualizando usuario: {info[indice][0]}")
                info[indice][0] = input("Nuevo nombre (Enter para mantener): ") 
                info[indice][1] = input("Nueva edad (Enter para mantener): ")
                info[indice][2] = input("Nuevo correo (Enter para mantener): ") 
                print("Usuario actualizado correctamente")
            else:
                print("Número de usuario inválido")
        
        conti = input("Ingrese s para continuar o n para finalizar: ")
        if conti == "n" or conti=="N":
            continuar = False
    
    elif opc == 3:
        print("Eliminar usuario")
        if len(info) == 0:
            print("No hay usuarios registrados para eliminar")
        else:
            for i in range(len(info)):
                print(f"{i+1}. {info[i][0]}, {info[i][1]} años, {info[i][2]}")
            
            indice = int(input("Ingrese el número del usuario a eliminar: ")) - 1
            
            if 0 <= indice < len(info):
                usuario_eliminado = info.pop(indice)
                print(f"Usuario {usuario_eliminado[0]} eliminado correctamente")
            else:
                print("Número de usuario inválido")
        
        conti = input("Ingrese s para continuar o n para finalizar: ")
        if conti == "n" or conti=="N":
            continuar = False
    
    elif opc == 4:
        continuar2==True
        while continuar2:
            print("Agregar usuarios")
            nombre = input("Nombre: ")

            # Verificación de edad
            edad_valida = False
            while not edad_valida:
                edad_input = input("Edad: ")
                try:
                    edad = int(edad_input)
                    edad_valida = True
                except ValueError:
                    print("Error: La edad debe ser un número entero")

                correo = input("Correo electrónico: ")
    
                # Verificar si el correo ya existe en la lista de usuarios
                correo_existe = False
            for usuario in info:
                if usuario[2] == correo:
                    correo_existe = True
                    break
    
            if correo_existe:
                print("Error: Este correo ya está registrado en el sistema")
            else:

                info.append([nombre, edad, correo])
                print("Usuario registrado correctamente")

            conti2 = input("Ingrese s para continuar registrando o n para finalizar: ")
            if conti2 == "n":
                     continuar2 = False
    
        conti = input("Ingrese s para continuar o n para finalizar: ")
        if conti == "n":
            continuar = False
        
    elif opc == 5:
        print("Saliendo del sistema")
        continuar = False
    else:
        print("Ingresó un número incorrecto")
        conti = input("Ingrese s para continuar o n para finalizar: ")
        if conti == "n" or conti=="N":
            continuar = False