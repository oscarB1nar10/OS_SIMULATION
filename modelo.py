from class_Proceso import Proceso, Recurso
from random import choice

class Modelo:

    def __init__(self):
        self.Procesos = []
        self.EnProceso = []
        self.Terminado = []
        self.Bloqueado = []
        self.Recursos = {}
        self.CrearRecursos()

    def Add_proceso(self, proceso):
        """
        :param proceso: [1, "uno", 20, 1, ["r1","r2"]],
                        formato [int: id, str: nombre, int: tamaño, int: hilos, Array: recursos]
        :return: nada
        """
        self.Procesos += [Proceso(proceso)]# agregar proceso
        recursos = proceso[4]
        for recurso in recursos:#agrega al recurso que proceso le utliza
            self.Recursos[recurso].proceso += [proceso[1]]

    def CrearRecursos(self):
        for i in range(6): #iniciar recursos
            nombre = "r" + str(i+1)
            self.Recursos[nombre] = Recurso()

    def Corriendo(self):
        """
        :return: un dict
        formato:
        "procesos": todos los procesos en listo, [1, "uno", 20, 1, ["r1","r2"],"listo"],
                    formato: ["id","nombre","tamaño","hilos","recursos","estado"]
        "EnProceso": el proceso en ese instante, [1, "uno", 20, 1, ["r1","r2"],"listo"],
                    formato: ["id","nombre","tamaño","hilos","recursos","estado"]
        "Terminado": Todos los procesos con estado Terminado, [1, "uno", 20, 1, ["r1","r2"],"Terminado"],
                    formato: ["id","nombre","tamaño","hilos","recursos","estado"]
        "Bloqueado": Todos los procesos con estado Bloqueado, [1, "uno", 20, 1, ["r1","r2"],"Bloqueado"],
                    formato: ["id","nombre","tamaño","hilos","recursos","estado"]
        "recursos": Todos los Recursos, ["libre", ["uno","dos"]],
                    formato: ["estado", "procesos que lo utilizan"]
        """
        if self.EnProceso:#si hay un proceso en ejecucion en ese instante
            self.EnProceso_if()#verifica si suelta los procesos y resta a su tamaño

        self.IniciarProceso()#inicia el suguiente proceso, verificanso si sus recursosestan libres

        resultado = {
            "Procesos": self.Procesos,
            "EnProceso": self.EnProceso,
            "Terminado": self.Terminado,
            "Bloqueado" : self.Bloqueado,
            "Recursos" : self.Recursos
            }
        
        return resultado

    def HayProcesos(self):
        """
        :return: yn boolean que define si hay mas procesos que ejecutar
        """
        if len(self.Procesos) != 0 and len(self.Bloqueado) != 0:
            return True
        return False

    def IniciarProceso(self):
        if self.RecursosLibres():
            self.EnProceso = self.Procesos[0]
            self.EnProceso.estado = "Ejecicion"
            self.Procesos.remove(self.Procesos[0])
            self.EstadoOcupado()
        else:
            self.Procesos[0].estado = "Bloqueado"
            self.Bloqueado += [self.Procesos[0]]
            self.Procesos.remove(self.Procesos[0])
            if len(self.Procesos)>0:
                self.IniciarProceso()

    def RecursosLibres(self):
        for recurso in self.Procesos[0].recursos:
            if self.Recursos[recurso].estado == "Ocupado":
                return False
        return True

    def EstadoOcupado(self):
        for recurso in self.EnProceso.recursos:
            self.Recursos[recurso].estado = "Ocupado"

    def EnProceso_if(self):
        if self.ChoiseRecursos():
            self.EnProceso.tamaño -= 10
            if self.EnProceso.tamaño == 0:
                self.EnProceso.estado = "Terminado"
                self.Terminado += [self.EnProceso]
            else:
                self.EnProceso.estado = "Listo"
                self.Procesos += [self.EnProceso]
        else:
            self.EnProceso.estado = "Bloqueado"
            self.Bloqueado += [self.EnProceso]

    def ChoiseRecursos(self):
        TempRecursos = self.Recursos

        for recursos in self.EnProceso.recursos:
            cho = choice([0,2])
            if cho >= 1:
                TempRecursos[recursos].estado = "libre"
            else:
                return False
        self.Recursos = TempRecursos

        return True