Reto 2

Alejandro y Carolina son aficionados a las carreras de Fórmula 1 y deciden apostar por sus escuderías favoritas en todas las carreras de la próxima temporada. 

Para ello, cada uno escribe la lista de sus escuderías favoritas, pero por facilidad, en vez de anotar todo el nombre, le asignan a cada escudería una letra identificadora. A continuación, se muestran todas las escuderías en competencia y sus letras identificadoras:

Letra Identificadora
	

Nombre de la Escudería

A
	

Alfa Romeo

B
	

BMW Sauber

C
	

Racing Point

E
	

Mercedes

F
	

Ferrari

H
	

Haas

I
	

Force India

L
	

Lotus

M
	

McLaren

N
	

Renault

O
	

Manor

P
	

Alpine

R
	

Red Bull

S
	

Aston Martin

T
	

Toro Rosso

U
	

Marussia

W
	

Williams

Z
	

AlphaTauri


Por ejemplo, si las escuderías favoritas de Alejandro son:

    R: Red Bull
    A: Alfa Romeo
    I: Force India
    F: Ferrari
    Z: AlphaTauri

Y las escuderías favoritas de Carolina son:

    U: Marussia
    Z: AlphaTauri
    E: Mercedes
    O: Manor
    F: Ferrari

Entonces, Alejandro anota su lista de escuderías favoritas como RAIFZ, y Carolina las anota como UZEOF.

Adicionalmente, en una lista conjunta van escribiendo quien va a la delantera en la cantidad de puntos, los cuales se asignan por cada acierto. Al concluir cada una de las carreras miran si la escudería ganadora está en una de sus listas, de ser así, se anotan un punto y luego comparan sus puntuaciones: Si Alejandro lleva más puntos en ese momento entonces en la lista conjunta escriben una 'A', si Carolina lleva más puntos escriben una 'C', pero si tienen los mismos puntos en ese momento, se escribe una 'E' de empate.

A modo de ejemplo:

    Si la carrera #1 la gana I (Force India), Alejandro se anota un punto y Carolina no, quedando Alejandro=1 / Carolina=0, por lo tanto, en la lista conjunta anotan A.
    Si la carrera #2 la gana H (Haas), ninguno de los dos se anota punto, quedando Alejandro=1 / Carolina=0, por lo tanto, en la lista conjunta anotan A.
    Si la carrera #3 la gana Z (AlphaTauri), ambos se anotan puntos, quedando Alejandro=2 / Carolina=1, por lo tanto, en la lista conjunta anotan A.
    Si la carrera #4 la gana O (Manor), Carolina se anota un punto y Alejandro no, quedando Alejandro=2 / Carolina=2, por lo tanto, en la lista conjunta anotan E.
    Si la carrera #5 la gana W (Williams), ninguno de los dos se anota punto, quedando Alejandro=2 / Carolina=2, por lo tanto, en la lista conjunta anotan E.
    Si la carrera #6 la gana F (Ferrari), ambos se anotan puntos, quedando Alejandro=3 / Carolina=3, por lo tanto, en la lista conjunta anotan E.
    Si la carrera #7 la gana E (Mercedes), Carolina se anota un punto y Alejandro no, quedando Alejandro=3 / Carolina=4, por lo tanto, en la lista conjunta anotan C.
    Si la carrera #8 la gana I (Force India), Alejandro se anota un punto y Carolina no, quedando Alejandro=4 / Carolina=4, por lo tanto, en la lista conjunta anotan E.

El ejemplo anterior puede ser resumido, usando solo las letras identificadoras, así:

    Lista de escuderías favoritas de Alejandro: RAIFZ
    Lista de escuderías favoritas de Carolina: UZEOF
    Ganadores de las carreras de la temporada: IHZOWFEI
    Anotaciones en la lista conjunta de comparaciones de puntajes: AAAEEECE

Entrada
	

Salida

RAIFZ
UZEOF
IHZOWFEI
	

AAAEEECE 


Crear un programa en lenguaje de programación Python que reciba las listas de las escuderías favoritas de Alejandro y Carolina, y la lista de escuderías ganadoras de toda la temporada, listas escritas usando solo las letras identificadoras de las escuderías, y muestre lo anotado en la lista conjunta al final de la temporada. Las listas deben ser ingresadas como Strings (cadena de texto).

Se adjuntan a continuación mas ejemplos, con entradas y salidas diferentes:

Entrada
	

Salida

OZCUT
PACIF
LOZLPIIMIUZSSWBAOPUPHPZIE
	

EAAAAECCCCEEEEECECECCCCCC

PAWO
NLMO
TPZLIFCIAUHNHWBIWRWU
	

EAAEEEEEAAAEEAAAAAAA

SEO
MAB
MOLLCPCTFRSETELMTZBLOTHOZIHB
	

CEEEEEEEEEAAAAAAAAAAAAAAAAAA

SAUCFM
AULINB
RPWZWLWAEBCROEWZMUR
	

EEEEECCCCCCCCCCCEEE