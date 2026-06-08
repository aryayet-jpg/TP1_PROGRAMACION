def calcular_carga_promedio(cpu: float, ram: float) -> float:
    """Calcula el promedio de uso de recursos (CPU/RAM)

    Args:
        cpu (float): Porcentaje de uso de CPU
        ram (float): Porcentaje de uso de RAM

    Returns:
        float: Promedio de uso de recursos (CPU/RAM)
    """
    return (cpu + ram) / 2

def calcular_porcentaje_riesgo(contador_alertas: int, total_reglas: int) -> float:
    """Calcula el porcentaje de riesgo de las alertas

    Args:
        contador_alertas (int): Cantidad de alertas activadas
        total_reglas (int): Cantidad de reglas evaluadas

    Returns:
        float: Porcentaje de riesgo de las alertas
    """
    return (contador_alertas / total_reglas) * 100