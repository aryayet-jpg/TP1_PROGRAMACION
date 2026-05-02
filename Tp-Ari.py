print("==== SISTEMA DE DIAGNOSTICO DEL SERVIDOR ===" )

#(Frann): Separo un poco para que sea mejor lejible!
# Entradas numericas
cpu = float(input("Ingrese el uso del CPU (%): "))
ram = float(input("Ingrese el uso de memoria RAM (%): "))
disco = float(input("Ingrese el espacio libre es disco (GB): "))
usuarios = int(input("Ingrese la cantidad de usuarios conectados: "))
procesos = int(input("Ingrese la cantidad de procesos activos: "))

# Entradas de categoria
so = input("Ingrese su sistema operativo (Linux/Windows): ") 
firewall = input("Ingrese su estado del firewall (Activo / Inactivo): ")
servidor = input("Ingrese su tipo de servidor (Web / Base de datos / Archivos): ")
nombre_del_servidor = input("Ingrese el nombre del servidor: ")
admin = input("Ingrese el nombre del administrador responsable: ")

carga_promedio = (cpu + ram) / 2 # (Frann): Acá agregué parentesis!
recursos_disponibles = print( f"\nEl promedio de uso de recursos (CPU/RAM) es: {carga_promedio}%:  ")

# Errores en caso de no coincidir
cpu_ram_error = ""
disco_procesos_error = ""
antivirus = ""
web_usuarios_cpu_error = ""
bdd_disco_ram_error = ""


input(f"Hola {admin}. Presione ENTER para ver su diagnostico: \n")

contador = 0

if cpu > 80 and ram > 80:
    cpu_ram_error = "🚨 Sobrecarga critica (CPU y RAM muy altas!) "
    contador += 1
else:
    print("El estado de su CPU/RAM funcionan perfecto!. ")

if disco < 30 or procesos > 80:
    disco_procesos_error = "🚨 Sobrecarga critica (Disco o Procesos altos!) "
    contador += 1
else:
    print("El estado de su Disco o proceso funcionan perfecto!. ")

if not firewall == "Activo":  
    antivirus = "🚨 Riesgo de seguridad: firewall desactivado. "
    contador += 1 

if (cpu >= 40 and cpu <= 70) and (ram >= 40 and ram <= 70): # (Frann): Corregí una logica acá
        print("El estado de su servidor es normal. ")

if servidor == "Web" and usuarios > 100 and cpu > 25:
        web_usuarios_cpu_error = "🚨 Su servidor web tiene alta demanda, se recomienda escalar recursos."
        contador += 1

if servidor == "Base de datos" and disco < 20 and ram > 70:
        bdd_disco_ram_error= "🚨 Su base de datos esta en riesgo (Poco disco y mucha RAM)."
        contador += 1


estado_general = (contador / 4) * 100
print(f"\n===============================================")
print(f"\nDiagnostico del servidor: {nombre_del_servidor}")
print(f"\nEl porcentaje del riesgo es: {estado_general}%")
print(f"Su sistema operativo es: {so}")
print(f"\n===============================================\n")
print(f"Problemas detectados:")
if cpu_ram_error: print(cpu_ram_error)
if disco_procesos_error: print(disco_procesos_error)
if antivirus: print(antivirus)
if web_usuarios_cpu_error: print(web_usuarios_cpu_error)
if bdd_disco_ram_error: print(bdd_disco_ram_error)
if contador == 0:
      print("No se detectaron problemas! Su servicio es estable. ")
print(f"\n===============================================")
# Prueba solucion Frann!