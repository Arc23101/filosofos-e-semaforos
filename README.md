Grupo: Antony V B
link youtube: https://youtu.be/CQjFQ6-JYtA
linguagem: Python

Parte 1:
filósofos com deadlock:
<img width="508" height="474" alt="image" src="https://github.com/user-attachments/assets/2e7d0842-9586-4c65-adec-ccbb9a9af49a" />
instruções, só dar play, pode demorar mas em algum momento da deadlock.
sem deadlock:
<img width="539" height="439" alt="image" src="https://github.com/user-attachments/assets/59db5bfe-e965-4219-852d-b0f75d5be466" />

instruções, só dar play.

Relatório curto explicando a dinâmica do problema, por que o
impasse surge e qual condição de Coffman será negada na solução proposta.
Pseudocódigo ou fluxograma do protocolo, demonstrando a ordem de aquisição e liberação
de recursos e como justiça/progresso são preservados

Nesse problema existem 5 filósofos e 5 garfos, cada filosofo precisa de dois garfos para comer mas eles compartilham os garfos,
cada filosofo pega um garfo de cada vez e esse é o problema se todos pegarem o garfo da esquerda todos vão espera infinitamente pelo da direto que esta na mão do filosofo ao lado
e como um filosofo só solta um garfo depois de comer isso gera uma espera infinita, isso acontece pois todas as condições de coffman estão presentes, 
Exclusão mútua(o garfo só pode ser usado por um de cada vez),retenção e espera(Cada um pega um garfo e espera pela liberação do outro),sem preempção(somente o proprio filosofo pode soltar o garfo), espera circular(
um ciclo circular eterno é criado pois cada um trava um grafo e espera o próximo filosofo do circulo soltar o dele), na solução desse problema é negada a espera circular pois cada garfo agora tem um numero e o filosofo
tem que pegar o de menor numero primeiro, então por exemplo o filosofo 4 tem que pegar o garfo 3 primeiro e depois o 4, já o filosofo 5 tem que pegar o garfo 0 e depois o 4 isso faz com que o sistema não fique preso
pois então ao menos um filosofo sempre vai ter 2 garfos e depois ele vai liberar eles e o ciclo vai poder continuar sem problemas.
Fluxograma: filósofos são iniciados cada um pega um garfo( sempre o menor dos seus) isso acontece tudo certo até chegar ao ultimo que não vai pegar nenhum pois o seu é 0 mas o 0 já foi pego pelo primeiro filosofo,
o ciclo continua para os outros mas nenhum deles pode pegar seu segundo garfo menos o filosofo 4 pois o filosofo 5 não pegou o garfo 4 pois ele é o seu maior garfo, então o filosofo 4 pega o segundo garfo, come e 
libera os seus garfos, começa a  pensar e então filosofo 3 pega seu segundo garfo que é o 3 que acabou de ser liberado e assim segue o ciclo infinitamente.
o progresso é preservado pois não são gerados deadlocks, e a justiça é preservada pois nenhum filosofo fica eternamente sem comer pois depois de comer os filósofos ficam pensando por um tempo e esse é o tempo
necessário para outro filosofo pegar o garfo para ou começar a comer ou pegar o seu garfo de menor numero e espera a sua vez pelo segundo garfo.

Parte 2:
semaforo com perdas:
<img width="901" height="90" alt="image" src="https://github.com/user-attachments/assets/76a3d6b7-4692-49dd-815e-7b8c87b7a3e4" />
instruções, só dar play, devido aos números serem baixos não acontece perda de dados e o maior numero que meu pc aguenta ainda é pequeno então para ver perda de dados é só aumentar as variáveis iniciais .
sem perdas:
<img width="896" height="100" alt="image" src="https://github.com/user-attachments/assets/dfc77e69-b552-4090-b1f4-f24c21165ac8" />

instruções, só dar play.


Tabela de resultados no README com pelo menos 3 execuções de cada versão: valor
esperado, valor obtido, tempo de execução.
Discussão escrita sobre: por que a versão sem sincronização perde incrementos, por que a
versão com semáforo é correta, o trade-off de throughput e o conceito de
visibilidade/ordenação (happens-before em Java; barreiras implícitas em Python).

