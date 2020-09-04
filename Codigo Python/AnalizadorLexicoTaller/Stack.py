from Stack_Node import StackNode


class Stack:
    def __init__(self):
        self.first = None

    def push(self, symbol, value):
        stack_node = StackNode(symbol, value)

        if self.first is None:
            self.first = stack_node
        else:
            stack_node.set_next(self.first)
            self.first = stack_node

    def pop(self):
        aux = self.first
        if self.first is None:
            print("Error, Stack doesn't have values")
        else:
            if self.first.get_symbol() is None:
                self.first = None
                return aux.get_symbol()
            else:
                self.first = aux.get_next()
                return aux.get_symbol()

    def peek(self):
        return self.first

    def show_values(self):
        aux = self.first
        while not aux is None:
            print(aux.get_symbol())
            aux = aux.get_next()

    def get_size(self):
        aux = self.first
        counter = 0
        while aux is not None:
            counter += 1
            aux = aux.get_next()

        return counter
