import threading
import time
import random



class Filosofo(threading.Thread):
    def __init__(self, idFilosofo, garfoEsq, garfoDir):
        super().__init__()
        self.idFilosofo = idFilosofo
        self.garfoEsq = garfoEsq
        self.garfoDir = garfoDir
        self.rodando = True
            
    def run(self):
            while self.rodando:
                print(f"Filósofo {self.idFilosofo} está pensando.")
                time.sleep(random.randint(1, 3))
    
                print(f"Filósofo {self.idFilosofo} está com fome.")
                
                primeiro_garfo = self.garfoDir
                segundo_garfo =  self.garfoEsq
    
                primeiro_garfo.lock.acquire()
                print(f"Filósofo {self.idFilosofo} pegou o garfo {primeiro_garfo.numeroGarfo}.")
    
                segundo_garfo.lock.acquire()
                print(f"Filósofo {self.idFilosofo} pegou o garfo {segundo_garfo.numeroGarfo}.")
    
                print(f"Filósofo {self.idFilosofo} está comendo")
                time.sleep(random.randint(1, 3))
    
                segundo_garfo.lock.release()
                primeiro_garfo.lock.release()
                print(f"Filósofo {self.idFilosofo} terminou de comer e soltou os garfos.")
    


class Garfo:
    def __init__(self, numeroGarfo):
        self.numeroGarfo = numeroGarfo
        self.lock = threading.Lock() 


num = 5
garfos = [Garfo(i) for i in range(num)]
filosofos = []

for i in range(num):
    garfo_esquerda = garfos[i]
    garfo_direita = garfos[(i + 1) % num]
    
    filosofo = Filosofo(i, garfo_esquerda, garfo_direita)
    filosofos.append(filosofo)
    filosofo.start() 

