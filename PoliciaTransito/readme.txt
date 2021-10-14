Un policia de transito está de guardia en una autopista monitoreando con su radar de velocidad a todos los conductores que transitan la via y deteniendo a los que imcumplen las normas de transito. Crear un programa en lenguaje de programación Python que determine si el policia deberia permitirle a un conductor, que ha sido detenido, seguir su camino o no, para ello el programa debe recibir los siguientes datos:

    Si tiene licencia de conducción o no (Valor booleano: Si=1  No=0)
    La cantidad de multas de transito (Número entero)
    La cantidad de grados de alcohol en la sangre (Número decimal)
    La velocidad a la que se desplazaba el vehiculo (Número decimal)
    Si tiene los papeles en regla o no (Valor booleano: Si=1  No=0)
    Si tiene vidrios polarizados o no (Valor booleano: Si=1  No=0)
    La edad de la persona (Número entero)


La persona puede seguir su camino solo si se cumplen las siguientes condiciones:

    Si tiene licencia de conducción
    Si la cantidad de multas de transito es cero
    Si la cantidad de grados de alcohol en la sangre es cero
    Si la velocidad de desplazamiento del vehiculo es mayor a cero y menor o igual a 80 km/h
    Si tiene los papeles en regla
    Si no tiene vidrios polarizados
    Si la persona tiene 18 años o mas, y menos de 75 años


El programa debe mostrar en la consola True si la persona puede seguir su camino, y False en caso contrario