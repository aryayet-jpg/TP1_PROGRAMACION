def pedir_cpu():
    return float(input("Ingrese el uso del CPU (%): ")) # Todos estos inputs los dejé para hacer validaciones

def pedir_ram():
    return float(input("Ingrese el uso de memoria RAM (%): ")) # Todos estos inp uts los dejé para hacer validaciones

def pedir_disco():
    return float(input("Ingrese el espacio libre en disco (GB): ")) # Todos estos inputs los dejé para hacer validaciones

def pedir_usuarios():
    return int(input("Ingrese la cantidad de usuarios conectados: ")) # Todos estos iuts los dejé para hacer validaciones

def pedir_procesos():
    return int(input("Ingrese la cantidad de procesos activos: ")) # Todos estos inp uts los dejé para hacer validaciones

def pedir_sistema_operativo():
    so = input("Ingrese su sistema operativo (Linux/Windows): ") 
    while so != "Linux" and so != "Windows":
        so = input("* CAMPO OBLIGATORIO Ingrese su sistema operativo (Linux/Windows): ") 
    return so

def pedir_firewall():
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
    return input("Ingrese el nombre del servidor: ")

def pedir_admin():
    return input("Ingrese el nombre del administrador responsable: ")

def ingresar_sistema_operativo():
    so = input("Ingrese su sistema operativo (Linux/Windows): ") 
    while so != "Linux" and so != "Windows":
        so = input("* CAMPO OBLIGATORIO Ingrese su sistema operativo (Linux/Windows): ") 
    return so

def ingresar_firewall():
    firewall = input("Ingrese su estado del firewall (Activo / Inactivo): ")
    while firewall != "Activo" and firewall != "Inactivo":
        firewall = input("* CAMPO OBLIGATORIO Ingrese su estado del firewall (Activo / Inactivo): ")
    return firewall

def ingresar_tipo_servidor():
    print("\n[1] Web  [2] Base de datos  [3] Archivos")
    servidor = int(input("Ingrese su tipo de servidor: "))
    while servidor != 1 and servidor != 2 and servidor != 3:
        servidor = int(input("* CAMPO OBLIGATORIO Ingrese su tipo de servidor: "))
    return servidor