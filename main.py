import timeit
import random
import matplotlib.pyplot as plt
from tabulate import tabulate

from ordered_linked_list import OrderedLinkedList
from binary_search_tree import BinarySearchTree
from red_black_tree import RedBlackTree

n = 300
step = 100
test_per_iteration = 10

# Creo un metodo per creare array di numeri casuali
max_value = 10000


def random_array(n, max_value):
    return [random.randint(0, max_value) for _ in range(n)]


# Creo le strutture dati
oll = OrderedLinkedList()
bst = BinarySearchTree()
rbt = RedBlackTree()

# Creo le liste in cui salvare i risultati dei test
assex = []
oll_insert_times = []
bst_insert_times = []
rbt_insert_times = []
oll_order_statistic_times = []
bst_order_statistic_times = []
rbt_order_statistic_times = []
oll_rank_times = []
bst_rank_times = []
rbt_rank_times = []


# Creo le funzioni di test
# Funzione di test dell'inserimento
def measure_insert_test(insert_function, arr):
    return timeit.timeit(stmt=lambda: [insert_function(arr[j]) for j in range(len(arr))],
                         number=test_per_iteration) / test_per_iteration * 1000  # tempo in ms


# Funzione di test della ricerca del k-esimo elemento più piccolo
def measure_os_test(os_function, start, length):
    k = length // 2  # Cerco l'elemento più o meno centrale
    return timeit.timeit(stmt=lambda: os_function(start, k),
                         number=test_per_iteration) / test_per_iteration * 1000  # tempo in ms


# Funzione di test della ricerca del rank di un elemento
def measure_rank_test(rank_function, ric):
    return timeit.timeit(stmt=lambda: rank_function(ric),
                         number=test_per_iteration) / test_per_iteration * 1000  # tempo in ms)


# Esecuzione test inserimento
for i in range(1, n, step):
    assex.append(i)  # Lista delle dimensioni degli array
    # Creo un array con i elementi random tra 0 e max_values (= 10000)
    arr = random_array(i, max_value)
    # Svolgo i test sull'inserimento e mi salvo i risultati espressi in ms
    oll_insert_times.append(measure_insert_test(oll.insert, arr))
    bst_insert_times.append(measure_insert_test(bst.insert, arr))
    rbt_insert_times.append(measure_insert_test(rbt.insert, arr))
    # Svolgo i test sulla ricerca del k-esimo elemento più piccolo e mi salvo i risultati espressi in ms
    oll_order_statistic_times.append(measure_os_test(oll.order_statistic, oll.head, i))
    bst_order_statistic_times.append(measure_os_test(bst.get_kesimo, bst.root, i))
    rbt_order_statistic_times.append(measure_os_test(rbt.os_select, rbt.root, i))
    # Genero l'elemento da ricercare
    ricercato = random.choice(arr)
    # Svolgo i test sulla ricerca del rango di un elemento casuale dell'array
    oll_rank_times.append(measure_rank_test(oll.oll_rank, ricercato))
    bst_rank_times.append(measure_rank_test(bst.get_rank, bst.search(bst.root, ricercato)))
    rbt_rank_times.append(measure_rank_test(rbt.os_rank, rbt.search(rbt.root, ricercato)))

# Grafici test inserimento

# Grafico inserimento lista linkata ordinata
plt.plot(assex, oll_insert_times, color='blue', label='Inserimento lista linkata ordinata')
plt.xlabel('Dimensione dell\'array')
plt.ylabel('Tempo di esecuzione (ms)')
plt.title('Tempi inserimento lista ordinata linkata')
plt.legend()
plt.show()

# Grafico inserimento albero binario
plt.plot(assex, bst_insert_times, color='green', label='Inserimento albero binario')
plt.xlabel('Dimensione dell\'array')
plt.ylabel('Tempo di esecuzione (ms)')
plt.title('Tempi inserimento albero binario')
plt.legend()
plt.show()

# Grafico inserimento albero rosso-nero
plt.plot(assex, rbt_insert_times, label='Inserimento albero rosso-nero')
plt.xlabel('Dimensione dell\'array')
plt.ylabel('Tempo di esecuzione (ms)')
plt.title('Tempi inserimento albero rosso-nero')
plt.legend()
plt.show()

# Grafico confronto tra i tre tempi di inserimento
plt.plot(assex, oll_insert_times, color='blue', label='Inserimento lista linkata ordinata')
plt.plot(assex, bst_insert_times, color='green', label='Inserimento albero binario')
plt.plot(assex, rbt_insert_times, color='red', label='Inserimento albero rosso-nero')
plt.xlabel('Dimensione dell\'array')
plt.ylabel('Tempo di esecuzione (ms)')
plt.title('Confronto tempi inserimento')
plt.legend()
plt.show()

# Grafici ricerca del k-esimo elemento più piccolo

# Grafico ricerca del k-esimo elemento più piccolo in una lista linkata ordinata
plt.plot(assex, oll_order_statistic_times, color='blue', label='Ricerca k-esimo lista linkata ordinata')
plt.xlabel('Dimensione dell\'array')
plt.ylabel('Tempo di esecuzione (ms)')
plt.title('Tempi ricerca k-esimo lista linkata ordinata')
plt.legend()
plt.show()

