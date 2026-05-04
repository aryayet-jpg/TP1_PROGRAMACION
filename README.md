# Sistema de Diagnóstico de Servidor
## Datos del proyecto
### Integrantes
- Franco Dominguez
- Daniel Almada
- Lautaro Rizzo
- Ariadna Tronconi
- Malena Aguirre

### Lenguaje utilizado
- Python

## Descripcion del codigo

El sistema desarrollado es una aplicación que permite analizar el estado de un servidor a partir de datos solicitados al usuario.

### Objetivos

- Evaluar el rendimiento del servidor
- Detectar posibles riesgos o fallos
- Generar alertas automáticas
- Brindar recomendaciones de administración

### Consignas solicitadas para las reglas

- Reglas que utilicen 3 o más variables en la condición. 
- Reglas con combinación AND / OR. 
- 1 Regla con NOT. 
- 1 Regla que evalúe rangos numéricos. 


### Reglas implementadas

1. Si el valor de CPU es mayor a 80 y RAM es mayor a 80, entonces se indica: **Sobrecarga crítica** - **Se utiliza AND y 2 variables**
2. Si los valores de CPU y RAM estan entre 40 y 70, entonces se indica: **Estado normal** -
 **Se utilizan rangos numericos y 2 variables**
3. Si el valor de disco es menor a 30 o procesos es mayor a 80, entonces se indica: **Mantenimiento urgente** - **Se utiliza OR y 2 variables**
4. Si NOT firewall activo (por lo tanto, firewall inactivo), entonces se indica: **Riesgo de seguridad** - **Se utiliza NOT y 1 variable**
5. Si la opcion de servidor es "Web" y el valor de usuarios es mayor a 100 y CPU es mayor a 85, entonces se indica: **Escalar recursos** - **Se utiliza AND y 3 variables**
6. Si la opcion de servidor es "Base de datos" y el valor de disco es menor a 20 y el valor de RAM es mayor a 70, entonces se indica: **Riesgo en BDD** - **Se utiliza AND y 3 variables**


### Flujo de decisión

1. Se solicitan datos al usuario.
2. Se calculan valores como el promedio de uso de CPU y RAM.
3. Se evalúan reglas condicionales.
4. Se acumulan alertas en base a las condiciones cumplidas.
5. Se calcula un porcentaje de riesgo.
6. Se muestran los resultados y recomendaciones.


## **Ejemplo de ejecución**

### Datos ingresados
- CPU: 95%
- RAM: 92%
- Disco: 5 GB
- Usuarios: 200
- Procesos: 120
- Firewall: Inactivo
- Servidor: Web

### Resultado:

===============================================

Diagnostico del servidor: Prueba

El porcentaje del riesgo es: 100.0%
Su sistema operativo es: Linux

===============================================

Problemas detectados:  
🚨 Sobrecarga critica (CPU y RAM muy altas!)  
🚨 Sobrecarga critica (Disco o Procesos altos!)   
🚨 Riesgo de seguridad: firewall desactivado.   
🚨 Su servidor web tiene alta demanda, se recomienda escalar recursos.  


Recomendaciones:
- Reducir carga del sistema o mejorar hardware (CPU/RAM).  
- Liberar espacio en disco o revisar procesos innecesarios.  
- Activar el firewall para mejorar la seguridad.  
- Escalar recursos del servidor web o balancear carga.  

