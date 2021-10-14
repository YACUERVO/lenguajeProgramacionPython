#se importa la librería de python random
import random

#se define una lista
sujetos = ["mami", "bebé", "princess", "mami"]
intenciones = ["yo quiero", "yo puedo", "yo vengo a", "voy a"]
verbos = ["encendelte", "amalte", "ligal", "jugal"]
advs = ["suave", "lento", "lápido", "fuelte"]
complementos_uno = ["hasta que salga el sol", "toda la noche", "hasta el amanecer", "todo el día"]
complementos_dos = ["sin anestesia", "sin compromiso", "feis to feis", "sin miedo"]

#se utiliza la librería para seleccionar un elemento al azar de la lista sujetos
sujeto_seleccionado = random.choice(sujetos)
intencion_seleccionada = random.choice(intenciones)
verbo_seleccionado = random.choice(verbos)
adv_seleccionado = random.choice(advs)
compl1s_seleccionado = random.choice(complementos_uno)
compl2s_seleccionado = random.choice(complementos_dos)

#se imprime la canción
print("letra generada: " + sujeto_seleccionado + " " + intencion_seleccionada + " " + verbo_seleccionado + " " 
      + adv_seleccionado + " " + compl1s_seleccionado + " " + compl2s_seleccionado)

