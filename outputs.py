"""Módulo para mostrar resultados del diagnóstico al usuario"""

def mostrar_introduccion(admin: str) -> None:
    """Muestra mensaje de bienvenida y solicita continuar.
    
    Args:
        admin (str): Nombre del administrador responsable.
    """
    print()
    print(f"Hola {admin}. Presione ENTER para ver su diagnóstico: ")
    input()


def mostrar_info_general(nombre_servidor: str, so: str, carga_promedio: float) -> None:
    """Muestra información general del servidor.
    
    Args:
        nombre_servidor (str): Nombre del servidor.
        so (str): Sistema operativo (Linux/Windows).
        carga_promedio (float): Promedio de uso de CPU y RAM.
    """
    print()
    print("=" * 55)
    print(f"📡 DIAGNÓSTICO DEL SERVIDOR: {nombre_servidor}")
    print(f"🖥️  Sistema operativo: {so}")
    print(f"📊 Carga promedio (CPU/RAM): {carga_promedio:.2f}%")
    print("=" * 55)


def mostrar_problemas(
    mensaje_cpu_ram: str,
    mensaje_disco_procesos: str,
    mensaje_firewall: str,
    mensaje_servidor_web: str,
    mensaje_base_datos: str
) -> int:
    """Muestra los problemas detectados y retorna la cantidad de alertas.
    
    Args:
        mensaje_cpu_ram (str): Mensaje de alerta por CPU/RAM.
        mensaje_disco_procesos (str): Mensaje de alerta por disco/procesos.
        mensaje_firewall (str): Mensaje de alerta por firewall.
        mensaje_servidor_web (str): Mensaje de alerta por servidor web.
        mensaje_base_datos (str): Mensaje de alerta por base de datos.
    
    Returns:
        int: Cantidad total de alertas activadas.
    """
    contador = 0
    print()
    print("⚠️  PROBLEMAS DETECTADOS:")
    print()

    if mensaje_cpu_ram:
        print(f"  • {mensaje_cpu_ram}")
        contador += 1
    if mensaje_disco_procesos:
        print(f"  • {mensaje_disco_procesos}")
        contador += 1
    if mensaje_firewall:
        print(f"  • {mensaje_firewall}")
        contador += 1
    if mensaje_servidor_web:
        print(f"  • {mensaje_servidor_web}")
        contador += 1
    if mensaje_base_datos:
        print(f"  • {mensaje_base_datos}")
        contador += 1

    if contador == 0:
        print("  ✅ No se detectaron problemas. El servidor está estable.")

    return contador


def mostrar_recomendaciones(
    hay_cpu_ram: bool,
    hay_disco_procesos: bool,
    hay_firewall: bool,
    hay_servidor_web: bool,
    hay_base_datos: bool
) -> None:
    """Muestra recomendaciones según los problemas detectados.
    
    Args:
        hay_cpu_ram (bool): True si hay alerta de CPU/RAM.
        hay_disco_procesos (bool): True si hay alerta de disco/procesos.
        hay_firewall (bool): True si hay alerta de firewall.
        hay_servidor_web (bool): True si hay alerta de servidor web.
        hay_base_datos (bool): True si hay alerta de base de datos.
    """
    print()
    print("🔧 RECOMENDACIONES:")
    print()

    if hay_cpu_ram:
        print("  • Reducir carga del sistema o mejorar hardware (CPU/RAM).")
    if hay_disco_procesos:
        print("  • Liberar espacio en disco o revisar procesos innecesarios.")
    if hay_firewall:
        print("  • Activar el firewall para mejorar la seguridad.")
    if hay_servidor_web:
        print("  • Escalar recursos del servidor web o balancear carga.")
    if hay_base_datos:
        print("  • Ampliar almacenamiento o optimizar uso de memoria en la base de datos.")

    if not any([hay_cpu_ram, hay_disco_procesos, hay_firewall, hay_servidor_web, hay_base_datos]):
        print("  ✅ Todo está en orden. Mantener las buenas prácticas.")


def mostrar_fin() -> None:
    """Muestra el cierre del diagnóstico."""
    print()
    print("=" * 55)
    print("🏁 Fin del diagnóstico")
    print("=" * 55)
    print()


def obtener_datos(
    nombre_servidor: str,
    so: str,
    carga_promedio: float,
    mensaje_cpu_ram: str,
    mensaje_disco_procesos: str,
    mensaje_firewall: str,
    mensaje_servidor_web: str,
    mensaje_base_datos: str
) -> None:
    """Función principal que muestra el diagnóstico completo del servidor.
    
    Esta función unifica toda la salida: información general, problemas detectados,
    recomendaciones y cierre del diagnóstico.
    
    Args:
        nombre_servidor (str): Nombre del servidor.
        so (str): Sistema operativo (Linux/Windows).
        carga_promedio (float): Promedio de uso de CPU y RAM.
        mensaje_cpu_ram (str): Mensaje de alerta por CPU/RAM.
        mensaje_disco_procesos (str): Mensaje de alerta por disco/procesos.
        mensaje_firewall (str): Mensaje de alerta por firewall.
        mensaje_servidor_web (str): Mensaje de alerta por servidor web.
        mensaje_base_datos (str): Mensaje de alerta por base de datos.
    """
    mostrar_info_general(nombre_servidor, so, carga_promedio)
    
    mostrar_problemas(
        mensaje_cpu_ram,
        mensaje_disco_procesos,
        mensaje_firewall,
        mensaje_servidor_web,
        mensaje_base_datos
    )
    
    mostrar_recomendaciones(
        hay_cpu_ram=bool(mensaje_cpu_ram),
        hay_disco_procesos=bool(mensaje_disco_procesos),
        hay_firewall=bool(mensaje_firewall),
        hay_servidor_web=bool(mensaje_servidor_web),
        hay_base_datos=bool(mensaje_base_datos)
    )
    
    mostrar_fin()