import timeit
import random
import matplotlib.pyplot as plt
import pandas as pd
import os

from ordered_linked_list import OrderedLinkedList
from binary_search_tree import BinarySearchTree
from red_black_tree import RedBlackTree

n = 5006
step = 50
test_per_iteration = 30


def random_array(n):
    array = []
    for i in range(0, n):
        array.append(i)
    random.shuffle(array)
    return array


# Creo le funzioni di test
# Funzione di test dell'inserimento di un valore in una struttura dati
def measure_insert_test(insert_function, array):
    times = []
    t = 0
    for j in range(len(array)):
        # Misuro il tempo di esecuzione di una singola iterazione
        times.append(timeit.timeit(stmt=lambda: insert_function(array[j]), number=1))
        t += times[j]
    return (t / len(array)) * 1000  # tempo in ms


# Funzione di test della ricerca del k-esimo elemento più piccolo
def measure_os_test(os_function, start, length):
    k = length // 2  # Cerco l'elemento più o meno centrale
    return timeit.timeit(stmt=lambda: os_function(start, k),
                         number=test_per_iteration) / test_per_iteration * 1000  # tempo in ms


# Funzione di test della ricerca del rank di un elemento
def measure_rank_test(rank_function, ric):
    return timeit.timeit(stmt=lambda: rank_function(ric),
                         number=test_per_iteration) / test_per_iteration * 1000  # tempo in ms)


