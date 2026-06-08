from inputs import (
    pedir_cpu, pedir_ram, pedir_disco, pedir_usuarios, 
    pedir_procesos, pedir_sistema_operativo, pedir_firewall, 
    pedir_nombre_servidor, pedir_admin, pedir_tipo_servidor
)
from calculos import calcular_carga_promedio
from reglas import regla_disco_procesos_error, regla_cpu_ram_error, regla_firewall_error, regla_estado_optimo, regla_servidor_web, regla_base_datos_disco_ram
from calculos import calcular_porcentaje_riesgo
from outputs import mostrar_reporte


print("==== SISTEMA DE DIAGNÓSTICO DEL SERVIDOR ===")

# # 1. PEDIDA DE DATOS INDIVIDUALES
cpu = pedir_cpu()
ram = pedir_ram()
disco = pedir_disco()
usuarios = pedir_usuarios()
procesos = pedir_procesos()

so = pedir_sistema_operativo()
firewall = pedir_firewall()
servidor = pedir_tipo_servidor()

nombre_del_servidor = pedir_nombre_servidor()
admin = pedir_admin()

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
# 4. PORCENTAJE DE RIESGO
porcentaje_riesgo = calcular_porcentaje_riesgo(contador, 4)

# MUESTRA DEL REPORTE
mostrar_reporte(
    nombre_del_servidor, 
    porcentaje_riesgo, 
    so, 
    mensaje_cpu_ram, 
    mensaje_disco_procesos, 
    mensaje_firewall, 
    mensaje_servidor_web, 
    mensaje_base_datos_disco_ram,
    contador
)