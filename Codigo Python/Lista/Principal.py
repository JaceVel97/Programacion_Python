from Lista import Lista

ListaEjemplo = Lista()

ListaEjemplo.insert_node("Prueba1", 12)
ListaEjemplo.insert_node("Prueba2", "Valor2")
ListaEjemplo.insert_node("Prueba3", 12)

print(ListaEjemplo.get_size())
print(ListaEjemplo.get_node(0).get_contenido())