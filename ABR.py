class Nodo:
    """
    Classe Nodo per la creazione di un albero binario di ricerca.
    """

    def __init__(self, valore):
        """
        Inizializzazione dell'oggetto Nodo.
        """
        self.valore = valore
        self.sx = None
        self.dx = None
        self.rank = 1


class Albero:
    """
    Classe Albero per la creazione di un albero binario di ricerca.
    """

    def __init__(self):
        """
        Inizializzazione dell'oggetto Albero.
        """
        self.radice = None

    def inserisci(self, valore):
        """
        Inserisce un nodo nell'albero.
        """
        self.radice = self._inserisci(self.radice, valore)

    def _inserisci(self, nodo, valore):
        """
        Funzione privata per l'inserimento di un nodo nell'albero.
        """
        if nodo is None:
            return Nodo(valore)
        elif valore < nodo.valore:
            nodo.sx = self._inserisci(nodo.sx, valore)
        else:
            nodo.dx = self._inserisci(nodo.dx, valore)

        nodo.rank = 1 + (nodo.sx.rank if nodo.sx else 0) + (nodo.dx.rank if nodo.dx else 0)
        return nodo

    def statistica_ordine(self, k):
        """
        Restituisce il k-esimo elemento dell'albero.
        """
        if k < 1 or k > self.radice.rank:
            return None
        return self._statistica_ordine(self.radice, k)

    def _statistica_ordine(self, nodo, k):
        """
        Funzione privata per il calcolo della statistica d'ordine.
        """
        if nodo.sx:
            r = nodo.sx.rank
        else:
            r = 0
        if k == r + 1:
            return nodo.valore
        elif k <= r:
            return self._statistica_ordine(nodo.sx, k)
        else:
            return self._statistica_ordine(nodo.dx, k - r - 1)
