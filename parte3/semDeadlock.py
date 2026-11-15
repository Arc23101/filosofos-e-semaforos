import threading

lockA = threading.Lock()
lockB = threading.Lock()

def threadSemDead(nome):
  print(f"{nome}: Tentando travando A")
  lockA.acquire()
  print(f"{nome}: travou A, agora tentando travando B")

  lockB.acquire()
  print(f"{nome}: Travou B")

  lockB.release()
  lockA.release()
  print(f"{nome}: Terminou e liberou tudo")


print("Versão sem deadlock")
thread1 = threading.Thread(target=threadSemDead, args=("Thread1",))
thread2 = threading.Thread(target=threadSemDead, args=("Thread2",))

thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("fim")
