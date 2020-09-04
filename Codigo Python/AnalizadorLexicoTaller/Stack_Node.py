class StackNode:
    def __init__(self, symbol, value):
        self.symbol = symbol
        self.value = value
        self.next = None

    # Get Method
    def get_symbol(self):
        return self.symbol

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    # Set Method
    def set_symbol(self, symbol_):
        self.symbol = symbol_

    def set_value(self, value_):
        self.value = value_

    def set_next(self, next_):
        self.next = next_
