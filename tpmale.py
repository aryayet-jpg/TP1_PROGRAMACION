print("==== SISTEMA DE DIAGNOSTICO DEL SERVIDOR ===" )

#Daniel: Agregué e Importé la función mostrar_datos del módulo datos_de_entrada

from datos_de_entrada import mostrar_datos  

# Daniel: Recibe las variables definidas en la función
(cpu, ram, admin, discos, procesos, disco, firewall, servidor, usuarios, nombre_del_servidor, so) = mostrar_datos()

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

match servidor: # Daniel: agregué un match para el input servidor.       
    case 1:
        if servidor == 1 and usuarios > 100 and cpu > 85: # (Male): corrijo cpu, 25 es bajo-
                web_usuarios_cpu_error = "🚨 Su servidor web tiene alta demanda, se recomienda escalar recursos."
                contador += 1
    case 2:
        if servidor == 2 and disco < 20 and ram > 70:
                bdd_disco_ram_error= "🚨 Su base de datos esta en riesgo (Poco disco y mucha RAM)."
                contador += 1
    case 3:
          print("") #Daniel: no hay validaciones para esta opción            
    case _:
          print("NO es uno de los servidores opcionales")

#(Male): Acomodo la cuenta del contador para que sea mas clara
total_reglas = 4  # porque match hace exclusión
estado_general = (contador / total_reglas) * 100

print(f"\n===============================================")
print(f"\nDiagnostico del servidor: {nombre_del_servidor}")
print(f"\nEl porcentaje del riesgo es: {estado_general}%")
print(f"Su sistema operativo es: {so}")
print(f"\n===============================================\n")
print(f"Problemas detectados:")

if cpu_ram_error: 
    print(cpu_ram_error)

if disco_procesos_error: 
    print(disco_procesos_error)

if antivirus: 
    print(antivirus)

if web_usuarios_cpu_error: 
    print(web_usuarios_cpu_error)

if bdd_disco_ram_error: 
    print(bdd_disco_ram_error)

if contador == 0:
      print("No se detectaron problemas! Su servicio es estable. ")

#Rizzo:Recomendaciones para optimizar

print("Recomendaciones:")

if cpu_ram_error: #Daniel:posicioné los print para que no estén el la misma linea
    print("- Reducir carga del sistema o mejorar hardware (CPU/RAM).")

if disco_procesos_error:
    print("- Liberar espacio en disco o revisar procesos innecesarios.")

if antivirus:
    print("- Activar el firewall para mejorar la seguridad.")

if web_usuarios_cpu_error:
    print("- Escalar recursos del servidor web o balancear carga.")

if bdd_disco_ram_error:
    print("- Ampliar almacenamiento o optimizar uso de memoria en la base de datos.")

if contador == 0:
    print("- No se requieren acciones. El sistema funciona correctamente.")
print(f"===============================================") 