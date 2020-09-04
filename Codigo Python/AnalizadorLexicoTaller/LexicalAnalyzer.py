from List import List
from Stack import Stack


class LexicalAnalizer:
    def __init__(self, entry):
        self.SymbolList = List()
        self.ErrorList = List()
        self.expression = []
        self.print_list = []
        self.variables = {}
        self.entry = entry
        self.row = 0
        self.column = -1
        self.state = 0
        self.lexeme = ""
        self.operation = ""
        self.i = 0
        self.verification = False
        self.verification_print = False

    def analyzer(self):
        self.state = 0
        self.i = 0
        while self.i < len(self.entry):
            self.column += 1
            self.switch()
            self.i += 1
        if self.ErrorList.get_size() == 0:
            self.resolve_operations()
            self.print_method()
        else:
            print("No se pueden mostrar los resultados ya que se encontraron errores en la entrada del archivo")

    def switch(self):
        if self.state == 0:
            self.state_zero()
        elif self.state == 1:
            self.state_one()
        elif self.state == 2:
            self.state_two()
        elif self.state == 3:
            self.state_three()
        elif self.state == 4:
            self.state_four()
        else:
            print("Estado invalido")

    def state_zero(self):
        if self.entry[self.i].isalpha():
            self.lexeme += self.entry[self.i]
            self.state = 1
        elif self.entry[self.i].isdigit():
            self.lexeme += self.entry[self.i]
            self.state = 2
        elif self.entry[self.i] == '$':
            self.state = 3
        elif self.entry[self.i] == '<':
            self.state = 4
        elif self.entry[self.i] == '^':
            self.operation += "," + self.entry[self.i]
            self.SymbolList.insert_node("Simbolo", "Potencia", self.entry[self.i], self.row, self.column)
        elif self.entry[self.i] == '{':
            self.SymbolList.insert_node("Simbolo", "LlaveA", self.entry[self.i], self.row, self.column)
        elif self.entry[self.i] == '}':
            self.SymbolList.insert_node("Simbolo", "LlaveC", self.entry[self.i], self.row, self.column)
        elif self.entry[self.i] == '(':
            self.operation += "," + self.entry[self.i]
            self.SymbolList.insert_node("Simbolo", "ParA", self.entry[self.i], self.row, self.column)
        elif self.entry[self.i] == ')':
            self.operation += "," + self.entry[self.i]
            self.SymbolList.insert_node("Simbolo", "ParC", self.entry[self.i], self.row, self.column)
        elif self.entry[self.i] == '+':
            self.operation += "," + self.entry[self.i]
            self.SymbolList.insert_node("Simbolo", "Suma", self.entry[self.i], self.row, self.column)
        elif self.entry[self.i] == '-':
            self.operation += "," + self.entry[self.i]
            self.SymbolList.insert_node("Simbolo", "Resta", self.entry[self.i], self.row, self.column)
        elif self.entry[self.i] == '*':
            self.operation += "," + self.entry[self.i]
            self.SymbolList.insert_node("Simbolo", "Multiplicacion", self.entry[self.i], self.row, self.column)
        elif self.entry[self.i] == '/':
            self.operation += "," + self.entry[self.i]
            self.SymbolList.insert_node("Simbolo", "Division", self.entry[self.i], self.row, self.column)
        elif self.entry[self.i] == '%':
            self.operation += "," + self.entry[self.i]
            self.SymbolList.insert_node("Simbolo", "Mod", self.entry[self.i], self.row, self.column)
        elif self.entry[self.i] == '=':
            self.verification = True
            self.SymbolList.insert_node("Simbolo", "Igual", self.entry[self.i], self.row, self.column)
        elif self.entry[self.i] == ';':
            self.verification_print = False
            if self.verification:
                self.expression.append(self.operation)
            self.operation = ""
            self.SymbolList.insert_node("Simbolo", "PyC", self.entry[self.i], self.row, self.column)
        elif self.entry[self.i] == '\n':
            self.row += 1
            self.column = -1
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
                self.operation = self.lexeme
                if self.verification_print:
                    self.print_list.append(self.lexeme)

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
            self.operation += "," + self.lexeme
            self.state = 0
            self.lexeme = ""
            self.column -= 1
            self.i -= 1

    def state_three(self):
        if self.entry[self.i] == "\n":
            self.state = 0
            self.row += 1
            self.column = -1

    def state_four(self):
        if self.entry[self.i] == ">":
            self.state = 0
        elif self.entry[self.i] == "\n":
            self.row += 1
            self.column = -1

    def is_reserved(self, lexeme):
        if lexeme.lower() == "operaciones":
            return True
        elif lexeme.lower() == "imprimir":
            self.verification = False
            self.verification_print = True
            return True
        return False

    def show_lexemes(self):
        for l in range(self.SymbolList.get_size()):
            print(f"->Lexema {(l+1)}: Tipo:", self.SymbolList.get_node(l).get_type(), " Contenido:", self.SymbolList.get_node(l).get_content(), " Fila:", self.SymbolList.get_node(l).get_row(), " Columna:", self.SymbolList.get_node(l).get_column())

    def show_errors(self):
        for l in range(self.ErrorList.get_size()):
            print(f"->Error {(l + 1)}: Tipo:", self.ErrorList.get_node(l).get_type(), " Descripcion:",
                  self.ErrorList.get_node(l).get_description(),  " Contenido:",
                  self.ErrorList.get_node(l).get_content(), " Fila:", self.ErrorList.get_node(l).get_row(),
                  " Columna:", self.ErrorList.get_node(l).get_column())

    def resolve_operations(self):
        post_list = []
        symbol_stack = Stack()
        result = 0
        variable = ""
        if self.ErrorList.get_size() > 0:
            print("No se pueden mostrar los resultados ya que se encontraron errores en la entrada del archivo")
        else:
            for a in range(len(self.expression)):
                for value in self.expression[a].split(","):
                    if self.SymbolList.get_type(value) == "Variable":
                        variable = value
                    elif self.SymbolList.get_type(value) == "Numero":
                        post_list.append(value)
                    else:
                        if symbol_stack.get_size() == 0:
                            symbol_stack.push(value, self.get_value(value))
                        else:
                            if self.get_value(value) == 3:
                                symbol_stack.push(value, self.get_value(value))
                            elif self.get_value(value) == 4:
                                while not symbol_stack.peek().get_value() == 3:
                                    if symbol_stack.get_size() > 0:
                                        post_list.append(symbol_stack.pop())
                                    else:
                                        break
                                symbol_stack.pop()
                            elif self.get_value(value) == symbol_stack.peek().get_value():
                                post_list.append(symbol_stack.pop())
                                symbol_stack.push(value, self.get_value(value))
                            elif self.get_value(value) > symbol_stack.peek().get_value():
                                symbol_stack.push(value, self.get_value(value))
                            elif self.get_value(value) < symbol_stack.peek().get_value():
                                while not symbol_stack.peek() is None:
                                    if not symbol_stack.peek().get_value() == 3:
                                        post_list.append(symbol_stack.pop())
                                    else:
                                        break
                                symbol_stack.push(value, self.get_value(value))
                # Final iteracion primer for
                while symbol_stack.get_size() > 0:
                    post_list.append(symbol_stack.pop())
                result = self.operate_expression(post_list)
                self.variables[variable] = result
                post_list = []

    def get_value(self, symbol):
        if symbol == "+" or symbol == "-":
            return 0
        elif symbol == "*" or symbol == "/" or symbol == "%":
            return 1
        elif symbol == "(":
            return 3
        elif symbol == ")":
            return 4
        elif symbol == "^":
            return 5

    def operate_expression(self, expression_list):
        stack_operation = Stack()
        result = 0
        for data in expression_list:
            if self.SymbolList.get_type(data) == "Numero":
                stack_operation.push(data, -1)
            else:
                try:
                    if stack_operation.get_size() >= 2:
                        if data == "+":
                            result = float(stack_operation.pop()) + float(stack_operation.pop())
                            stack_operation.push(result, -1)
                        elif data == "-":
                            number2 = float(stack_operation.pop())
                            number1 = float(stack_operation.pop())
                            result = number1 - number2
                            stack_operation.push(result, -1)
                        elif data == "*":
                            result = float(stack_operation.pop()) * float(stack_operation.pop())
                            stack_operation.push(result, -1)
                        elif data == "/":
                            number2 = float(stack_operation.pop())
                            number1 = float(stack_operation.pop())
                            if not number2 == 0:
                                result = number1 / number2
                            else:
                                print("No es posible dividir entre cero")
                                stack_operation.push(0, -1)
                                break
                            stack_operation.push(result, -1)
                        elif data == "%":
                            number2 = float(stack_operation.pop())
                            number1 = float(stack_operation.pop())
                            if not number2 == 0:
                                result = number1 % number2
                            else:
                                print("No es posible dividir entre cero")
                                stack_operation.push(0, -1)
                                break
                            stack_operation.push(result, -1)
                        elif data == "^":
                            number2 = float(stack_operation.pop())
                            number1 = float(stack_operation.pop())

                            result = pow(number1, number2)
                            stack_operation.push(result, -1)
                    else:
                        print("Insuficiencia de valores en la pila")
                except ValueError:
                    print("Error de conversion")

        return float(stack_operation.pop())

    def print_method(self):
        try:
            for id in self.print_list:
                print(f"Impresion: '{self.variables[id]}'")
        except KeyError:
            print("A key is missing")