Reto 3

Alejandra trabaja como coordinadora de operaciones en la Terminal de Transporte de Bogotá, y se le ha encomendado la tarea de determinar las frecuencias de viajes terrestres consecutivos realizados por las empresas de transporte de pasajeros que operan en la terminal en un día determinado. Las empresas de transporte son identificadas mediante las siguientes siglas mostradas a continuación:

Siglas
	

Nombre de la Empresa de Transporte

A
	

Transportes Alianza

B
	

Transportes y Turismo Berlinas del Fonce

C
	

Coflonorte Los Libertadores

E
	

El Rápido Duitama Ltda.

F
	

Cootransfusa

G
	

Copetran

I
	

Transportadores De Ipiales

J
	

Expreso Brasilia

L
	

Cootransbol

M
	

Flota Magdalena

N
	

Expreso Bolivariano

O
	

Omega

P
	

Transportes Expreso Palmira

R
	

Rápido El Carmen

S
	

Socotrans

T
	

Flota Valle De Tenza

V
	

Velotax Ltda.

W
	

Coomotor

X
	

Expreso Los Comuneros

Y
	

Nueva Flota Boyacá

Z
	

Flota La Macarena


Alejandra recibe como insumo para la tarea encomendada una lista de todos los viajes realizados por las empresas de transporte en estricto orden de salida de la terminal, en el siguiente formato que usa las siglas de las empresas:

N N N J P P N N

Esta lista de viajes, que se lee de izquierda a derecha, indica que primero se realizaron 3 viajes de Expreso Bolivariano (N), luego 1 viaje de Expreso Brasilia (J), luego 2 viajes de Transportes Expreso Palmira (P), y finalmente 2 viajes de Expreso Bolivariano (N). Alejandra debe comunicar a sus superiores estas frecuencias en el siguiente formato en dos líneas:

N J P N

3 1 2 2

Es importante resaltar que las siglas de las empresas de transporte de pasajeros están separadas por un espacio en blanco, de igual manera para las frecuencias:

Entrada
	

Salida

N N N J P P N N

 
	

N J P N
3 1 2 2


Crear un programa en lenguaje de programación Python que reciba la lista de viajes realizados por las empresas de transporte de pasajeros en un día, y muestre como resultado el conteo de frecuencias consecutivas en dos filas. Tanto los datos de entrada como los datos de salida deben estar separados por un espacio en blanco entre caracteres. La salida debe mostrarse en dos líneas.

Se adjuntan a continuación más ejemplos, con entradas y salidas diferentes:

Entrada
	

Salida

J J J J N N N V V V J J J A A A A R R R R S I I I I O O O L L

 
	

J N V J A R S I O L
4 3 3 3 4 4 1 4 3 2

M M M P P J J J J A C M I I O O O T T C

 
	

M P J A C M I O T C
3 2 4 1 1 1 2 3 2 1

N G G G G W W W N N N N N N N L Z B S S I I I I

 
	

N G W N L Z B S I
1 4 3 7 1 1 1 2 4

S S S S S J J N N N N N N V V V V P P P P X X X F F O O O O

 
	

S J N V P X F O
5 2 6 4 4 3 2 4