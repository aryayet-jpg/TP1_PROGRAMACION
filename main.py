import json
import os

from inputs import (pedir_cpu, pedir_ram, pedir_disco, pedir_usuarios, pedir_procesos, 
                    pedir_sistema_operativo, pedir_firewall, pedir_nombre_servidor, 
                    pedir_admin, pedir_tipo_servidor)
from calculos import calcular_carga_promedio
from reglas import (regla_cpu_ram_error, regla_disco_procesos_error, regla_firewall_error, 
                    regla_servidor_web, regla_base_datos_disco_ram)
from outputs import mostrar_info_general, mostrar_problemas, mostrar_recomendaciones, mostrar_fin

ARCHIVO_DATOS = "servidor_config.json"

def cargar_datos():
    """Carga los datos verificando la existencia del archivo."""
    if os.path.exists(ARCHIVO_DATOS):
        archivo = open(ARCHIVO_DATOS, "r", encoding="utf-8")
        datos = json.load(archivo)
        archivo.close()
        print("\n[+] Configuración cargada correctamente.")
        return datos
    else:
        print("\n[-] No se encontró archivo previo. Iniciando con valores vacíos.")
        
        return {
            "config": {"nombre": "", "admin": "", "so": "", "tipo": 0, "firewall": ""},
            "recursos": {"cpu": 0.0, "ram": 0.0, "disco": 0.0, "usuarios": 0, "procesos": 0},
            "diagnostico": {
                "promedio": 0.0, 
                "alertas": {"cpu_ram": "", "disco": "", "firewall": "", "web": "", "db": ""}
            }
        }

def guardar_datos(datos):
    """Guarda los datos usando open y close tradicional."""
    archivo = open(ARCHIVO_DATOS, "w", encoding="utf-8")
    json.dump(datos, archivo, indent=4)
    archivo.close()
    print("\n[+] ¡Configuración guardada exitosamente!")

def modificar(datos):
    """Actualiza el diccionario con las funciones del Sprint 2."""
    datos["config"] = {
        "nombre": pedir_nombre_servidor(), "admin": pedir_admin(), 
        "so": pedir_sistema_operativo(), "tipo": pedir_tipo_servidor(), 
        "firewall": pedir_firewall()
    }
    datos["recursos"] = {
        "cpu": pedir_cpu(), "ram": pedir_ram(), "disco": pedir_disco(), 
        "usuarios": pedir_usuarios(), "procesos": pedir_procesos()
    }
    print("\n[+] Datos actualizados en memoria.")

def ejecutar_diagnostico(datos):
    """Lógica de reglas del Sprint 2 adaptada al diccionario."""
    c, r, d, u, p, f, t = (datos["recursos"]["cpu"], datos["recursos"]["ram"], datos["recursos"]["disco"],
                           datos["recursos"]["usuarios"], datos["recursos"]["procesos"], 
                           datos["config"]["firewall"], datos["config"]["tipo"])
    
    datos["diagnostico"]["promedio"] = calcular_carga_promedio(c, r)
    

    datos["diagnostico"]["alertas"] = {
        "cpu_ram": "🚨 Sobrecarga critica (CPU y RAM muy altas)" if regla_cpu_ram_error(c, r) else "",
        "disco": "🚨 Sobrecarga critica (Disco bajo o procesos altos)" if regla_disco_procesos_error(d, p) else "",
        "firewall": "🚨 Riesgo de seguridad: firewall desactivado" if regla_firewall_error(f) else "",
        "web": "🚨 Servidor web con alta demanda, escalar recursos" if regla_servidor_web(t, u, c) else "",
        "db": "🚨 Base de datos en riesgo (poco disco y mucha RAM)" if regla_base_datos_disco_ram(t, d, r) else ""
    }
    print("[+] Diagnóstico ejecutado correctamente.")

def mostrar(datos):
    """Usa funciones de output."""
    mostrar_info_general(datos["config"]["nombre"], datos["config"]["so"], datos["diagnostico"]["promedio"])
    a = datos["diagnostico"]["alertas"]
    mostrar_problemas(a["cpu_ram"], a["disco"], a["firewall"], a["web"], a["db"])
    mostrar_recomendaciones(bool(a["cpu_ram"]), bool(a["disco"]), bool(a["firewall"]), bool(a["web"]), bool(a["db"]))
    mostrar_fin()

def main():
    datos = cargar_datos()
    while True:
        print("\n--- MENÚ SPRINT 3 ---")
        print("1. Cargar configuración | 2. Mostrar configuración | 3. Modificar configuración")
        print("4. Ejecutar diagnóstico | 5. Guardar configuración | 6. Salir")
        op = input("Seleccione una opción: ")
        
        if op == "1": datos = cargar_datos()
        elif op == "2": mostrar(datos)
        elif op == "3": modificar(datos)
        elif op == "4": ejecutar_diagnostico(datos)
        elif op == "5": guardar_datos(datos)
        elif op == "6": break
        else: print("Opción no válida.")

if __name__ == "__main__":
    main()