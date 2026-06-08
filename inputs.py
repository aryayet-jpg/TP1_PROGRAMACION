from validaciones import validar_float, validar_int, validar_texto

def pedir_cpu():
    """Solicita y valida el porcentaje de uso de CPU (0-100).
    
    Returns:
        float: Porcentaje de uso de CPU válido entre 0 y 100.
    """
    return validar_float("Ingrese el uso del CPU (%): ", 0.0, 100.0)

def pedir_ram():
    """Solicita y valida el porcentaje de uso de memoria RAM (0-100).
    
    Returns:
        float: Porcentaje de uso de RAM válido entre 0 y 100.
    """
    return validar_float("Ingrese el uso de memoria RAM (%): ", 0.0, 100.0)

def pedir_disco():
    """Solicita y valida el espacio libre en disco en GB (0-10000).
    
    Returns:
        float: Espacio libre en disco válido entre 0 y 10000 GB.
    """
    return validar_float("Ingrese el espacio libre en disco (GB): ", 0.0, 10000.0)

def pedir_usuarios():
    """Solicita y valida la cantidad de usuarios conectados (0-5000).
    
    Returns:
        int: Cantidad de usuarios válida entre 0 y 5000.
    """
    return validar_int("Ingrese la cantidad de usuarios conectados: ", 0, 5000)

def pedir_procesos():
    """Solicita y valida la cantidad de procesos activos (0-10000).
    
    Returns:
        int: Cantidad de procesos válida entre 0 y 10000.
    """
    return validar_int("Ingrese la cantidad de procesos activos: ", 0, 10000)

def pedir_sistema_operativo():
    """Solicita y valida que el sistema operativo sea Linux o Windows.
    
    Returns:
        str: Sistema operativo válido ('Linux' o 'Windows').
    """
    so = input("Ingrese su sistema operativo (Linux/Windows): ") 
    while so != "Linux" and so != "Windows":
        so = input("* CAMPO OBLIGATORIO Ingrese su sistema operativo (Linux/Windows): ") 
    return so

def pedir_firewall():
    """Solicita y valida que el estado del firewall sea Activo o Inactivo.
    
    Returns:
        str: Estado del firewall válido ('Activo' o 'Inactivo').
    """
    firewall = input("Ingrese su estado del firewall (Activo / Inactivo): ")
    while firewall != "Activo" and firewall != "Inactivo":
        firewall = input("* CAMPO OBLIGATORIO Ingrese su estado del firewall (Activo / Inactivo): ")
    return firewall

def pedir_tipo_servidor():
    """Solicita y valida que el tipo de servidor sea 1 (Web), 2 (Base de datos) o 3 (Archivos).
    
    Returns:
        int: Tipo de servidor válido (1, 2 o 3).
    """
    print()
    print("[1] Web") 
    print("[2] Base de datos")
    print("[3] Archivos")
    servidor = int(input("Ingrese su tipo de servidor: "))
    while servidor != 1 and servidor != 2 and servidor != 3:
        servidor = int(input("* CAMPO OBLIGATORIO Ingrese su tipo de servidor: "))
    return servidor

def pedir_nombre_servidor():
    """Solicita y valida el nombre del servidor (mínimo 3 caracteres).
    
    Returns:
        str: Nombre del servidor válido con al menos 3 caracteres.
    """
    return validar_texto("Ingrese el nombre del servidor: ")

def pedir_admin():
    """Solicita y valida el nombre del administrador responsable (mínimo 3 caracteres).
    
    Returns:
        str: Nombre del administrador válido con al menos 3 caracteres.
    """
    return validar_texto("Ingrese el nombre del administrador responsable: ")