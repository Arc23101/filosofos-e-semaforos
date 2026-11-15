import threading
import time

numeroDeThreads = 8
execucoes = 200000
valorEsperado = numeroDeThreads * execucoes

count = 0
semaforo = threading.Semaphore(1)  

def somaComSincronia():
    global count
    for i in range(execucoes):
        semaforo.acquire()
        try:
            count += 1
        finally:
            semaforo.release()


threads = [threading.Thread(target=somaComSincronia) for i in range(numeroDeThreads)]
inicio = time.time()
for i in threads: i.start()
for i in threads: i.join()
tempo = time.time() - inicio

print(f"Esperado: {valorEsperado}")
print(f"(Com sincronia) Obtido: {count} Tempo: {tempo:.3f}s")