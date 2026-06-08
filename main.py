from inputs import ingresar_sistema_operativo, ingresar_firewall, ingresar_tipo_servidor
from calculos import calcular_carga_promedio
from reglas import regla_disco_procesos_error, regla_cpu_ram_error, regla_firewall_error, regla_estado_optimo, regla_servidor_web, regla_base_datos_disco_ram
from validaciones import validar_float, validar_int, validar_texto, validar_opcion, validar_servidor



print("==== SISTEMA DE DIAGNÓSTICO DEL SERVIDOR ===")

# 1. PEDIDA DE DATOS INDIVIDUALES 
cpu = float(input("Ingrese el uso del CPU (%): "))
ram = float(input("Ingrese el uso de memoria RAM (%): "))
disco = float(input("Ingrese el espacio libre en disco (GB): "))
usuarios = int(input("Ingrese la cantidad de usuarios conectados: "))
procesos = int(input("Ingrese la cantidad de procesos activos: "))


so = ingresar_sistema_operativo()
firewall = ingresar_firewall()
servidor = ingresar_tipo_servidor()

nombre_del_servidor = input("Ingrese el nombre del servidor: ")
admin = input("Ingrese el nombre del administrador responsable: ")


# 2. CÁLCULO DE LA CARGA PROMEDIO
carga_promedio = calcular_carga_promedio(cpu, ram)
print(f"\nEl promedio de uso de recursos (CPU/RAM) es: {carga_promedio}%:  ")

input(f"Hola {admin}. Presione ENTER para ver su diagnostico: \n")

# 3. EVALUACIÓN 
# VARIABLES DE DIAGNÓSTICO

mensaje_cpu_ram = ""
mensaje_disco_procesos = ""
mensaje_firewall = ""
mensaje_servidor_web = ""
mensaje_base_datos_disco_ram = ""


contador = 0

# Validación CPU y RAM

if regla_cpu_ram_error(cpu, ram):

    mensaje_cpu_ram = "🚨 Sobrecarga critica (CPU y RAM muy altas!) "
    contador += 1
    
else:
    print("El estado de su CPU/RAM funcionan perfecto!. ")


# Validación Disco y Procesos

if regla_disco_procesos_error(disco, procesos):

    mensaje_disco_procesos = "🚨 Sobrecarga crítica (Disco o Procesos altos)"
    contador += 1

else:
    print("El estado de su Disco o proceso funciona perfecto.")


# Validación Firewall

if regla_firewall_error(firewall):

    mensaje_firewall = "🚨 Riesgo de seguridad: firewall desactivado. "
    contador += 1 


# Validacion alerta de estado óptimo o normal

if regla_estado_optimo(cpu, ram):
    print("El estado de su servidor es normal. ")


# Validacion alerta de servidor web

if regla_servidor_web(servidor, usuarios, cpu):
    mensaje_servidor_web = ("🚨 Su servidor web tiene alta demanda, se recomienda escalar recursos.")  
    contador += 1


# Validacion alerta de base de datos

if regla_base_datos_disco_ram(servidor, disco, ram):
    mensaje_base_datos_disco_ram = ("🚨 Su base de datos esta en riesgo (Poco disco y mucha RAM).")
    contador += 1

    
