import threading
import time

def hilos(): #funcion random
  print ("hilo principal inicio")
  time.sleep(10)
  print ("hilo principal fin")

prueba = threading.Thread(target= hilos) #creamos un threading que iniciará un hilo de ejecución  
prueba.start() #iniciamos el threading
print ("hilo secundario") #al estar ejecutance el threading, se crea un segundo hilo de ejecución mientras se mantiene en ejecución el primero hasta que cumpla el tiempo de 10 segundos (en este caso) y finalice su ejecucion
