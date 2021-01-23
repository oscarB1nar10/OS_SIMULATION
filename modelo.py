from class_Proceso import Proceso, Recurso
from random import choice

class Modelo:

    def __init__(self):
        self.procesos = []
        self.enejecucion = []
        self.terminado = []
        self.recursos = {}
        self.CrearRecursos()

    def CrearRecursos(self):
        for i in range(6):  # iniciar recursos
            nombre = "r" + str(i + 1)
            self.recursos[nombre] = Recurso(nombre)

    def Add_proceso(self, proceso):
        self.procesos += [Proceso(proceso)]  # agregar proceso

    def Corriendo(self):
        if self.enejecucion:
            self.enejecucion.tamaño -= 10
            if self.DesocuparProcesos(self.enejecucion.recursos):
                self.enejecucion.estado = "listo"
            else:
                self.enejecucion.estado = "Bloqueado"

            if self.enejecucion.tamaño == 0:
                self.terminado += [self.enejecucion]
                self.procesos.remove(self.enejecucion)
                self.enejecucion = []

        if self.procesos:

            self.enejecucion = self.procesos[0]
            while True:
                self.OcuparProcesos(self.enejecucion.recursos)
                self.procesos.remove(self.procesos[0])
                if self.enejecucion.estado == "Bloqueado":
                    if self.DesocuparProcesos(self.enejecucion.recursos):
                        self.enejecucion.estado = "listo"
                    else:
                        self.enejecucion.estado = "Bloqueado"
                    self.procesos += [self.enejecucion]
                    self.enejecucion = self.procesos[0]
                else:
                    break

            self.enejecucion.estado = "Ejecicion"
            self.procesos += [self.enejecucion]

        return {
            "procesos": self.procesos,
            "ejecicion": self.enejecucion,
            "recursos": self.recursos,
            "terminados": self.terminado
        }

    def OcuparProcesos(self, recursos):
        for recurso in recursos:
            self.recursos[recurso].estado = "Ocupado"

    def DesocuparProcesos(self, recursos):
        TempRecursos = self.recursos
        for recurso in recursos:
            cho = choice([0, 3])
            if cho >= 1:
                TempRecursos[recurso].estado = "Libre"
                self.recursos = TempRecursos
            else:
                return False
        return True

    def hayprocesos(self):
        if self.procesos:
            return True
        return False