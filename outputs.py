def mostrar_reporte(nombre_del_servidor, estado_general, so, cpu_ram_error, disco_procesos_error, antivirus, web_usuarios_cpu_error, bdd_disco_ram_error, contador):
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
    else:
        print("Recomendaciones:")

        if cpu_ram_error: 
            print("- Reducir carga del sistema o mejorar hardware (CPU/RAM).")

        if disco_procesos_error:
            print("- Liberar espacio en disco o revisar procesos innecesarios.")

        if antivirus:
            print("- Activar el firewall para mejorar la seguridad.")

        if web_usuarios_cpu_error:
            print("- Escalar recursos del servidor web o balancear carga.")

        if bdd_disco_ram_error:
            print("- Ampliar almacenamiento o optimizar uso de memoria en la base de datos.")

        print(f"==============================================")