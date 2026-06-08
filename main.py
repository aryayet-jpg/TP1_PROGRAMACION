#main

from inputs import pedir_cpu, pedir_ram, pedir_disco, pedir_usuarios, pedir_procesos, pedir_sistema_operativo, pedir_firewall, pedir_nombre_servidor, pedir_admin, pedir_tipo_servidor

from calculos import calcular_carga_promedio

from reglas import regla_cpu_ram_error, regla_disco_procesos_error, regla_firewall_error, regla_servidor_web, regla_base_datos_disco_ram

from outputs import mostrar_introduccion, obtener_datos


print("==== SISTEMA DE DIAGNÓSTICO DEL SERVIDOR ====")

cpu = pedir_cpu()
ram = pedir_ram()
disco = pedir_disco()
usuarios = pedir_usuarios()
procesos = pedir_procesos()
so = pedir_sistema_operativo()
firewall = pedir_firewall()
servidor = pedir_tipo_servidor()
nombre_servidor = pedir_nombre_servidor()
admin = pedir_admin()

carga_promedio = calcular_carga_promedio(cpu, ram)

mostrar_introduccion(admin)

mensaje_cpu_ram = "🚨 Sobrecarga critica (CPU y RAM muy altas)" if regla_cpu_ram_error(cpu, ram) else ""
mensaje_disco_procesos = "🚨 Sobrecarga critica (Disco bajo o procesos altos)" if regla_disco_procesos_error(disco, procesos) else ""
mensaje_firewall = "🚨 Riesgo de seguridad: firewall desactivado" if regla_firewall_error(firewall) else ""
mensaje_servidor_web = "🚨 Servidor web con alta demanda, escalar recursos" if regla_servidor_web(servidor, usuarios, cpu) else ""
mensaje_base_datos = "🚨 Base de datos en riesgo (poco disco y mucha RAM)" if regla_base_datos_disco_ram(servidor, disco, ram) else ""

obtener_datos(
    nombre_servidor=nombre_servidor,
    so=so,
    carga_promedio=carga_promedio,
    mensaje_cpu_ram=mensaje_cpu_ram,
    mensaje_disco_procesos=mensaje_disco_procesos,
    mensaje_firewall=mensaje_firewall,
    mensaje_servidor_web=mensaje_servidor_web,
    mensaje_base_datos=mensaje_base_datos
)