# Grafico ricerca del k-esimo elemento più piccolo in un albero binario
plt.plot(assex, bst_order_statistic_times, color='green', label='Ricerca k-esimo albero binario')
plt.xlabel('Dimensione dell\'array')
plt.ylabel('Tempo di esecuzione (ms)')
plt.title('Tempi ricerca k-esimo albero binario')
plt.legend()
plt.show()

# Grafico ricerca del k-esimo elemento più piccolo in un albero rosso-nero
plt.plot(assex, rbt_order_statistic_times, color='red', label='Ricerca k-esimo albero rosso-nero')
plt.xlabel('Dimensione dell\'array')
plt.ylabel('Tempo di esecuzione (ms)')
plt.title('Tempi ricerca k-esimo albero rosso-nero')
plt.legend()
plt.show()

# Grafico confronto tra le ricerche dei k-esimi elementi più piccoli
plt.plot(assex, oll_order_statistic_times, color='blue', label='Ricerca k-esimo lista linkata ordinata')
plt.plot(assex, bst_order_statistic_times, color='green', label='Ricerca k-esimo albero binario')
plt.plot(assex, rbt_order_statistic_times,color='red', label='Ricerca k-esimo albero rosso-nero')
plt.xlabel('Dimensione dell\'array')
plt.ylabel('Tempo di esecuzione (ms)')
plt.title('Tempi ricerca k-esimo lista linkata ordinata')
plt.legend()
plt.show()

# Grafici ricerca rank di un elemento

# Grafico ricerca rank di un elemento in una lista ordinata
plt.plot(assex, oll_rank_times, color='blue', label='Ricerca rank di un elemento lista linkata ordinata')
plt.xlabel('Dimensione dell\'array')
plt.ylabel('Tempo di esecuzione (ms)')
plt.title('Tempi ricerca rank di un elemento lista linkata ordinata')
plt.legend()
plt.show()

# Grafico ricerca rank di un elemento in un albero binario
plt.plot(assex, bst_rank_times, color='green', label='Ricerca rank di un elemento in un albero binario')
plt.xlabel('Dimensione dell\'array')
plt.ylabel('Tempo di esecuzione (ms)')
plt.title('Tempi ricerca rank di un elemento in un albero binario')
plt.legend()
plt.show()

# Grafico ricerca rank di un elemento in un albero rosso-nero
plt.plot(assex, bst_rank_times, color='red', label='Ricerca rank di un elemento in un albero rosso-nero')
plt.xlabel('Dimensione dell\'array')
plt.ylabel('Tempo di esecuzione (ms)')
plt.title('Tempi ricerca rank di un elemento in un albero rosso-nero')
plt.legend()
plt.show()

# Confronto grafici ricerca rank di un elemento
plt.plot(assex, oll_rank_times, color='blue', label='Ricerca rank di un elemento lista linkata ordinata')
plt.plot(assex, bst_rank_times, color='green', label='Ricerca rank di un elemento in un albero binario')
plt.plot(assex, bst_rank_times, color='red', label='Ricerca rank di un elemento in un albero rosso-nero')
plt.xlabel('Dimensione dell\'array')
plt.ylabel('Tempo di esecuzione (ms)')
plt.title('Tempi ricerca rank di un elemento in un albero rosso-nero')
plt.legend()
plt.show()

# Creazione delle tabelle

# Creazione delle liste dei dati per inserimento, ricerca k-esima statistica d'ordine e rank
data_inserimento = []
data_order_statistic = []
data_rank = []

for assex, oll_insert_times, bst_insert_times, rbt_insert_times, oll_order_statistic_times, bst_order_statistic_times, rbt_order_statistic_times, oll_rank_times, bst_rank_times, rbt_rank_times in zip(assex, oll_insert_times, bst_insert_times, rbt_insert_times, oll_order_statistic_times, bst_order_statistic_times, rbt_order_statistic_times, oll_rank_times, bst_rank_times, rbt_rank_times):
    data_inserimento.append([assex, oll_insert_times, bst_insert_times, rbt_insert_times])
    data_order_statistic.append([assex, oll_order_statistic_times, bst_order_statistic_times, rbt_order_statistic_times])
    data_rank.append([assex, oll_rank_times, bst_rank_times, rbt_rank_times])

# Stampa delle tabelle con il testo centrato e senza indici
# Tabella inserimenti
print("Tempi di inserimento:")
print(tabulate(data_inserimento, headers=['Dimensione dell\'array', 'Lista linkata ordinata', 'Albero binario', 'Albero rosso-nero'], tablefmt='fancy_grid', numalign='center'))

# Tabella statistica d'ordine
print("Tempi di ricerca statistica d'ordine:")
print(tabulate(data_order_statistic, headers=['Dimensione dell\'array', 'Lista linkata ordinata', 'Albero binario', 'Albero rosso-nero'], tablefmt='fancy_grid', numalign='center'))

# Tabella rank
print("Tempi di ricerca del rank:")
print(tabulate(data_rank, headers=['Dimensione dell\'array', 'Lista linkata ordinata', 'Albero binario', 'Albero rosso-nero'], tablefmt='fancy_grid', numalign='center'))
