Reto 5

Daniel, nuestro ferviente coleccionista de láminas Marvel, regresó de su viaje a Estados Unidos, y está ansioso de mostrar a sus amigos todas las laminas que compró en el viaje. Todos están impresionados por las laminas adquiridas por Daniel, y naturalmente sus amigos desean intercambiar laminas. 

Se listan todas las laminas Marvel disponibles:

Colección Completa de laminas Marvel

Número Identificador
	

Nombre

1
	

CaptainAmerica

2
	

BlackPanther

3
	

Killmonger

4
	

Groot

5
	

Hawkeye

6
	

BlackWidow

7
	

TheWinterSoldier

8
	

Star-Lord

9
	

Wolverine

10
	

IronMan

11
	

Ultron

12
	

ScarletWitch

13
	

Vision

14
	

IronFist

15
	

Hulk

16
	

Spider-Man

17
	

Loki

18
	

BlackBolt

19
	

CaptainMarvel

20
	

LukeCage

21
	

Quicksilver

22
	

GhostRider

23
	

Daredevil

24
	

Spider-Woman

25
	

SilverSurfer

26
	

DoctorStrange

27
	

Cyclops

28
	

Falcon

29
	

Quake

30
	

MoonKnight

31
	

Beast

32
	

Iceman

33
	

TheThing

34
	

KittyPryde

35
	

JeanGrey

36
	

TheInvisibleWoman

37
	

NickFury

38
	

Venom

39
	

Deadpool

40
	

Storm

41
	

ThePunisher

42
	

ProfessorX

43
	

Thanos

44
	

Thor

45
	

Ant-Man

46
	

Wasp

47
	

Magneto

48
	

JessicaJones

49
	

Blade

50
	

DoctorDoom

51
	

TheMandarin

52
	

Gamora

53
	

Rocket

54
	

Nebula

55
	

DraxTheDestroyer

56
	

Mantis

57
	

Wong

58
	

AncientOne

59
	

Kaecilius

60
	

Dormammu

61
	

Okoye

62
	

Shuri

63
	

Ikaris

64
	

Thena

65
	

Kingo

66
	

Ajak

67
	

Makkari

68
	

Phastos

69
	

Sprite

70
	

Gilgamesh

71
	

Malekith

72
	

EgoTheLivingPlanet

73
	

HowardTheDuck

74
	

RedSkull

75
	

RonanTheAccuser

76
	

Hela


No todas las laminas son iguales, algunas son mas raras que las demás, así que según su rareza se clasifican en clases, listadas a continuación:

Clases de láminas Marvel

Número Identificador
	

Nombre

1
	

Diamond

2
	

Gold

3
	

Silver

4
	

Bronze

5
	

Normal


Daniel está un poco abrumado por todo el tiempo y esfuerzo que requeriría el proceso de intercambio de laminas Marvel con sus amigos, por que usted se ofrece a ayudarle en el proceso, para ello usted se propone crear un módulo en Python llamado laminas_marvel, que contenga las siguientes 4 funciones listadas y descritas a continuación. Nota: Por practicidad, las funciones no usarán los nombres de las laminas o clases sino sus números identificadores, tanto en los datos de entrada como los de salida:

1. Función lista_clases: Dada una lista de las clases de todas las láminas Marvel de Daniel, la función debe retornar una lista con las clases de láminas que se encuentran en la lista de Daniel, en estricto orden en el que son detectadas las clases si son leídas de la primera a la última.

Ejemplos para la función lista_clases()

Entrada
	

Salida

[3,2,1,1,1,3,2,1,1,1]
	

[3,2,1]

[2, 3, 2, 1, 2, 2, 1, 4, 4, 1, 4, 1, 2, 1, 4, 3, 4, 2, 3, 1, 2, 4, 3, 1, 2, 1, 1, 3, 4, 4, 3, 3, 2, 4, 2, 2, 1, 3, 1, 3, 4, 2, 1, 2, 2, 2, 4, 1, 4, 3, 4, 4, 4, 4, 3, 4, 2, 2, 2, 4, 1, 1, 2, 3, 1, 3, 2, 4, 2, 3]
	

[2, 3, 1, 4]

[1, 1, 2, 4, 4, 4, 3, 3, 4, 1, 5, 3, 2, 1, 2, 1, 2, 5, 1, 4, 3, 3, 2, 4, 5, 2, 4, 2, 4, 1, 3, 1, 5, 5, 1, 1, 2, 3, 5, 1, 1, 3, 2, 3, 1, 3, 1, 2, 3, 3, 4, 4, 1, 3, 1, 5, 4, 5, 4, 3, 1, 4, 2, 1, 5, 3]
	

[1, 2, 4, 3, 5]


2. Función laminas_faltantes_por_clase: Se tiene la lista de las clases de las laminas disponibles para cambiar que tiene un amigo, Daniel la revisa rápidamente y crea una lista de los índices (el conteo inicia desde 0) de las laminas que no tiene de dicha lista. Dada la lista de índices (el conteo inicia desde 0) de laminas que le faltan a Daniel de la lista del amigo, la lista de clases de las laminas del amigo y una clase particular, la función debe retornar una lista con los índices de las laminas de dicha clase particular que le faltan a Daniel.

Ejemplos para la función laminas_faltantes_por_clase()

Entrada
	

Salida

[1,3,6,8]

[3,2,1,1,1,3,2,1,1,1]

1
	

[3,8]

[1,3,6,8]

