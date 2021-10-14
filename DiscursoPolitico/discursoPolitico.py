#se importa la libreria 

#Modificar el algoritmo que compone reggaeton como Melquiades, para que ahora genere Discursos Políticos, utilizando como datos de entrada la tabla "Como hacer un discurso politico" mostrada en clase, la cual está adjuntada en esta actividad. Deben enviar la entrega mediante esta actividad en Google Classroom, no por correo electronico, el archivo a enviar puede ser un archivo Python (.py), un archivo comprimido generado desde Repl.it (.zip) o un notebook de Google Colaboratory (.ipynb). La actividad es opcional, individual, puede ser desarrollada en Repl.it, Google Colaboratory, Visual Studio Code, PyCharm o cualquier otra herramienta de su preferencia, y no cuenta como uno de los retos del componente de Programación del Ciclo 1 del programa.

import random


lambetazo = ["queridos", "apreciados", "distinguidos","honorables","estimados","respetados"];
pontencialesMarranos=["compatriotas","conciudadanos","amigos","coterraneos","compartidarios","electores"];
condicion = ["en mi gobierno","con su apoyo","siendo elegido","con su ayuda","si me siguen","duante mi mandato"];
compromiso=["voy derrotar","vencere","eliminare","acabare","luchare contra","combatire"];
ilusionGuerrerista =["la violencia y","la delicuencia y","la corrupcion y","la inflacion y","la porbreza y","el desplazamiento y"];
promesa=["trabajare por","garantizare","protegere","velare por","promovere","defendere"];
beneficioPpulista=["la educacion","el empleo","la seguridad","la paz","la igualdad","la salud"];
cantidadVotos=["del pais","de la ciudad","de la comunidad","de la poblacion","para toda la gente","de cada colombiano"];

lambetazo1 = random.choice(lambetazo);
pontencialesMarranos1=random.choice(pontencialesMarranos);
condicion1=random.choice(condicion);
compromiso1=random.choice(compromiso);
ilusionGuerrerista1=random.choice(ilusionGuerrerista);
promesa1=random.choice(promesa);
beneficioPpulista1=random.choice(beneficioPpulista);
cantidadVotos1=random.choice(cantidadVotos);

#imprimir resultado 

print("Yo su candidato presidencial vengo con el siguiente disurso de politiqueria barata" + " " + lambetazo1 + " " + pontencialesMarranos1 + " " + condicion1 + " " + compromiso1 + " " + ilusionGuerrerista1 + " " + promesa1 + " " + beneficioPpulista1 + " " + cantidadVotos1);



