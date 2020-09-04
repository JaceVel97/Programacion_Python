from LexicalAnalyzer import LexicalAnalizer
from Stack import Stack

# Entrada de datos

print("Bienvenido a nuestro analizador lexico")
print("A continuacion se le presentan dos opciones para el ingreso de la entrada")
print("1: Ingresar entrada por consola")
print("2: Ingresar direccion de archivo de texto con la entrada")
print("3: Salir")
print("Piense sabiamente su decisión y a continuación ingresala")
option = input("Ingrese la opción que desea: \n")
while not option.isdigit():
    print("No penso sabiamente, pues ingreso una entrada nula")
    option = input("Ingrese de nuevo la opción que desea: \n")
value = int(option)
while not value == 3:
    if value == 1:
        print("------------------Ingreso de entrada por consola-----------------")
        entry = input("Ingrese su entrada:\n")
        lexical = LexicalAnalizer(entry)
        lexical.analyzer()
        lexical.show_lexemes()
        print("-----------------------------------------------------------------------------------------------")
        lexical.show_errors()

    elif value == 2:
        print("------------------Ingreso de direccion de archivo de texto-----------------")
        path = input("Ingrese su direccion:\n")
        entry = ""
        try:
            file = open(path, 'rt')
            entry = file.read()

        except AttributeError:
            print("The path is incorrect")
        except ValueError:
            print("The path is incorrect")
        lexical = LexicalAnalizer(entry)
        lexical.analyzer()
        # lexical.show_lexemes()
        print("-----------------------------------------------------------------------------------------------")
        lexical.show_errors()
    else:
        print("No penso sabiamente, pues ingreso una entrada nula")

    print("Bienvenido a nuestro analizador lexico")
    print("A continuacion se le presentan dos opciones para el ingreso de la entrada")
    print("1: Ingresar entrada por consola")
    print("2: Ingresar direccion de archivo de texto con la entrada")
    print("Piense sabiamente su decisión y a continuación ingresala")
    print("3: Salir")
    value = int(input("Ingrese la opción que desea: \n"))