from inputs import ingresar_sistema_operativo, ingresar_firewall, ingresar_tipo_servidor
from calculos import calcular_carga_promedio
from reglas import evaluar_sistema
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
# Pasamos las variables sueltas.
evaluar_sistema(nombre_del_servidor, so, cpu, ram, disco, procesos, firewall, servidor, usuarios)