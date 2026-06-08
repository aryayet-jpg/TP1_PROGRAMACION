
from validaciones import validar_float, validar_int, validar_texto, validar_opcion, validar_servidor

def pedir_cpu():
    # Usamos tu función: mensaje, min, max
    return validar_float("Ingrese el uso del CPU (%): ", 0, 100)

def pedir_ram():
    return validar_float("Ingrese el uso de memoria RAM (%): ", 0, 100)

def pedir_disco():
    return validar_float("Ingrese el espacio libre en disco (GB): ", 0, 1000)

def pedir_usuarios():
    return validar_int("Ingrese la cantidad de usuarios conectados: ", 0, 500)

def pedir_procesos():
    return validar_int("Ingrese la cantidad de procesos activos: ", 0, 1000)

def pedir_sistema_operativo():
    return validar_opcion("Ingrese su sistema operativo (Linux/Windows): ")

def pedir_firewall():
    return validar_texto("Ingrese su estado del firewall (Activo / Inactivo): ")

def pedir_nombre_servidor():
    return validar_texto("Ingrese el nombre del servidor: ")

def pedir_admin():
    return validar_texto("Ingrese el nombre del administrador responsable: ")

def pedir_tipo_servidor():
    return validar_servidor("Ingrese su tipo de servidor: ")

#funciones duplicadas, llamamos a las nuevas:
def ingresar_sistema_operativo():
    return pedir_sistema_operativo()

def ingresar_firewall():
    return pedir_firewall()

def ingresar_tipo_servidor():
    return pedir_tipo_servidor()