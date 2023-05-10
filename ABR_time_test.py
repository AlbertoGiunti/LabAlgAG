from ABR import BinarySearchTree
import random
import timeit


# Definiamo una funzione che ci permette di eseguire i test dell'albero binario di ricerca
bst = BinarySearchTree()
N = 20
A = list(range(N))
random.shuffle(A)

for i in range(N):
    bst.insert(A[i])

bst.print_tree()
print("kesimo:")
print(bst.get_kesimo(bst.root, 8))