[3,2,1,1,1,3,2,1,1,1]

2
	

[1,6]

[54, 27, 3, 49, 24, 43, 22, 13, 37, 34, 10, 2, 58, 32, 47, 38, 57, 33, 9, 19, 23, 16, 25, 5, 7, 52, 26]

[4, 1, 2, 4, 2, 5, 2, 4, 3, 2, 4, 2, 4, 2, 2, 1, 5, 1, 2, 4, 2, 3, 2, 1, 4, 2, 3, 1, 1, 5, 3, 2, 4, 3, 3, 4, 2, 4, 1, 3, 2, 1, 4, 1, 3, 1, 2, 5, 5, 1, 5, 5, 2, 3, 3, 3, 3, 5, 1]

4
	

[3, 24, 37, 10, 32, 19, 7]

[35, 16, 40, 43, 6, 32, 68, 15, 33, 45, 11, 26, 42, 30, 48, 3, 54, 23, 69, 4, 46, 1, 39, 25, 62, 2, 28, 10, 19, 12]

[5, 3, 4, 4, 5, 4, 5, 1, 2, 2, 4, 4, 4, 4, 1, 5, 2, 1, 2, 5, 5, 5, 4, 2, 4, 4, 5, 3, 5, 2, 3, 3, 5, 4, 4, 4, 3, 4, 5, 2, 3, 1, 1, 4, 4, 4, 3, 1, 1, 1, 3, 5, 4, 5, 3, 5, 5, 4, 2, 3, 1, 1, 5, 4, 5, 5, 1, 3, 1, 5, 5]

3
	

[40, 30, 54, 46, 1]


3. Función laminas_faltantes: Dada una lista con las láminas que tiene un amigo y la lista con las láminas que tiene Daniel, la función debe retornar la lista con las láminas que le interesarían intercambiar a Daniel de la lista su amigo.

Ejemplos para la función laminas_faltantes()

Entrada
	

Salida

[3,5,7,10,15,16]

[4,10,5,8]
	

[3,7,15,16]

[10, 52, 38, 35, 63, 44, 2, 5, 8, 16, 25, 59, 28, 61, 29, 21, 48, 53, 26, 31, 60, 65, 40, 4, 57] 

[10, 35, 7, 54, 43, 45, 44, 56, 47, 60, 12, 9, 27, 22, 4, 53, 23, 20, 38, 41, 14, 8, 25]
	

[52, 63, 2, 5, 16, 59, 28, 61, 29, 21, 48, 26, 31, 65, 40, 57]

[17, 9, 70, 33, 69, 22, 4, 67, 27, 36, 39, 2, 45, 61, 71, 25, 16, 50, 49, 46, 11, 63, 24, 66, 6, 5, 15, 14]

[29, 1, 58, 19, 16, 31, 4, 50, 68, 51, 52, 20, 67, 66, 53, 34, 47, 21, 42, 10, 24, 59, 13, 57, 43, 65, 44, 33, 7, 46, 45, 6]
	

[17, 9, 70, 69, 22, 27, 36, 39, 2, 61, 71, 25, 49, 11, 63, 5, 15, 14]


4. Función cantidad_laminas_cambiables: Dada la lista de láminas que tiene un amigo y la lista de láminas que tiene Daniel, la función debe retornar el número de láminas que pueden cambiar. La lista que maneja cada persona indica los números de las láminas que tienen para cambiar y aquellos números que no están en dicha lista son los que necesitan.

Ejemplos para la función cantidad_laminas_cambiables()

Entrada
	

Salida

[3,5,7,10,15,16]

[4,10,5,8]
	

2

[18, 56, 17, 28, 54, 35, 4, 13, 23, 12, 47, 33, 3, 30, 44, 39, 15, 11, 31, 49, 22, 25, 32, 19, 36]

[47, 29, 4, 45, 49, 9, 1, 53, 8, 28, 6, 41, 37, 23, 50, 12, 42, 35, 7, 43, 31, 34, 51, 14, 22, 25]
	

15

[38, 5, 6, 60, 61, 8, 53, 25, 54, 22, 21, 11, 19, 24, 44, 37, 40, 4, 17, 15, 16, 56] 

[38, 15, 18, 12, 59, 3, 14, 35, 30, 4, 2, 60, 58, 6, 56, 46, 7, 26, 27, 20, 11, 54, 55, 24, 37, 21, 31, 13, 40]
	

10


Crear un módulo en lenguaje de programación Python llamado laminas_marvel que contenga únicamente las 4 funciones listadas antes, las cuales deben tener los nombres indicados. Ninguna de las funciones debe mostrar información en la consola usando print(), en cambio, los datos de salida deben ser retornados por la función. Ninguna de las funciones debe recibir información ingresada por el usuario usando input(), en cambio, los datos de entrada serán almacenados en las variables de entrada de la función. El módulo debe estar contenido en un archivo llamado laminas_marvel.py y debe seguir la siguiente plantilla:

def lista_clases(clases):
  resultado = []
  # Algoritmo
  return resultado


def laminas_faltantes_por_clase(indices, clases, clase_a_verificar):
  resultado = []
  # Algoritmo
  return resultado


def laminas_faltantes(laminas_persona_1, laminas_persona_2):
  resultado = []
  # Algoritmo
  return resultado


def cantidad_laminas_cambiables(laminas_persona_1, laminas_persona_2):
  resultado = 0
  # Algoritmo
  return resultado