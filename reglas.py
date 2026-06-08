# 1. Verificar CPU y RAM

def regla_cpu_ram_error (cpu: float, ram: float) -> bool:
    """
    Verifica si el uso de CPU y RAM superan el 80%. Si ambos superan el 80%, se considera un error.
    Args:
        cpu (float): Porcentaje de uso de CPU.
        ram (float): Porcentaje de uso de RAM.                  
    Returns:
        bool: True si ambos CPU y RAM superan el 80%, False en caso contrario.
        
    """
    return cpu > 80 and ram > 80

    

# 2. Verificar Disco y Procesos

def regla_disco_procesos_error(disco: float, procesos: int) -> bool:
    """
    Verifica si el uso de disco o la cantidad de procesos superan el 80%. Si ambos superan el 80%, se considera un error.
    Args:
        disco (float): Porcentaje de uso de disco.
        procesos (int): Cantidad de procesos activos.                  
    Returns:
        bool: True si ambos disco y procesos superan el 80%, false en caso contrario.

    """

    return disco < 30 or procesos > 80
    


# 3. Verificar Firewall

def regla_firewall_error(firewall: str) -> bool:
    """
    Verifica si el firewall está inactivo. Si el firewall está inactivo, se considera un error.
    Args:
        firewall (str): Estado del firewall ("Activo" o "Inactivo").
    Returns:
        bool: True si el firewall está inactivo, false si está activo.

    """
    if not firewall == "Activo":
        return True
    else:
        return False
        


# 4: Verificar alerta de estado óptimo o normal

def regla_estado_optimo(cpu: float, ram: float) -> bool:
    """
    Verifica si el uso de CPU y RAM están en un rango óptimo.
    Args:
        cpu (float): Porcentaje de uso de CPU.
        ram (float): Porcentaje de uso de RAM.
    Returns:
        bool: True si ambos CPU y RAM están entre 40% y 70%, false en caso contrario.

    """
    return (cpu >= 40 and cpu <= 70) and (ram >= 40 and ram <= 70)



# 5. Verificar alerta servidor web

def regla_servidor_web(servidor: int, usuarios: int, cpu: float) -> bool:
    """
    Verifica si el servidor es del tipo web y si la cantidad de usuarios conectados supera los 100 y el uso de CPU supera el 85%. Si se cumplen estas condiciones, se indica una alerta para servidores web.
    Args:
        servidor (int): Tipo de servidor (1 para web, 2 para base de datos, 3 para archivos).
        usuarios (int): Cantidad de usuarios conectados.
        cpu (float): Porcentaje de uso de CPU.
    Returns:
        bool: True si el servidor es web y se cumplen las condiciones de usuarios y CPU, false en caso contrario.

    """
    return servidor == 1 and usuarios > 100 and cpu > 85
    


# 6. Verificar alerta base de datos
    
def regla_base_datos_disco_ram(servidor: int, disco: float, ram: float) -> bool:
    """
    Verifica si el servidor es del tipo base de datos y si el espacio libre en disco es menor a 20 GB y el uso de RAM supera el 70%. Si se cumplen estas condiciones, se indica una alerta para servidores de base de datos.
    Args:
        servidor (int): Tipo de servidor (1 para web, 2 para base de datos, 3 para archivos).
        disco (float): Espacio libre en disco en GB.
        ram (float): Porcentaje de uso de RAM.
    Returns:
        bool: True si el servidor es de base de datos y se cumplen las condiciones de disco y RAM, false en caso contrario.

    """
    return servidor == 2 and disco < 20 and ram > 70