PS C:\Users\Antony\Documents\BCC\semestre3\Sistema\TDE2> & 'C:\Users\Antony\AppData\Local\Python\pythoncore-3.14-64\python.exe' 'c:/Users/Antony/Documents/BCC/semestre3/Sistema/TDE2/semaforo.py'
Esperado: 1600000
(Com sincronia) Obtido: 1600000 Tempo: 1.189s
PS C:\Users\Antony\Documents\BCC\semestre3\Sistema\TDE2> & 'C:\Users\Antony\AppData\Local\Python\pythoncore-3.14-64\python.exe' 'c:/Users/Antony/Documents/BCC/semestre3/Sistema/TDE2/semaforo.py'
Esperado: 1600000
(Com sincronia) Obtido: 1600000 Tempo: 1.174s
PS C:\Users\Antony\Documents\BCC\semestre3\Sistema\TDE2> C:\Users\Antony\AppData\Local\Python\pythoncore-3.14-64\python.exe c:/Users/Antony/Documents/BCC/semestre3/Sistema/TDE2/semaforo.py
Esperado: 1600000
(Com sincronia) Obtido: 1600000 Tempo: 1.148s
PS C:\Users\Antony\Documents\BCC\semestre3\Sistema\TDE2> 

PS C:\Users\Antony\Documents\BCC\semestre3\Sistema\TDE2> & 'C:\Users\Antony\AppData\Local\Python\pythoncore-3.14-64\python.exe' 'c:/Users/Antony/Documents/BCC/semestre3/Sistema/TDE2/semaforoSemSicronizacao.py'
Esperado: 1600000
(Sem sincronização) Obtido: 1600000 Tempo: 0.061s
PS C:\Users\Antony\Documents\BCC\semestre3\Sistema\TDE2> & 'C:\Users\Antony\AppData\Local\Python\pythoncore-3.14-64\python.exe' 'c:/Users/Antony/Documents/BCC/semestre3/Sistema/TDE2/semaforoSemSicronizacao.py'
Esperado: 1600000
(Sem sincronização) Obtido: 1600000 Tempo: 0.067s
PS C:\Users\Antony\Documents\BCC\semestre3\Sistema\TDE2> & 'C:\Users\Antony\AppData\Local\Python\pythoncore-3.14-64\python.exe' 'c:/Users/Antony/Documents/BCC/semestre3/Sistema/TDE2/semaforoSemSicronizacao.py'
Esperado: 1600000
(Sem sincronização) Obtido: 1600000 Tempo: 0.068s
PS C:\Users\Antony\Documents\BCC\semestre3\Sistema\TDE2> 

Na teoria era para acontecer perda de dados na segunda tabela sim, mas por serem números pequenos isso não acontece pois as threads acabam muito rápido e não da tempo de dar conflito entre elas, tentei aumentar 
os números mas quando começa a ter perda de dados os números já são tão grandes que meu pc só trava.
A perda de incrementos acontece pois o funcionamento da thread acontece assim, ela lê a variável = 0, salva internamente , muda a variável interna para mais 1, e depois modifica a principal com o seu valor interno
mas nesse meio tempo outra thread tambem leu o valor e guardou como 0 tambem, ela tambem adiciona 1 e quando vai modificar a principal , a principal já é 1 mas por ter salvo seu valor antes dela ser modificada pela
primeira ela achava que era 0 e agora salva a principal como 1 tambem. A com o semáforo é a correta pois ela trava a a escrita e leitura dessa variável até a sua thread completar seu proceso, que no caso é ler,salvar
internamente, modificar e salvar na principal para ai liberar para outra ler a variavel, isso garante que não vai ter perda de dados. O trade-off de throughput, é a consequência de um processo mais seguro, com o semáforo
é garantido que nada vai se perder mas tambem aumenta muito o tempo pois agora todas as threads que usam essa variável tem que espera sua vez para ver e mexer nela, maior segurança, menor velocidade de procesamento.
Pelo que pesquisei, em Java o jeito que a linguagem foi construída tem algum tipo de mecanismo que permite que as mudanças feitas durante um lock sejam visíveis por outras threads que usam o comando acquire nessa variavel
dai isso garante que as threads estejam com os mesmo dados, já no python a biblioteca threading tem algum mecanismo que força as memorias locais de cada theread a sincronizarem com a memoria principal do programa,
e assim nenhuma thread tem os dados errados.

Parte 3:
Logs ou prints anexados ao README evidenciando o travamento (programa que não
termina e/ou diagnóstico do tipo jstack/threading enumerate apontando as threads
bloqueadas).
<img width="1437" height="240" alt="image" src="https://github.com/user-attachments/assets/a639db67-24af-4021-9060-dd8f06922fd8" />
sistema em deadlock
instruções, só dar play.

<img width="1391" height="200" alt="image" src="https://github.com/user-attachments/assets/01d742c0-a0c4-421c-821b-b0e9cc420bce" />
Sistema sem deadlock
instruções, só dar play.


