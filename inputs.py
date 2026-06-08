from validaciones import validar_float, validar_int, validar_texto

def pedir_cpu():
    """
    Pide el uso del CPU y lo valida
    """
    
    return validar_float("Ingrese el uso del CPU (%): ", 0.0, 100.0)

def pedir_ram():
    """
    Pide el uso de la RAM y lo valida
    """
    return validar_float("Ingrese el uso de memoria RAM (%): ", 0.0, 100.0)

def pedir_disco():
    """
    Pide el espacio libre en disco y lo valida
    """
    return validar_float("Ingrese el espacio libre en disco (GB): ", 0.0, 10000.0)

def pedir_usuarios():
    """
    Pide la cantidad de usuarios conectados y lo valida
    """
    return validar_int("Ingrese la cantidad de usuarios conectados: ", 0, 5000)

def pedir_procesos():
    """
    Pide la cantidad de procesos activos y lo valida
    """
    return validar_int("Ingrese la cantidad de procesos activos: ", 0, 10000)

def pedir_sistema_operativo():
    """
    Pide el sistema operativo y lo valida
    """
    so = input("Ingrese su sistema operativo (Linux/Windows): ") 
    while so != "Linux" and so != "Windows":
        so = input("* CAMPO OBLIGATORIO Ingrese su sistema operativo (Linux/Windows): ") 
    return so

def pedir_firewall():
    """
    Pide el estado del firewall y lo valida
    """
    firewall = input("Ingrese su estado del firewall (Activo / Inactivo): ")
    while firewall != "Activo" and firewall != "Inactivo":
        firewall = input("* CAMPO OBLIGATORIO Ingrese su estado del firewall (Activo / Inactivo): ")
    return firewall

def pedir_tipo_servidor():
    print()
    print("[1] Web") 
    print("[2] Base de datos")
    print("[3] Archivos")
    servidor = int(input("Ingrese su tipo de servidor: "))
    while servidor != 1 and servidor != 2 and servidor != 3:
        servidor = int(input("* CAMPO OBLIGATORIO Ingrese su tipo de servidor: "))
    return servidor

def pedir_nombre_servidor():
    return validar_texto("Ingrese el nombre del servidor: ")

def pedir_admin():
    return validar_texto("Ingrese el nombre del administrador responsable: ")