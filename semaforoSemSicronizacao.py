import threading
import time

numeroDeThreads = 8
execucoes = 200000
valorEsperado = numeroDeThreads * execucoes
count = 0

def soma():
    global count
    for i in range(execucoes):
        count += 1  

threads = [threading.Thread(target=soma) for i in range(numeroDeThreads)]
inicio = time.perf_counter()
for i in threads: i.start()
for i in threads: i.join()
tempo = time.perf_counter() - inicio

print(f"Esperado: {valorEsperado}")
print(f"(Sem sincronização) Obtido: {count} Tempo: {tempo:.3f}s")
