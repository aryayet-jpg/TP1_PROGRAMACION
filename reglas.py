from calculos import calcular_porcentaje_riesgo
from outputs import mostrar_reporte

def evaluar_sistema(nombre_del_servidor, so, cpu, ram, disco, procesos, firewall, servidor, usuarios):
    # Errores en caso de no coincidir
    cpu_ram_error = ""
    disco_procesos_error = ""
    antivirus = ""
    web_usuarios_cpu_error = ""
    bdd_disco_ram_error = ""
    
    contador = 0

    # 1. Validación CPU y RAM
    if cpu > 80 and ram > 80:
        cpu_ram_error = "🚨 Sobrecarga critica (CPU y RAM muy altas!) "
        contador += 1
    else:
        print("El estado de su CPU/RAM funcionan perfecto!. ")

    # 2. Validación Disco y Procesos
    if disco < 30 or procesos > 80:
        disco_procesos_error = "🚨 Sobrecarga critica (Disco o Procesos altos!) "
        contador += 1
    else:
        print("El estado de su Disco o proceso funcionan perfecto!. ")

    # 3. Validación Firewall
    if not firewall == "Activo":  
        antivirus = "🚨 Riesgo de seguridad: firewall desactivado. "
        contador += 1 

    # 4: Alerta de estado óptimo o normal
    if (cpu >= 40 and cpu <= 70) and (ram >= 40 and ram <= 70): 
        print("El estado de su servidor es normal. ")

    # 5. Validación según tipo de servidor
    match servidor:       
        case 1:
            if servidor == 1 and usuarios > 100 and cpu > 85: 
                web_usuarios_cpu_error = "🚨 Su servidor web tiene alta demanda, se recomienda escalar recursos."
                contador += 1
        case 2:
            if servidor == 2 and disco < 20 and ram > 70:
                bdd_disco_ram_error = "🚨 Su base de datos esta en riesgo (Poco disco y mucha RAM)."
                contador += 1
        case 3:
            print("")           
        case _:
            print("NO es uno de los servidores opcionales")

    # 6: Calculamos el riesgo real
    total_reglas = 4  
    estado_general = calcular_porcentaje_riesgo(contador, total_reglas)

    # LLAMADA AL OUTPUT:
    mostrar_reporte(
        nombre_del_servidor, 
        estado_general, 
        so, 
        cpu_ram_error, 
        disco_procesos_error, 
        antivirus, 
        web_usuarios_cpu_error, 
        bdd_disco_ram_error, 
        contador
    )