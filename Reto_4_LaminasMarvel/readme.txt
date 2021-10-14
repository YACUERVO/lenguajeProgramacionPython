Reto 4

Daniel es un ávido coleccionista de láminas Marvel y se encuentra de viaje en Estados Unidos, específicamente se encuentra visitando Nueva York. Recorriendo la ciudad encontró un sector con varias tiendas especializadas que venden láminas Marvel, y luego de una rápida inspección de las tiendas se dio cuenta que algunas de ellas difícilmente las encontraría en Colombia.

A continuación, se lista la colección completa de las láminas Marvel:

Colección Completa de laminas Marvel

ID
	

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


Como buen coleccionista, Daniel carga consigo una lista de las láminas Marvel que le faltan para completar su colección, y quiere utilizar todo el dinero del que dispone en el momento para comprar tantas láminas como pueda de dicha lista, ya que difícilmente tendría opción de volver a Estados Unidos en el corto plazo, sin embargo, el dinero es escaso, así que su idea es optimizar de la mejor manera el uso del dinero, y poder comprar la mayor cantidad de láminas Marvel con el dinero disponible.

Sin embargo, las tiendas no venden láminas Marvel al detal, solo al por mayor, lo que obliga a comprarlas todas en una sola tienda, tampoco las venden por internet, la compra debe realizarse de manera presencial, además cada tienda tiene una disponibilidad diferente de láminas Marvel y usualmente cada lámina es vendida a un precio diferente en cada tienda, precio que depende de su rareza.

El dilema de Daniel es elegir la tienda en la que pueda comprar la mayor cantidad de láminas Marvel con el dinero disponible, por lo que Daniel procede a preguntar en cada tienda cuales láminas tienen disponibles a la venta y a que precio las venden. A modo de ejemplo, en una de las tiendas, estas son las láminas Marvel disponibles y su precio en dólares:

Ejemplo: Láminas Marvel disponibles en una tienda

Nombre
	

Precio en dólares

Hulk
	

81

Thor
	

28

Falcon
	

52

IronMan
	

87

Venom
	

56

Deadpool
	

39

CaptainMarvel
	

29

CaptainAmerica
	

81

Hawkeye
	

67

ScarletWitch
	

86


Esta información también puede ser representada como un diccionario en formato JSON así:

{"Hulk":81, "Thor": 28, "Falcon": 52, "IronMan": 87, "Venom": 56, "Deadpool": 39, "CaptainMarvel": 29, "CaptainAmerica": 81, "Hawkeye": 67, "ScarletWitch":86}


Daniel luego compara dicha tabla con su lista de las láminas Marvel que le faltan para completar su colección, a modo de ejemplo, su lista de láminas faltantes es:

Ejemplo: Láminas Marvel que faltan para completar la colección

ID
	

Nombre

4
	

Groot

7
	

TheWinterSoldier

10
	

IronMan

38
	

Venom

28
	

Falcon

5
	

Hawkeye

39
	

Deadpool


Al hacer la comparación se da cuenta que de las laminas Marvel que le faltan, solo puede comprar 5 en esa tienda: IronMan, Venom, Falcon, Hawkeye y Deadpool, y el precio total a pagar seria de 301 dólares:

Ejemplo: Laminas Marvel que le faltan y que puede conseguir en la tienda

Nombre
	

Precio en dólares

IronMan
	

87

Venom
	

56

Falcon
	

52

Hawkeye
	

67

Deadpool
	

39

Precio Total:
	

301


Se muestra a continuación el ejemplo anterior en formato de Entradas / Salidas:

Entrada
	

Salida

{"Hulk": 81, "Thor": 28, "Falcon": 52, "IronMan": 87, "Venom": 56, "Deadpool": 39, "CaptainMarvel": 29, "CaptainAmerica": 81, "Hawkeye": 67, "ScarletWitch": 86}
Groot TheWinterSoldier IronMan Venom Falcon Hawkeye Deadpool
	

301
IronMan Venom Falcon Hawkeye Deadpool



Crear un programa en lenguaje de programación Python que reciba como datos de entrada un diccionario en formato JSON con las láminas Marvel disponibles en una tienda y su precio correspondiente, además de la lista de las láminas que le faltan para completar su colección (los nombres deben estar separados por un espacio en blanco), y muestre como resultado las láminas Marvel disponibles en la tienda y que se encuentran en su lista para completar la colección (también separados por espacio en blanco), así como el precio total si las comprara. Dado que el dato que mas le interesa a Daniel es el precio total que pagaría, este debe ser mostrado en la primera línea.

Nota: Por facilidad al momento de ingresar los datos de entrada, todos los espacios en blanco en los nombres de las laminas Marvel fueron removidos.

Se adjuntan a continuación mas ejemplos, para listas de laminas faltantes y para tiendas diferentes, así como su resultado esperado respectivo:  

Entrada
	

Salida

