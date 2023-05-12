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
        # k = random.randint(1, n)
        k = int(n / 2)
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
        # k = random.randint(1, n)
        k = int(n / 2)
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
        # k = random.randint(1, n)
        k = int(n / 2)
        os = timeit.timeit(stmt=lambda: rbt.os_select(rbt.root, k), number=1)
        etos = etos + os
    # Calcolo dei tempi medi di inserimento e ricerca della k-esima statistica d'ordine
    tmi = eti / rep
    tmos = etos / rep
    return tmi, tmos


# Definiamo una lista di numeri di test
n_values = list(range(50, 2000, 50))
rep = 15

# Liste dei risultati dei tempi di inserimento
assex = []
oll_ins_results = []
bst_ins_results = []
rbt_ins_results = []

# Liste dei risultati dei tempi di ricerca di una k-esima statistica d'ordine casuale
oll_os_results = []
bst_os_results = []
rbt_os_results = []

for n in n_values:
    assex.append(n)

    oll_tins, oll_tos = oll_tests(n, rep)
    oll_ins_results.append(oll_tins)
    oll_os_results.append(oll_tos)
    bst_tins, bst_tos = bst_tests(n, rep)
    bst_ins_results.append(bst_tins)
    bst_os_results.append(bst_tos)
    rbt_tins, rbt_tos = rbt_tests(n, rep)
    rbt_ins_results.append(rbt_tins)
    rbt_os_results.append(rbt_tos)

# Stampa i risultati trovati
print("Risultati dei test: ")
print("OLL inserimento: "+str(oll_ins_results))
print("OLL ordere-statistic: "+str(oll_os_results))
print("ABR inserimento: "+str(bst_ins_results))
print("ABR order-statistic: "+str(bst_os_results))
print("ARN inserimento: "+str(rbt_ins_results))
print("ARN order-statistic: "+str(rbt_os_results))

# Rappresentiamo i risultati graficamente

# Grafico funzione di inserimento ordered linked list
plt.plot(assex, oll_ins_results, label="Tempo di inserimento Ordered Linked List")
plt.xlabel("Numero di elementi")
plt.ylabel("Tempo di inserimento")
plt.title("Tempo di inserimento Ordered Linked List")
plt.legend()
plt.show()

# Grafico funzione di inserimento binary search tree
plt.plot(assex, bst_ins_results, label="Tempo di inserimento Binary Search Tree")
plt.xlabel("Numero di elementi")
plt.ylabel("Tempo di inserimento")
plt.title("Tempo di inserimento Binary Search Tree")
plt.legend()
plt.show()

# Grafico funzione di inserimento red black tree
plt.plot(assex, rbt_ins_results, label="Tempo di inserimento Red Black Tree")
plt.xlabel("Numero di elementi")
plt.ylabel("Tempo di inserimento")
plt.title("Tempo di inserimento Red Black Tree")
plt.legend()
plt.show()

# Grafico funzione di ricerca ordered linked list
plt.plot(assex, oll_os_results, label="Tempo di ricerca Ordered Linked List")
plt.xlabel("Numero di elementi")
plt.ylabel("Tempo di ricerca")
plt.title("Tempo di ricerca Ordered Linked List")
plt.legend()
plt.show()

# Grafico funzione di ricerca binary search tree
plt.plot(assex, bst_os_results, label="Tempo di ricerca Binary Search Tree")
plt.xlabel("Numero di elementi")
plt.ylabel("Tempo di ricerca")
plt.title("Tempo di ricerca Binary Search Tree")
plt.legend()
plt.show()

# Grafico funzione di ricerca red black tree
plt.plot(assex, rbt_os_results, label="Tempo di ricerca Red Black Tree")
plt.xlabel("Numero di elementi")
plt.ylabel("Tempo di ricerca")
plt.title("Tempo di ricerca Red Black Tree")
plt.legend()
plt.show()

# Confronto delle funzioni di inserimento
plt.plot(assex, oll_ins_results, label="Tempo di inserimento Ordered Linked List")
plt.plot(assex, bst_ins_results, label="Tempo di inserimento Binary Search Tree")
plt.plot(assex, rbt_ins_results, label="Tempo di inserimento Red Black Tree")
plt.xlabel("Numero di elementi")
plt.ylabel("Tempo di inserimento")
plt.title("Confronto tra i tempi di inserimento")
plt.legend()
plt.show()


# Confronto delle funzioni di ricerca
plt.plot(assex, oll_os_results, label="Tempo di ricerca Ordered Linked List")
plt.plot(assex, bst_os_results, label="Tempo di ricerca Binary Search Tree")
plt.plot(assex, rbt_os_results, label="Tempo di ricerca Red Black Tree")
plt.xlabel("Numero di elementi")
plt.ylabel("Tempo di ricerca")
plt.title("Confronto tra i tempi di ricerca")
plt.legend()
plt.show()
