#prueba validaciones.py

def validar_float(mensaje: str, minimo: float, maximo: float) -> float:
    """Valida entradas numéricas (CPU, RAM, Disco)"""
    valor = float(input(mensaje))
    while valor < minimo or valor > maximo:
        print(f"Error: El valor debe estar entre {minimo} y {maximo}.")
        valor = float(input(mensaje))
    return valor

def validar_int(mensaje: str, minimo: int, maximo: int) -> int:
    """Valida enteros (Usuarios, Procesos)"""
    valor = int(input(mensaje))
    while valor < minimo or valor > maximo:
        print(f"Error: El valor debe estar entre {minimo} y {maximo}.")
        valor = int(input(mensaje))
    return valor

def validar_texto(mensaje: str) -> str:
    """Valida que el campo no esté vacío y tenga una longitud mínima"""
    texto = input(mensaje)
    while len(texto) < 3:
        print("Error: El campo debe tener al menos 3 caracteres.")
        texto = input(mensaje)
    return texto

def validar_opcion(mensaje: str) -> str:
    """Valida que la opción sea obligatoriamente Linux o Windows"""
    valor = input(mensaje)
    # Mientras el valor NO sea Linux Y TAMPOCO sea Windows, seguimos
    while valor != "Linux" and valor != "Windows":
        print("Error: Solo se permite 'Linux' o 'Windows'")
        valor = input(mensaje)
    return valor

def validar_servidor(mensaje: str) -> int:
    """Valida el tipo de servidor: solo permite 1, 2 o 3"""
    print("\n[1] Web  [2] Base de datos  [3] Archivos")
    
    # Pedimos el dato por primera vez
    servidor = int(input(mensaje))
    
    # Mientras el número sea menor a 1 O mayor a 3, significa que está mal
    while servidor < 1 or servidor > 3:
        print("Error: El número debe ser 1, 2 o 3.")
        servidor = int(input("Ingrese su tipo de servidor: "))
        
    return servidor