def test(oll_i, oll_os, oll_r, bst_i, bst_os, bst_r, rbt_i, rbt_os, rbt_r, n, step):
    # Creo le strutture dati
    oll = OrderedLinkedList()
    bst = BinarySearchTree()
    rbt = RedBlackTree()

    # Esecuzione test
    for i in range(5, n, step):
        # Creo un array con i elementi random tra 0 e n
        arr = random_array(i)

        # svolgo i test sull'inserimento e mi salvo i risultati espressi in ms
        oll_i.append(measure_insert_test(oll.insert, arr))
        bst_i.append(measure_insert_test(bst.insert, arr))
        rbt_i.append(measure_insert_test(rbt.insert, arr))

        # Svolgo i test sulla ricerca del k-esimo elemento più piccolo e mi salvo i risultati espressi in ms
        oll_os.append(measure_os_test(oll.order_statistic, oll.head, i))
        bst_os.append(measure_os_test(bst.get_kesimo, bst.root, i))
        rbt_os.append(measure_os_test(rbt.os_select, rbt.root, i))

        # Svolgo i test sulla ricerca del rango di un elemento casuale dell'array
        oll_r.append(measure_rank_test(oll.oll_rank, oll.search(oll.head, i // 2)))
        bst_r.append(measure_rank_test(bst.get_rank, bst.search(bst.root, i // 2)))
        rbt_r.append(measure_rank_test(rbt.os_rank, rbt.search(rbt.root, i // 2)))

        # Svuoto le liste
        oll = OrderedLinkedList()
        bst = BinarySearchTree()
        rbt = RedBlackTree()

    return oll_i, oll_os, oll_r, bst_i, bst_os, bst_r, rbt_i, rbt_os, rbt_r


if __name__ == '__main__':

    # Creo le liste in cui salvare i risultati dei test
    assex = []

    # Serve per i grafici
    for i in range(5, n, step):
        assex.append(i)

    oll_insert_times = [0.0] * len(assex)
    bst_insert_times = [0.0] * len(assex)
    rbt_insert_times = [0.0] * len(assex)
    oll_order_statistic_times = [0.0] * len(assex)
    bst_order_statistic_times = [0.0] * len(assex)
    rbt_order_statistic_times = [0.0] * len(assex)
    oll_rank_times = [0.0] * len(assex)
    bst_rank_times = [0.0] * len(assex)
    rbt_rank_times = [0.0] * len(assex)

    print("Parto con l'esecuzione dei test")

    # Sommo tutti i valori dei vari test
    for j in range(test_per_iteration):
        print("Eseguo il test numero: ", (j+1), "/", test_per_iteration)
        oll_temp_i = []
        bst_temp_i = []
        rbt_temp_i = []
        oll_temp_os = []
        bst_temp_os = []
        rbt_temp_os = []
        oll_temp_r = []
        bst_temp_r = []
        rbt_temp_r = []
        oll_temp_i, oll_temp_os, oll_temp_r, bst_temp_i, bst_temp_os, bst_temp_r, rbt_temp_i, rbt_temp_os, rbt_temp_r = test(
            oll_temp_i, oll_temp_os, oll_temp_r,
            bst_temp_i, bst_temp_os, bst_temp_r,
            rbt_temp_i, rbt_temp_os, rbt_temp_r, n,
            step)

        for k in range(len(oll_temp_i)):
            # Inserimento
            oll_insert_times[k] += oll_temp_i[k]
            bst_insert_times[k] += bst_temp_i[k]
            rbt_insert_times[k] += rbt_temp_i[k]

            # Statistica D'Ordine
            oll_order_statistic_times[k] += oll_temp_os[k]
            bst_order_statistic_times[k] += bst_temp_os[k]
            rbt_order_statistic_times[k] += rbt_temp_os[k]

            # Rango
            oll_rank_times[k] += oll_temp_r[k]
            bst_rank_times[k] += bst_temp_r[k]
            rbt_rank_times[k] += rbt_temp_r[k]

    print("Faccio le medie")

    # Faccio le medie
    for s in range(0, len(assex)):
        # Inserimento
        oll_insert_times[s] = oll_insert_times[s] / test_per_iteration
        bst_insert_times[s] = bst_insert_times[s] / test_per_iteration
        rbt_insert_times[s] = rbt_insert_times[s] / test_per_iteration

        # Statistica d'ordine
        oll_order_statistic_times[s] = oll_order_statistic_times[s] / test_per_iteration
        bst_order_statistic_times[s] = bst_order_statistic_times[s] / test_per_iteration
        rbt_order_statistic_times[s] = rbt_order_statistic_times[s] / test_per_iteration

        # Rango
        oll_rank_times[s] = oll_rank_times[s] / test_per_iteration
        bst_rank_times[s] = bst_rank_times[s] / test_per_iteration
        rbt_rank_times[s] = rbt_rank_times[s] / test_per_iteration


    # Funzione per svuotare una cartella
    def svuota_cartella(cartella):
        file_lista = os.listdir(cartella)
        for file in file_lista:
            file_path = os.path.join(cartella, file)
            os.remove(file_path)


    # Svuota la cartella "tabelle"
    svuota_cartella("tabelle")

    # Svuota la cartella "immagini"
    svuota_cartella("immagini")

    # Grafici test inserimento
    print("Creo i grafici")

    # Grafico inserimento lista linkata ordinata
    plt.clf()
    plt.plot(assex, oll_insert_times, color='blue', label='Inserimento lista linkata ordinata')
    plt.xlabel('Dimensione dell\'array')
    plt.ylabel('Tempo di esecuzione (ms)')
    plt.title('Tempi inserimento lista ordinata linkata')
    plt.legend()
    # Salvo i grafdici nella cartella immagini
    plt.savefig('immagini/oll_ins.png')
    plt.show()

    # Grafico inserimento albero binario
    plt.clf()
    plt.plot(assex, bst_insert_times, color='green', label='Inserimento albero binario')
    plt.xlabel('Dimensione dell\'array')
    plt.ylabel('Tempo di esecuzione (ms)')
    plt.title('Tempi inserimento albero binario')
    plt.legend()
    plt.savefig('immagini/bst_ins.png')
    plt.show()

    # Grafico inserimento albero rosso-nero
    plt.clf()
    plt.plot(assex, rbt_insert_times, color='red', label='Inserimento albero rosso-nero')
    plt.xlabel('Dimensione dell\'array')
    plt.ylabel('Tempo di esecuzione (ms)')
    plt.title('Tempi inserimento albero rosso-nero')
    plt.legend()
    plt.savefig('immagini/rbt_ins.png')
    plt.show()

    # Grafico confronto tra i tre tempi di inserimento
    plt.clf()
    plt.plot(assex, oll_insert_times, color='blue', label='Inserimento lista linkata ordinata')
    plt.plot(assex, bst_insert_times, color='green', label='Inserimento albero binario')
    plt.plot(assex, rbt_insert_times, color='red', label='Inserimento albero rosso-nero')
    plt.xlabel('Dimensione dell\'array')
    plt.ylabel('Tempo di esecuzione (ms)')
    plt.title('Confronto tempi inserimento')
    plt.legend()
    plt.savefig('immagini/conf_ins.png')
    plt.show()

    # Grafici ricerca del k-esimo elemento più piccolo

    # Grafico ricerca del k-esimo elemento più piccolo in una lista linkata ordinata
    plt.clf()
    plt.plot(assex, oll_order_statistic_times, color='blue', label='Ricerca k-esimo lista linkata ordinata')
    plt.xlabel('Dimensione dell\'array')
    plt.ylabel('Tempo di esecuzione (ms)')
    plt.title('Tempi ricerca k-esimo lista linkata ordinata')
    plt.legend()
    plt.savefig('immagini/oll_os.png')
    plt.show()

    # Grafico ricerca del k-esimo elemento più piccolo in un albero binario
    plt.clf()
    plt.plot(assex, bst_order_statistic_times, color='green', label='Ricerca k-esimo albero binario')
    plt.xlabel('Dimensione dell\'array')
    plt.ylabel('Tempo di esecuzione (ms)')
    plt.title('Tempi ricerca k-esimo albero binario')
    plt.legend()
    plt.savefig('immagini/bst_os.png')
    plt.show()

    # Grafico ricerca del k-esimo elemento più piccolo in un albero rosso-nero
    plt.clf()
    plt.plot(assex, rbt_order_statistic_times, color='red', label='Ricerca k-esimo albero rosso-nero')
    plt.xlabel('Dimensione dell\'array')
    plt.ylabel('Tempo di esecuzione (ms)')
    plt.title('Tempi ricerca k-esimo albero rosso-nero')
    plt.legend()
    plt.savefig('immagini/rbt_os.png')
    plt.show()

    # Grafico confronto tra le ricerche dei k-esimi elementi più piccoli
    plt.clf()
    plt.plot(assex, oll_order_statistic_times, color='blue', label='Ricerca k-esimo lista linkata ordinata')
    plt.plot(assex, bst_order_statistic_times, color='green', label='Ricerca k-esimo albero binario')
    plt.plot(assex, rbt_order_statistic_times, color='red', label='Ricerca k-esimo albero rosso-nero')
    plt.xlabel('Dimensione dell\'array')
    plt.ylabel('Tempo di esecuzione (ms)')
    plt.title('Tempi ricerca k-esimo lista linkata ordinata')
    plt.legend()
    plt.savefig('immagini/conf_os.png')
    plt.show()

    # Grafici ricerca rank di un elemento

    # Grafico ricerca rank di un elemento in una lista ordinata
    plt.clf()
    plt.plot(assex, oll_rank_times, color='blue', label='Ricerca rank di un elemento lista linkata ordinata')
    plt.xlabel('Dimensione dell\'array')
    plt.ylabel('Tempo di esecuzione (ms)')
    plt.title('Tempi ricerca rank di un elemento lista linkata ordinata')
    plt.legend()
    plt.savefig('immagini/oll_rank.png')
    plt.show()

    # Grafico ricerca rank di un elemento in un albero binario
    plt.clf()
    plt.plot(assex, bst_rank_times, color='green', label='Ricerca rank di un elemento in un albero binario')
    plt.xlabel('Dimensione dell\'array')
    plt.ylabel('Tempo di esecuzione (ms)')
    plt.title('Tempi ricerca rank di un elemento in un albero binario')
    plt.legend()
    plt.savefig('immagini/bst_rank.png')
    plt.show()

    # Grafico ricerca rank di un elemento in un albero rosso-nero
    plt.clf()
    plt.plot(assex, rbt_rank_times, color='red', label='Ricerca rank di un elemento in un albero rosso-nero')
    plt.xlabel('Dimensione dell\'array')
    plt.ylabel('Tempo di esecuzione (ms)')
    plt.title('Tempi ricerca rank di un elemento in un albero rosso-nero')
    plt.legend()
    plt.savefig('immagini/rbt_rank.png')
    plt.show()

    # Confronto grafici ricerca rank di un elemento
    plt.clf()
    plt.plot(assex, oll_rank_times, color='blue', label='Ricerca rank di un elemento lista linkata ordinata')
    plt.plot(assex, bst_rank_times, color='green', label='Ricerca rank di un elemento in un albero binario')
    plt.plot(assex, rbt_rank_times, color='red', label='Ricerca rank di un elemento in un albero rosso-nero')
    plt.xlabel('Dimensione dell\'array')
    plt.ylabel('Tempo di esecuzione (ms)')
    plt.title('Tempi ricerca rank di un elemento in un albero rosso-nero')
    plt.legend()
    plt.savefig('immagini/conf_rank.png')
    plt.show()

    # Creazione delle tabelle

    # Creazione delle liste dei dati per inserimento, ricerca k-esima statistica d'ordine e rank
    data_inserimento = {'Dimensione dell\'array': assex, 'Lista linkata ordinata': oll_insert_times,
                        'Albero binario': bst_insert_times, 'Albero rosso-nero': rbt_insert_times}
    df_ins = pd.DataFrame(data_inserimento)
    data_order_statistic = {'Dimensione dell\'array': assex, 'Lista linkata ordinata': oll_order_statistic_times,
                            'Albero binario': bst_order_statistic_times,
                            'Albero rosso-nero': rbt_order_statistic_times}
    df_os = pd.DataFrame(data_order_statistic)
    data_rank = {'Dimensione dell\'array': assex, 'Lista linkata ordinata': oll_rank_times,
                 'Albero binario': bst_rank_times, 'Albero rosso-nero': rbt_rank_times}
    df_rank = pd.DataFrame(data_rank)

    # Approssimazione dei tempi di esecuzione
    df_ins = df_ins.round(4)
    df_os = df_os.round(4)
    df_rank = df_rank.round(4)

    plt.clf()

    # Visualizzazione delle tabelle come immagini separate
    plt.figure(figsize=(10, 6))  # Imposta la dimensione dell'immagine

    # Tabella 1: Inserimento
    plt.title("Inserimento")
    plt.axis('off')  # Rimuove gli assi
    table1 = plt.table(cellText=df_ins.values, colLabels=df_ins.columns, loc='center')
    table1.auto_set_font_size(False)
    table1.set_fontsize(10)
    plt.savefig('tabelle/tabella_inserimento.png')  # Salva l'immagine della tabella di inserimento come file PNG
    plt.show()

    # Creazione di una nuova figura per la tabella di ricerca della k-esima statistica d'ordine
    plt.clf()
    plt.figure(figsize=(10, 6))
    plt.title("Ricerca K-esima Statistica d'Ordine")
    plt.axis('off')
    table2 = plt.table(cellText=df_os.values, colLabels=df_os.columns, loc='center')
    table2.auto_set_font_size(False)
    table2.set_fontsize(10)
    plt.savefig('tabelle/tabella_kesima_statistica_ordine.png')
    plt.show()

    # Creazione di una nuova figura per la tabella di ricerca rank
    plt.clf()
    plt.figure(figsize=(10, 6))
    plt.title("Ricerca Rank")
    plt.axis('off')
    table3 = plt.table(cellText=df_rank.values, colLabels=df_rank.columns, loc='center')
    table3.auto_set_font_size(False)
    table3.set_fontsize(10)
    plt.savefig('tabelle/tabella_ricerca_rank.png')
    plt.show()
