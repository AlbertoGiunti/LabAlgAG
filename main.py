import timeit
import random
import matplotlib.pyplot as plt
import pandas as pd
from ordered_linked_list import OrderedLinkedList
from ABR import BinarySearchTree
from ARN import RedBlackTree


# Definiamo una funzione che ci permette di eseguire i test della lista ordinata
def oll_tests(n, rep):
    oll = OrderedLinkedList()
    A = list(n)
    # test inserimento e ricerca k-esima statistica d'ordine
    # eti = elapsed time insert
    eti = 0
    # etos = elapsed time order statistic
    etos = 0
    for _ in range(rep):
        # Randomizza la lista di elementi da inserire ogni iterazione
        random.shuffle(A)
        e = timeit.timeit(stmt=lambda: [oll.insert(A[i]) for i in A], number=1)
        eti = eti + e
        k = random.randint(1, n)
        os = timeit.timeit(stmt=lambda: oll.order_statistic(k), number=1)
        etos = etos + os
    # Calcolo dei tempi medi di inserimento e ricerca della k-esima statistica d'ordine
    tmi = eti / rep
    tmos = etos / rep
    return tmi, tmos


# Definiamo una funzione che ci permette di eseguire i test dell'albero binario di ricerca
def bst_tests(n, rep):
    bst = BinarySearchTree()
    A = list(n)
    # test inserimento e ricerca k-esima statistica d'ordine
    # eti = elapsed time insert
    eti = 0
    # etos = elapsed time order statistic
    etos = 0
    for _ in range(rep):
        # Randomizza la lista di elementi da inserire ogni iterazione
        random.shuffle(A)
        e = timeit.timeit(stmt=lambda: [bst.insert(A[i]) for i in A], number=1)
        eti = eti + e
        k = random.randint(1, n)
        os = timeit.timeit(stmt=lambda: bst.get_kesimo(bst.root(), k), number=1)
        etos = etos + os
    # Calcolo dei tempi medi di inserimento e ricerca della k-esima statistica d'ordine
    tmi = eti / rep
    tmos = etos / rep
    return tmi, tmos


# Definiamo una funzione che ci permette di eseguire i test dell'albero rosso nero
def brt_tests(n, rep):
    rbt = RedBlackTree()
    A = list(n)
    # test inserimento e ricerca k-esima statistica d'ordine
    # eti = elapsed time insert
    eti = 0
    # etos = elapsed time order statistic
    etos = 0
    for _ in range(rep):
        # Randomizza la lista di elementi da inserire ogni iterazione
        random.shuffle(A)
        e = timeit.timeit(stmt=lambda: [rbt.insert(A[i]) for i in A], number=1)
        eti = eti + e
        k = random.randint(1, n)
        os = timeit.timeit(stmt=lambda: rbt.os_select(rbt.root(), k), number=1)
        etos = etos + os
    # Calcolo dei tempi medi di inserimento e ricerca della k-esima statistica d'ordine
    tmi = eti / rep
    tmos = etos / rep
    return tmi, tmos


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
