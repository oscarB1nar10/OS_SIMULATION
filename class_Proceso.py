
class Proceso:

    def __init__(self, proceso):
        self.id = proceso[0]
        self.nombre = proceso[1]
        self.tamaño = proceso[2]
        self.hilos = proceso[3]
        self.recursos = proceso[4]
        self.estado = "listo"

class Recurso:

    def __init__(self, nombre):
        self.estado = "libre"
        self.nombre = nombre