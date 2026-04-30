
print("==== SISTEMA DE DIAGNOSTICO DEL SERVIDOR ===" )

cpu = float(input("Ingrese el uso del CPU (%): "))
ram = float(input("Ingrese el uso de memoria RAM (%): "))
disco = float(input("Ingrese el espacio libre es disco (GB): "))
usuarios = int(input("Ingrese la cantidad de usuarios conectados: "))
procesos = int(input("Ingrese la cantidad de procesos activos: "))
so = input("Ingrese su sistema operativo (Linux/Windows): ") 
firewall = input("Ingrese su estado del firewall (Activo / Inactivo): ")
servidor = input("Ingrese su tipo de servidor (Web / Base de datos / Archivos): ")
nombre_del_servidor = input("Ingrese el nombre del servidor: ")
admin = input("Ingrese el nombre del administrador responsable: ")

carga_promedio = cpu + ram / 2 
recursos_disponibles = print( f"Sus recursos disponibles son {carga_promedio}:  ")

diagnostico = input(f"Hola {admin}. Presione ENTER para ver su diagnostico: ")


if cpu > 80 and ram > 90:
    print("🚨 El estado de su servidor es critico (CPU y RAM muy altas) ")
else:
    print("El estado de su servidor es util. ")

if disco > 30 or procesos > 80:
    print("Su servidor necesita mantenimiento. ")
else:
    print("El estado de su servidor es util. ")

if not firewall == "Activo":  
    print("Riesgo de seguridad: firewall desactivado. ")  

if cpu <= 40 and cpu >= 80 and ram <= 40 and ram >= 90:
        print("El estado de su servidor es normal. ")

if servidor == "Web" and usuarios > 40:
        print("Su servidor web es de alta demanda. ")
#no se me ocurre como seguir aca

if servidor == "BaseDatos" and disco < 20 and ram > 70:
        print("Su base de datos esta en riesgo, ")
#aca tampoco jeje
