from Node import Node


class List:
    def __init__(self):
        self.first = None
        self.last = None

    def insert_node(self, type_, description_, content_, row_, column_):
        new_lexeme = Node(type_, description_, content_, row_, column_)

        if self.first is None:
            self.last = new_lexeme
            self.first = self.last
        else:
            self.last.set_next(new_lexeme)
            new_lexeme.set_previous(self.last)
            self.last = new_lexeme

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
        while aux is not None:
            counter += 1
            aux = aux.get_next()

        return counter

    def get_type(self, data):
        aux = self.first
        while aux is not None:
            if data == aux.get_content():
                return aux.get_type()
            aux = aux.get_next()

        return "No_type"
