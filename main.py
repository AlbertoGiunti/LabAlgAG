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
    A = list(range(n))
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
    A = list(range(n))
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
        # Misura del tempo di ricerca della k-esima statistica d'ordine
        os = timeit.timeit(stmt=lambda: bst.get_kesimo(bst.root, k), number=1)
        etos = etos + os
    # Calcolo dei tempi medi di inserimento e ricerca della k-esima statistica d'ordine
    tmi = eti / rep
    tmos = etos / rep
    return tmi, tmos


# Definiamo una funzione che ci permette di eseguire i test dell'albero rosso nero
def rbt_tests(n, rep):
    rbt = RedBlackTree()
    A = list(range(n))
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
        os = timeit.timeit(stmt=lambda: rbt.os_select(rbt.root, k), number=1)
        etos = etos + os
    # Calcolo dei tempi medi di inserimento e ricerca della k-esima statistica d'ordine
    tmi = eti / rep
    tmos = etos / rep
    return tmi, tmos


# Definiamo una lista di numeri di test
n_values = list(range(1, 30))
rep = 15

# Liste dei risultati dei tempi di inserimento
oll_ins_results = []
bst_ins_results = []
rbt_ins_results = []

# Liste dei risultati dei tempi di ricerca di una k-esima statistica d'ordine casuale
oll_os_results = []
bst_os_results = []
rbt_os_results = []

for n in n_values:
    oll_tins, oll_tos = oll_tests(n, rep)
    oll_ins_results.append(oll_tins)
    oll_os_results.append(oll_tos)
    print(oll_ins_results)
    print(oll_os_results)
    bst_tins, bst_tos = bst_tests(n, rep)
    bst_ins_results.append(bst_tins)
    bst_os_results.append(bst_tos)
    print(bst_ins_results)
    print(bst_os_results)
    rbt_tins, rbt_tos = rbt_tests(n, rep)
    rbt_ins_results.append(rbt_tins)
    rbt_os_results.append(rbt_tos)
    print(rbt_ins_results)
    print(rbt_os_results)

# Stampa i risultati trovati
print("Risultati test inserimento lista ordinata:")

# Rappresentiamo i risultati graficamente
