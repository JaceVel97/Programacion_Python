from Nodo import Nodo

class Lista:
    def __init__(self):
        self.first = None
        self.last = None

    def insert_node(self, titulo, contenido):
        new_nodo = Nodo(titulo, contenido)

        if self.first == None:
            self.last = new_nodo
            self.first = self.last
        else:
            self.last.set_next(new_nodo)
            new_nodo.set_previous(self.last)
            self.last = new_nodo

    def get_node(self, position):
        aux = self.first
        counter = 0
        while counter < position:
            counter += 1
            aux = aux.get_next()

        return aux

    def get_size(self):
        aux = self.first
        counter = 0
        while aux != None:
            counter += 1
            aux = aux.get_next()

        return counter
