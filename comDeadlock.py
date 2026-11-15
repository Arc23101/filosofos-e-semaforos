import threading
import time

lockA = threading.Lock()
lockB = threading.Lock()

def threadComDeadA(nome):
  
    print(f"{nome}: Tentando travando A")
    lockA.acquire()
    print(f"{nome}: travou A, agora tentando travando B")
    time.sleep(0.05)  

    lockB.acquire()
    print(f"{nome}: Travou B")
    time.sleep(0.05)  


    lockB.release()
    lockA.release()
    print(f"{nome}: Terminou e liberou tudo")

def threadComDeadB(nome):
  
    print(f"{nome}: Tentando travando B")
    lockB.acquire()
    print(f"{nome}: travou B, agora tentando travando A")
    time.sleep(0.05)  

    lockB.acquire()
    print(f"{nome}: Travou A")
    time.sleep(0.05)  


    lockB.release()
    lockA.release()
    print(f"{nome}: Terminou e liberou tudo")


print("Versão com Deadlock")
thread1 = threading.Thread(target=threadComDeadA, args=("Thread1",))
thread2 = threading.Thread(target=threadComDeadB, args=("Thread2",))

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print("fim")