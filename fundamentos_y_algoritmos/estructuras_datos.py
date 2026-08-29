# lista enlazada simple

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        # La lista comienza vacía
        self.cabeza = None

    def agregar_al_inicio(self, valor):
        nuevo_nodo = Nodo(valor)

        # El nuevo nodo apunta al antiguo primer nodo
        nuevo_nodo.siguiente = self.cabeza

        # Ahora el nuevo nodo se convierte en la cabeza
        self.cabeza = nuevo_nodo

    def agregar_al_final(self, valor):
        nuevo_nodo = Nodo(valor)

        # Si la lista está vacía, el nuevo nodo será la cabeza
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return

        # Recorremos hasta llegar al último nodo
        actual = self.cabeza

        while actual.siguiente is not None:
            actual = actual.siguiente

        # El último nodo apunta al nuevo nodo
        actual.siguiente = nuevo_nodo

    def eliminar(self, valor):
        # Si la lista está vacía
        if self.cabeza is None:
            return

        # Caso especial: el valor está en el primer nodo
        if self.cabeza.valor == valor:
            self.cabeza = self.cabeza.siguiente
            return

        # Buscamos el nodo anterior al que queremos eliminar
        actual = self.cabeza

        while actual.siguiente is not None:
            if actual.siguiente.valor == valor:
                # Saltamos el nodo que queremos eliminar
                actual.siguiente = actual.siguiente.siguiente
                return

            actual = actual.siguiente

    def buscar(self, valor):
        actual = self.cabeza

        while actual is not None:
            if actual.valor == valor:
                return True

            actual = actual.siguiente

        return False

    def a_lista(self):
        resultado = []
        actual = self.cabeza

        while actual is not None:
            resultado.append(actual.valor)
            actual = actual.siguiente

        return resultado

lista = ListaEnlazada()

lista.agregar_al_inicio(20)
lista.agregar_al_inicio(10)
lista.agregar_al_final(30)
lista.agregar_al_final(40)

print(lista.a_lista())
# [10, 20, 30, 40]

print(lista.buscar(30))
# True

print(lista.buscar(50))
# False

lista.eliminar(20)

print(lista.a_lista())
# [10, 30, 40]