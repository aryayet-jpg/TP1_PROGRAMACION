# 1. Verificar CPU y RAM
def regla_cpu_ram_error(cpu: float, ram: float) -> bool:
    """Regla: Alerta si CPU y RAM superan ambos el 80%.
    
    Args:
        cpu (float): Porcentaje de uso de CPU.
        ram (float): Porcentaje de uso de RAM.
    
    Returns:
        bool: True si CPU > 80 y RAM > 80, False en caso contrario.
    """
    if cpu > 80 and ram > 80:
        return True
    else:
        return False 
    

def regla_disco_procesos_error(disco: float, procesos: int) -> bool:
    """Regla: Alerta si disco libre es menor a 30GB O procesos superan 80.
    
    Args:
        disco (float): Espacio libre en disco (GB).
        procesos (int): Cantidad de procesos activos.
    
    Returns:
        bool: True si disco < 30 o procesos > 80, False en caso contrario.
    """
    if disco < 30 or procesos > 80:
        return True
    else:
        return False


def regla_firewall_error(firewall: str) -> bool:
    """Regla: Alerta si el firewall NO está activo.
    
    Args:
        firewall (str): Estado del firewall ('Activo' o 'Inactivo').
    
    Returns:
        bool: True si firewall no es 'Activo', False en caso contrario.
    """
    if not firewall == "Activo":
        return True
    else:
        return False
        

def regla_estado_optimo(cpu: float, ram: float) -> bool:
    """Regla: Estado óptimo si CPU y RAM están entre 40% y 70%.
    
    Args:
        cpu (float): Porcentaje de uso de CPU.
        ram (float): Porcentaje de uso de RAM.
    
    Returns:
        bool: True si CPU y RAM están entre 40 y 70, False en caso contrario.
    """
    if (cpu >= 40 and cpu <= 70) and (ram >= 40 and ram <= 70): 
        return True
    else:
        return False


def regla_servidor_web(servidor: int, usuarios: int, cpu: float) -> bool:   
    """Regla: Alerta para servidor web si usuarios > 100 y CPU > 85.
    
    Args:
        servidor (int): Tipo de servidor (1=Web, 2=Base de datos, 3=Archivos).
        usuarios (int): Cantidad de usuarios conectados.
        cpu (float): Porcentaje de uso de CPU.
    
    Returns:
        bool: True si es servidor web, usuarios > 100 y CPU > 85.
    """
    if servidor == 1 and usuarios > 100 and cpu > 85:
        return True
    else:
        return False    
    

def regla_base_datos_disco_ram(servidor: int, disco: float, ram: float) -> bool:
    """Regla: Alerta para base de datos si disco < 20GB y RAM > 70%.
    
    Args:
        servidor (int): Tipo de servidor (1=Web, 2=Base de datos, 3=Archivos).
        disco(float): Espacio libre en disco (GB).
        ram (float): Porcentaje de uso de RAM.
    
    Returns:
        bool: True si es servidor BD, disco < 20 y RAM > 70.
    """
    if servidor == 2 and disco < 20 and ram > 70:
        return True
    else:
        return False