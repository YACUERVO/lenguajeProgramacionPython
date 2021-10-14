Reto 1

Se esta planeando un misión de exploración espacial tripulada hacia el exterior del sistema solar, específicamente hacia la nube de oort, región del espacio de mucho interés ya que contendría restos de la formación del sistema solar y por lo tanto podría llegar a tener claves importantes para entender los orígenes de la vida en la tierra, sin embargo, no se conoce con precisión la distancia de la tierra a los bordes exteriores de la nube, ya que los asteroides que la componen no emiten luz visible, por lo que no se puede usar la técnica de paralaje, sin embargo, algunos científicos tienen diferentes estimaciones de esta distancia calculadas por métodos indirectos. Se desea entender el esfuerzo logístico que implicaría llevar seres humanos a distancias tan lejanas.

Se conoce que el peso de la carga útil en toneladas requerida para un viaje de esta naturaleza, carga que incluye agua, comida, oxigeno y todo lo que los astronautas pudieran llegar a necesitar para el viaje, crece a razón del doble de la distancia a recorrer mas un peso de base de 4 toneladas. También se sabe que la cantidad de gigalitros de combustible necesarios para alcanzar la velocidad requerida para llegar a una distancia determinada, es de una quinta parte de la suma entre la distancia total a recorrer y el peso de la carga útil a llevar.

También se desea conocer el número de cohetes que se necesitarían para alojar el combustible a usar en el viaje. El centro de lanzamiento dispone de cuatro cohetes de propulsión que usan combustible liquido, pero dado que la cantidad de cohetes a usar depende de la cantidad de combustible, que a su vez depende de la distancia a recorrer, no se conoce cuantos cohetes se necesitarían para el viaje.

Si la cantidad de combustible necesaria fuera de 20 gigalitros o menos, solo se necesitaría un cohete, si la cantidad fuera mayor a 20 gigalitros, pero igual o menor a 30 gigalitros, se necesitarían dos cohetes. Para cantidades de combustible mayores a 30 gigalitros, pero iguales o menores a 50 gigalitros, se necesitarían tres cohetes, para cantidad de combustible mayores a 50 gigalitros se necesitarían los cuatro cohetes.

El reto consiste en crear un programa escrito en lenguaje de programación Python, que reciba la distancia estimada desde la tierra a la nube de oort, medida en unidades astronómicas, y muestre como resultado tres datos: La misma distancia recibida por el programa, el peso de la carga útil en toneladas y la cantidad de combustible en gigalitros requerida para el viaje hasta la nube.

Estos datos deben ser mostrados como números enteros, separados por un espacio y sin mostrar las unidades de medida. Dado que estamos tratando con estimaciones, todas las distancias, pesos y volúmenes deben ser redondeados a números enteros, por lo que no deben ser mostradas con cifras decimales.

En la siguiente línea, el programa debe mostrar la cantidad de cohetes que se requerirían para alojar todo el combustible necesario en el viaje, pero en este caso, la cantidad se debe mostrar en formato texto: Si la cantidad de cohetes es 1, el programa debe mostrar el texto “uno”, si es 2 debe mostrar el texto “dos”, si es 3 debe mostrar el texto “tres”, y si es 4 debe mostrar el texto “cuatro”. Todos los textos deben ser mostrados en minúsculas, sin excepción.


Ejemplos:

A modo de ejemplo, si la distancia estimada a la nube de oort que es ingresada al programa es de 100 unidades astronómicas, el peso de la carga útil seria de 204 toneladas, la cantidad de combustible seria de 60 gigalitros, y por lo tanto se necesitarían cuatro cohetes para realizar el viaje.

Entrada
	

Salida

100
	

100 204 60
cuatro

En un segundo ejemplo, si la distancia estimada a la nube de oort que es ingresada al programa es de 35 unidades astronómicas, el peso de la carga útil seria de 74 toneladas, la cantidad de combustible seria de 21 gigalitros, y por lo tanto se necesitarían dos cohetes para realizar el viaje.

Entrada
	

Salida

35
	

35 74 21
