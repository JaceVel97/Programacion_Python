class Nodo:
    def __init__(self, titulo, contenido):
        self.titulo = titulo
        self.contenido = contenido
        self.Next = None
        self.Previous = None

    def get_titulo(self):
        return self.titulo

    def get_contenido(self):
        return self.contenido

    def set_titulo(self, titulo_):
        self.titulo_ = titulo_

    def set_contenido(self, contenido_):
        self.contenido = contenido_

    def get_next(self):
        return self.Next

    def get_previous(self):
        return self.Previous

    def set_next(self, Next):
        self.Next = Next

    def set_previous(self, Previous):
        self.Previous = Previous