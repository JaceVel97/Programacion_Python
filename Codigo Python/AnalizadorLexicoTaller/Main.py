from LexicalAnalyzer import LexicalAnalizer
# Entrada de datos

print("Bienvenido a nuestro analizador lexico")
print("A continuacion se le presentan dos opciones para el ingreso de la entrada")
print("1: Ingresar entrada por consola")
print("2: Ingresar direccion de archivo de texto con la entrada")
print("Piense sabiamente su decisión y a continuación ingresala")
option = int(input("Ingrese la opción que desea: \n"))

if option == 1:
    print("------------------Ingreso de entrada por consola-----------------")
    entry = input("Ingrese su entrada:\n")
    lexical = LexicalAnalizer(entry)
    lexical.analyzer()
    lexical.show_Lexemes()
    print("-----------------------------------------------------------------------------------------------")
    lexical.show_errors()

else:
    print("------------------Ingreso de direccion de archivo de texto-----------------")
    entry = input("Ingrese su direccion:\n")