{"Thanos": 65, "Groot": 16, "TheThing": 62, "Kingo": 100, "DoctorDoom": 79, "DraxTheDestroyer": 36, "Okoye": 76, "Sprite": 46, "Ikaris": 52, "Killmonger": 32, "Makkari": 11, "Hela": 85, "BlackPanther": 84, "Quake": 83, "IronMan": 16, "ScarletWitch": 40, "Venom": 38, "Beast": 94, "Malekith": 30, "IronFist": 35, "Wasp": 75, "CaptainMarvel": 77, "BlackWidow": 21, "RonanTheAccuser": 13, "SilverSurfer": 76, "Kaecilius": 16, "MoonKnight": 48, "Wong": 15, "Spider-Man": 75, "JeanGrey": 45, "Cyclops": 47, "Ant-Man": 81, "GhostRider": 92}
CaptainMarvel Magneto LukeCage Dormammu TheThing KittyPryde Hulk Storm Mantis TheWinterSoldier Wong Thor TheInvisibleWoman IronMan Hela Cyclops Star-Lord Beast RonanTheAccuser Sprite Shuri CaptainAmerica Rocket BlackBolt Ultron
	

455
CaptainMarvel TheThing Wong IronMan Hela Cyclops Beast RonanTheAccuser Sprite


Entrada
	

Salida

{"Spider-Woman": 47, "Okoye": 89, "AncientOne": 43, "TheWinterSoldier": 11, "Wong": 89, "KittyPryde": 72, "Nebula": 64, "SilverSurfer": 77, "Malekith": 38, "EgoTheLivingPlanet": 95, "Sprite": 92, "Loki": 21, "Ant-Man": 12, "DraxTheDestroyer": 51, "Quicksilver": 42, "Thor": 82, "Quake": 44, "Star-Lord": 42, "Hulk": 89, "Hawkeye": 74, "CaptainMarvel": 35, "Mantis": 78, "HowardTheDuck": 66, "Daredevil": 21, "ProfessorX": 74, "Ajak": 65, "Killmonger": 67, "Blade": 43}
Thena Thor TheWinterSoldier Venom Cyclops Vision Wasp Ikaris TheMandarin EgoTheLivingPlanet ProfessorX HowardTheDuck NickFury Sprite Quicksilver Gilgamesh DoctorDoom Dormammu ScarletWitch Phastos DoctorStrange Okoye LukeCage Makkari JessicaJones SilverSurfer Rocket Blade BlackWidow Ajak Spider-Man Magneto
	

736
Thor TheWinterSoldier EgoTheLivingPlanet ProfessorX HowardTheDuck Sprite Quicksilver Okoye SilverSurfer Blade Ajak


Entrada
	

Salida

{"Thor": 45, "Gilgamesh": 97, "Dormammu": 20, "Nebula": 65, "DoctorStrange": 64, "Malekith": 23, "CaptainAmerica": 18, "DoctorDoom": 46, "Vision": 64, "TheMandarin": 32, "Spider-Man": 79, "Mantis": 98, "Quake": 84, "Sprite": 53, "SilverSurfer": 91, "JessicaJones": 80, "Venom": 48, "Wolverine": 87, "LukeCage": 12, "Loki": 43, "Phastos": 35, "Shuri": 47, "Hulk": 58, "Makkari": 26, "DraxTheDestroyer": 26, "Wasp": 73, "RonanTheAccuser": 61}
Killmonger Nebula Ant-Man Hawkeye Gamora Blade Vision Quake ProfessorX JeanGrey Cyclops Hulk TheWinterSoldier Ikaris TheInvisibleWoman Hela Wasp Spider-Man Magneto Mantis BlackBolt IronFist SilverSurfer Beast Thanos DoctorStrange Kaecilius RonanTheAccuser KittyPryde Dormammu Venom Iceman GhostRider IronMan BlackPanther Spider-Woman Gilgamesh Ajak
	

902
Nebula Vision Quake Hulk Wasp Spider-Man Mantis SilverSurfer DoctorStrange RonanTheAccuser Dormammu Venom Gilgamesh

 

Entrada
	

Salida

{"Loki": 92, "HowardTheDuck": 46, "DoctorDoom": 88, "Mantis": 13, "Rocket": 52, "NickFury": 98, "Malekith": 90, "Iceman": 62, "Gilgamesh": 12, "JessicaJones": 50, "Deadpool": 31, "IronFist": 44, "RonanTheAccuser": 12, "RedSkull": 11, "Cyclops": 39, "Okoye": 16, "Hela": 97, "CaptainAmerica": 74, "Spider-Woman": 76, "Sprite": 46, "LukeCage": 65, "GhostRider": 33, "Gamora": 15, "Phastos": 28, "Killmonger": 49, "Ajak": 15, "Kingo": 69, "EgoTheLivingPlanet": 20, "Beast": 65, "Groot": 66, "SilverSurfer": 98, "Shuri": 50, "TheThing": 55}
Quicksilver Star-Lord Loki JeanGrey AncientOne Quake Venom Deadpool Wasp Kingo Wolverine Vision Hela Gamora JessicaJones BlackWidow TheThing Iceman SilverSurfer CaptainAmerica Wong ScarletWitch Malekith DraxTheDestroyer Shuri BlackBolt RonanTheAccuser Spider-Man
	

795
Loki Deadpool Kingo Hela Gamora JessicaJones TheThing Iceman SilverSurfer CaptainAmerica Malekith Shuri RonanTheAccuser