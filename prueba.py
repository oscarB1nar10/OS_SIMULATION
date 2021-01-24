from model.modelo import Modelo

Model = Modelo()

procesos = [
    [1, "uno", 20, 1, ["r1"]],
    [2, "dos", 30, 1, ["r1","r3"]],
    [2, "tres", 50, 1, ["r1","r2"]]
]


for proceso in procesos:
    Model.Add_proceso(proceso)

while True:
    todo = Model.Corriendo()

    if todo['ejecicion']:
        print("\n\n" + todo['ejecicion'].nombre + "  " + todo['ejecicion'].estado + "  " + str(todo['ejecicion'].tamaño))


    print("\nrecursos")
    for recurso in todo['recursos']:
        if todo['recursos'][recurso].estado == "Ocupado":
            print(todo['recursos'][recurso].nombre + "  " + todo['recursos'][recurso].estado)

    print("\nprocesos")
    for proceso in todo['procesos']:
        print(proceso.nombre + "  " + str(proceso.tamaño) + "  " + proceso.estado)

    if len(todo['terminados']) != []:
        print("\nterminados")
        for terminado in todo['terminados']:
            print(terminado.nombre + "  " + str(terminado.tamaño) + "  " + terminado.estado)

    if not Model.hayprocesos():
        break

    """print(todo['EnProceso'].nombre + "  " + todo['EnProceso'].estado + "  " + str(todo['EnProceso'].tamaño))
    for proceso in todo['Procesos']:
       print(proceso.nombre + "  " + str(proceso.tamaño) + "  " + proceso.estado)"""
