#prueba validaciones.py
def validar_float(mensaje: str, minimo: float, maximo: float) -> float:
    """Valida que el input sea un número flotante dentro de un rango específico.
    
    Args:
        mensaje (str): Mensaje mostrado al usuario para solicitar el dato.
        minimo (float): Valor mínimo aceptado.
        maximo (float): Valor máximo aceptado.
    
    Returns:
        float: Valor numérico válido dentro del rango.
    """
    valor = float(input(mensaje))
    while valor < minimo or valor > maximo:
        print(f"Error: El valor debe estar entre {minimo} y {maximo}.")
        valor = float(input(mensaje))
    return valor

def validar_int(mensaje: str, minimo: int, maximo: int) -> int:
    """Valida que el input sea un número entero dentro de un rango específico.
    
    Args:
        mensaje (str): Mensaje mostrado al usuario para solicitar el dato.
        minimo (int): Valor mínimo aceptado.
        maximo (int): Valor máximo aceptado.
    
    Returns:
        int: Valor entero válido dentro del rango.
    """
    valor = int(input(mensaje))
    while valor < minimo or valor > maximo:
        print(f"Error: El valor debe estar entre {minimo} y {maximo}.")
        valor = int(input(mensaje))
    return valor

def validar_texto(mensaje: str) -> str:
    """Valida que el input sea texto no vacío con longitud mínima de 3 caracteres.
    
    Args:
        mensaje (str): Mensaje mostrado al usuario para solicitar el dato.
    
    Returns:
        str: Texto válido con al menos 3 caracteres.
    """
    texto = input(mensaje)
    while len(texto) < 3:
        print("Error: El campo debe tener al menos 3 caracteres.")
        texto = input(mensaje)
    return texto

def validar_opcion(mensaje: str) -> str:
    """Valida que la opción ingresada sea 'Linux' o 'Windows'.
    
    Args:
        mensaje (str): Mensaje mostrado al usuario para solicitar el dato.
    
    Returns:
        str: Opción válida ('Linux' o 'Windows').
    """
    valor = input(mensaje)
    while valor != "Linux" and valor != "Windows":
        print("Error: Solo se permite 'Linux' o 'Windows'")
        valor = input(mensaje)
    return valor

def validar_servidor(mensaje: str) -> int:
    """Valida que el tipo de servidor sea 1, 2 o 3.
    
    Args:
        mensaje (str): Mensaje mostrado al usuario para solicitar el dato.
    
    Returns:
        int: Número válido (1, 2 o 3).
    """
    print("\n[1] Web  [2] Base de datos  [3] Archivos")
    
    servidor = int(input(mensaje))
    
    while servidor < 1 or servidor > 3:
        print("Error: El número debe ser 1, 2 o 3.")
        servidor = int(input("Ingrese su tipo de servidor: "))
        
    return servidor
