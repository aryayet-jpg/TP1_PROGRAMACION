# Daniel: función mostrar datos 
def mostrar_datos() -> str | int | float:
    """ 
    Muestra los datos de estrada.

    Args:
         (str | int | float): Valores numéricos y cadenas de caracteres ingresados por el usuario.
    
    return:
         (str | int | float): variables numéricas y cadenas de caracteres "que fueron" ingresados por el usuario.
    """
    #(Frann): Separo un poco para que sea mejor lejible!
    # Entradas numericas
    cpu = float(input("Ingrese el uso del CPU (%): "))
    ram = float(input("Ingrese el uso de memoria RAM (%): "))
    disco = float(input("Ingrese el espacio libre es disco (GB): "))
    usuarios = int(input("Ingrese la cantidad de usuarios conectados: "))
    procesos = int(input("Ingrese la cantidad de procesos activos: "))

    # Entradas de categoria
    # Daniel: Agregue un while para que valide sólo las opciones ofrecidas por el input 

    so = input("Ingrese su sistema operativo (Linux/Windows): ") 
    while so != "Linux" and so != "Windows":
        so = input("* CAMPO OBLIGATORIO Ingrese su sistema operativo (Linux/Windows): ") 

    # Daniel: Agregue un while para que valide sólo las opciones ofrecidas por el input 
    firewall = input("Ingrese su estado del firewall (Activo / Inactivo): ")
    while firewall != "Activo" and firewall != "Inactivo":
        firewall = input("* CAMPO OBLIGATORIO Ingrese su estado del firewall (Activo / Inactivo):" \
        " ")

    # Daniel: modifiqué el imput y antepuse tres print para usarlos con el match
    print()
    print("[1] Web") 
    print("[2] Base de datos")
    print("[3] Archivos")

    servidor = int(input("Ingrese su tipo de servidor: "))
    while servidor != 1 and servidor != 2 and servidor != 3:
        servidor = int(input("* CAMPO OBLIGATORIO Ingrese su tipo de servidor: "))

    nombre_del_servidor = input("Ingrese el nombre del servidor: ")
    admin = input("Ingrese el nombre del administrador responsable: ")

    return(cpu, ram, admin, disco, procesos, disco, firewall, servidor, usuarios, nombre_del_servidor, so) 

# mostrar_datos()