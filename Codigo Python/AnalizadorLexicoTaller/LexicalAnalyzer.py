from List import List


class LexicalAnalizer:
    def __init__(self, entry):
        self.SymbolList = List()
        self.ErrorList = List()
        self.variables = {}
        self.entry = entry
        self.row = 0
        self.column = -1
        self.state = 0
        self.lexeme = ""
        self.i = 0

    def analyzer(self):
        self.state = 0
        self.i = 0
        while self.i < len(self.entry):
            self.column += 1
            self.switch()
            self.i += 1

    def switch(self):
        if self.state == 0:
            self.state_zero()
        elif self.state == 1:
            self.state_one()
        elif self.state == 2:
            self.state_two()
        else:
            print("Estado invalido")

    def state_zero(self):
        if self.entry[self.i].isalpha():
            self.lexeme += self.entry[self.i]
            self.state = 1
        elif self.entry[self.i].isdigit():
            self.lexeme += self.entry[self.i]
            self.state = 2
        elif self.entry[self.i] == '{':
            self.SymbolList.insert_node("Simbolo", "LlaveA", self.entry[self.i], self.row, self.column)
        elif self.entry[self.i] == '}':
            self.SymbolList.insert_node("Simbolo", "LlaveC", self.entry[self.i], self.row, self.column)
        elif self.entry[self.i] == '(':
            self.SymbolList.insert_node("Simbolo", "ParA", self.entry[self.i], self.row, self.column)
        elif self.entry[self.i] == ')':
            self.SymbolList.insert_node("Simbolo", "ParC", self.entry[self.i], self.row, self.column)
        elif self.entry[self.i] == '+':
            self.SymbolList.insert_node("Simbolo", "Suma", self.entry[self.i], self.row, self.column)
        elif self.entry[self.i] == '-':
            self.SymbolList.insert_node("Simbolo", "Resta", self.entry[self.i], self.row, self.column)
        elif self.entry[self.i] == '*':
            self.SymbolList.insert_node("Simbolo", "Multiplicacion", self.entry[self.i], self.row, self.column)
        elif self.entry[self.i] == '/':
            self.SymbolList.insert_node("Simbolo", "Division", self.entry[self.i], self.row, self.column)
        elif self.entry[self.i] == '%':
            self.SymbolList.insert_node("Simbolo", "Mod", self.entry[self.i], self.row, self.column)
        elif self.entry[self.i] == '=':
            self.SymbolList.insert_node("Simbolo", "Igual", self.entry[self.i], self.row, self.column)
        elif self.entry[self.i] == ';':
            self.SymbolList.insert_node("Simbolo", "PyC", self.entry[self.i], self.row, self.column)
        elif self.entry[self.i] == '\n':
            self.row += 1
            self.column = 0
        elif self.entry[self.i] == '\t':
            self.state = 0
        elif self.entry[self.i] == ' ':
            self.state = 0
        else:
            self.ErrorList.insert_node("Lexico", "El simbolo no pertenece al lenguaje actual", self.entry[self.i], self.row, self.column)

    def state_one(self):

        if self.entry[self.i].isalpha():
            self.lexeme += self.entry[self.i]
        elif self.entry[self.i].isdigit():
            self.lexeme += self.entry[self.i]
        elif self.entry[self.i] == '_':
            self.lexeme += self.entry[self.i]
        else:
            if self.is_reserved(self.lexeme):
                self.SymbolList.insert_node("Reservada", "Palabra reservada", self.lexeme, self.row, (self.column-len(self.lexeme)))
            else:
                self.SymbolList.insert_node("Variable", "Id", self.lexeme, self.row, (self.column-len(self.lexeme)))

            self.state = 0
            self.lexeme = ""
            self.column -= 1
            self.i -= 1

    def state_two(self):
        if self.entry[self.i].isdigit():
            self.lexeme += self.entry[self.i]
            self.state = 2
        elif self.entry[self.i] == ".":
            self.lexeme += self.entry[self.i]
            self.state = 2
        else:
            self.SymbolList.insert_node("Numero", "Valor numerico", self.lexeme, self.row, (self.column-len(self.lexeme)))
            self.state = 0
            self.lexeme = ""
            self.column -= 1
            self.i -= 1

    def is_reserved(self, lexeme):
        if lexeme.lower() == "operaciones":
            return True
        elif lexeme.lower() == "imprimir":
            return True
        return False

    def show_Lexemes(self):
        for l in range(self.SymbolList.get_size()):
            print(f"->Lexema {(l+1)}: Tipo:", self.SymbolList.get_node(l).get_type(), " Contenido:", self.SymbolList.get_node(l).get_content(), " Fila:", self.SymbolList.get_node(l).get_row(), " Columna:", self.SymbolList.get_node(l).get_column())

    def show_errors(self):
        for l in range(self.ErrorList.get_size()):
            print(f"->Error {(l + 1)}: Tipo:", self.ErrorList.get_node(l).get_type(), " Descripcion:",
                  self.ErrorList.get_node(l).get_description(),  " Contenido:",
                  self.ErrorList.get_node(l).get_content(), " Fila:", self.ErrorList.get_node(l).get_row(),
                  " Columna:", self.ErrorList.get_node(l).get_column())