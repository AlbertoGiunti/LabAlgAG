import timeit
import random
import matplotlib.pyplot as plt
import pandas as pd
from ordered_linked_list import OrderedLinkedList


# Definiamo una funzione che ci permette di eseguire i test
def run_tests(n):
    # Creiamo una lista di n numeri casuali
    random_numbers = [random.randint(0, 1000) for _ in range(n)]

    # Misuriamo il tempo di creazione della lista
    create_time = timeit.timeit(stmt=lambda: OrderedLinkedList(), number=1)

    # Inizializziamo la lista ordinata
    lista = OrderedLinkedList()

    # Misuriamo il tempo di inserimento dei dati
    insert_time = timeit.timeit(stmt=lambda: [lista.insert(x) for x in random_numbers], number=1)

    # Selezioniamo una statistica d'ordine casuale
    k = random.randint(1, n)

    # Misuriamo il tempo di ricerca della statistica d'ordine
    order_statistic_time = timeit.timeit(stmt=lambda: lista.order_statistic(k), number=1)

    # Restituiamo i tempi di esecuzione
    return create_time, insert_time, order_statistic_time


# Definiamo una lista di numeri di test
n_values = [10, 50, 100, 500, 1000, 5000]

# Eseguiamo i test per ogni valore di n
results = []
for n in n_values:
    results.append(run_tests(n))

# Rappresentiamo i risultati graficamente
df = pd.DataFrame(results, columns=['Creazione', 'Inserimento', 'Ricerca'], index=n_values)
df.plot(kind='bar')
plt.xlabel('n')
plt.ylabel('Tempo (secondi)')
plt.show()
