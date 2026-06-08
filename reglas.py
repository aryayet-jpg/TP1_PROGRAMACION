# 1. Validación CPU y RAM

def regla_cpu_ram_error (cpu: float, ram: float) -> bool:
    if cpu > 80 and ram > 80:
        return True
    else:
        return False 
    

# 2. Validación Disco y Procesos

def regla_disco_procesos_error(disco: float, procesos: int) -> bool:

    if disco < 30 or procesos > 80:
        return True
    else:
        return False


# 3. Validación Firewall

def regla_firewall_error(firewall: str) -> bool:
    if not firewall == "Activo":
        return True
    else:
        return False
        

# 4: Alerta de estado óptimo o normal

def regla_estado_optimo(cpu: float, ram: float) -> bool:
    if (cpu >= 40 and cpu <= 70) and (ram >= 40 and ram <= 70): 
        return True
    else:
         return False


# 5. Validación alerta servidor web
def regla_servidor_web(servidor: int, usuarios: int, cpu: float) -> bool:   
    if servidor == 1 and usuarios > 100 and cpu > 85:
        return True
    else:
        return False    
    

# 6. Validación alerta base de datos
    
def regla_base_datos_disco_ram(servidor: int, disco: float, ram: float) -> bool:
    if servidor == 2 and disco < 20 and ram > 70:
        return True
    else:
       return False
