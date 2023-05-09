import timeit
import random
import matplotlib.pyplot as plt
import pandas as pd
from ordered_linked_list import OrderedLinkedList
from ABR import BinarySearchTree
from ARN import RedBlackTree


# Definiamo una funzione che ci permette di eseguire i test della lista ordinata
def oll_run_tests(n):
    # Creiamo una lista di n numeri casuali tra 0 e 1000 da inserire poi nella lista
    random_numbers = [random.randint(0, 1000) for _ in range(n)]

    # Misuriamo il tempo di creazione della lista ordinata
    oll_create_time = timeit.timeit(stmt=lambda: OrderedLinkedList(), number=1000)

    # Inizializziamo la lista ordinata
    lista = OrderedLinkedList()

    # Misuriamo il tempo di inserimento dei dati
    oll_insert_time = timeit.timeit(stmt=lambda: [lista.insert(x) for x in random_numbers], number=1000)

    # Selezioniamo una statistica d'ordine casuale
    k = random.randint(1, n)

    # Misuriamo il tempo di ricerca della statistica d'ordine
    oll_order_statistic_time = timeit.timeit(stmt=lambda: lista.order_statistic(k), number=1000)

    # Restituiamo i tempi di esecuzione
    return oll_create_time, oll_insert_time, oll_order_statistic_time


# Definiamo una funzione che ci permette di eseguire i test dell'albero binario di ricerca
def bst_run_tests(n):
    # Creiamo una lista di n numeri casuali tra 0 e 1000 da inserire poi nell'albero binario
    random_numbers = [random.randint(0, 1000) for _ in range(n)]

    # Misuriamo il tempo di creazione dell'albero binario di ricerca
    bst_create_time = timeit.timeit(stmt=lambda: BinarySearchTree(), number=1000)

    # Inizializziamo l'albero binario di ricerca
    bst = BinarySearchTree()

    # Misuriamo il tempo di inserimento dei dati
    bst_insert_time = timeit.timeit(stmt=lambda: [bst.insert(x) for x in random_numbers], number=1000)

    # Selezioniamo una statistica d'ordine casuale
    k = random.randint(1, n)

    # Misuriamo il tempo di ricerca della statistica d'ordine
    bst_order_statistic_time = timeit.timeit(stmt=lambda: bst.get_ith_smallest(k), number=1000)

    # Restituiamo i tempi di esecuzione
    return bst_create_time, bst_insert_time, bst_order_statistic_time


# Definiamo una funzione che ci permette di eseguire i test dell'albero rosso-nero
def rbt_run_tests(n):
    # Creiamo una lista di n numeri casuali tra 0 e 1000 da inserire poi nell'albero rosso-nero
    random_numbers = [random.randint(0, 1000) for _ in range(n)]

    # Misuriamo il tempo di creazione dell'albero rosso-nero
    rbt_create_time = timeit.timeit(stmt=lambda: RedBlackTree(), number=1000)

    # Inizializziamo l'albero rosso-nero
    rbt = RedBlackTree()

    # Misuriamo il tempo di inserimento dei dati
    rbt_insert_time = timeit.timeit(stmt=lambda: [rbt.insert(x) for x in random_numbers], number=1000)

    # Selezioniamo una statistica d'ordine casuale
    k = random.randint(1, n)

    # Misuriamo il tempo di ricerca della statistica d'ordine
    rbt_order_statistic_time = timeit.timeit(stmt=lambda: rbt.os_select(k), number=1000)

    # Restituiamo i tempi di esecuzione
    return rbt_create_time, rbt_insert_time, rbt_order_statistic_time


# Definiamo una lista di numeri di test
n_values = [10, 100, 500, 1000, 3000]

# Eseguiamo i test per ogni valore di n
oll_results = []
bst_results = []
rbt_results = []
for n in n_values:
    oll_results.append(oll_run_tests(n))
    bst_results.append(bst_run_tests(n))
    rbt_results.append(rbt_run_tests(n))

# Rappresentiamo i risultati graficamente


