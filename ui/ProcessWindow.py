from tkinter import *

from class_Proceso import Proceso
from modelo import Modelo
from ui.ProcessStatistics import ProcessStatistics
from random import randint
import pandas as pd
from tkinter import ttk
import tkinter as tk
import time
import threading



class ProcessWindow:

    def __init__(self, win):
        self.process_state = []
        self.process_resources = []
        self.process_threads = []
        self.process_size = []
        self.process_name = []

        self.process_to_execute = []
        self.model = Modelo()

        self.lb_process_id = Label(win, text="Process id")
        self.lb_process_name = Label(win, text="Name")
        self.lb_process_weight = Label(win, text="Weight")
        self.lb_process_threads = Label(win, text="Number of threads")
        self.lb_process_resources = Label(win, text="Resources")

        self.input_process_id = Entry()
        self.input_process_name = Entry()
        self.input_process_weight = Entry()
        self.input_process_threads = Entry()

        clicked = StringVar()
        clicked.set("Resource1")
        self.resources_menu = OptionMenu(win, clicked, "Resource1", "Resource2", "Resource3", "Resource4", "Resource5")
        self.resources_menu.pack()

        self.lb_process_id.place(x=100, y=50)
        self.input_process_id.place(x=200, y=50)
        self.lb_process_name.place(x=100, y=100)
        self.input_process_name.place(x=200, y=100)
        self.lb_process_weight.place(x=100, y=150)
        self.input_process_weight.place(x=200, y=150)
        self.lb_process_threads.place(x=100, y=200)
        self.input_process_threads.place(x=200, y=200)
        self.lb_process_resources.place(x=100, y=250)
        self.resources_menu.place(x=200, y=250)

        # Frame for created process
        self.process_frame = LabelFrame(win, text="Created process", padx=10, pady=10)
        self.process_frame.pack(padx=10, pady=10)
        self.process_frame.place(x=350, y=50)

        self.btn_create_process = Button(win, text='Accept', command=self.create, width=5, height=1)
        self.btn_new_process = Button(win, text='New', command=self.new)
        self.btn_execute_process = Button(win, text='Execute', command=self.execute)
        self.btn_process_stats = Button(win, text='Process stats', command=self.stats)
        self.btn_create_process.place(x=0, y=280)
        self.btn_new_process.place(x=60, y=280)
        self.btn_execute_process.place(x=120, y=280)
        self.btn_process_stats.place(x=180, y=280)

    def create(self):
        process_id = int(self.input_process_id.get())
        process_name = str(self.input_process_name.get())
        process_weight = int(self.input_process_weight.get())
        process_threads = int(self.input_process_threads.get())

        resources = self.select_process()
        process_detail = [
            process_id,
            process_name,
            process_weight,
            process_threads,
            resources]

        process = Proceso(process_detail)

        # This process is added to stack in [Model]
        self.model.Add_proceso(process_detail)

        self.process_to_execute.append(process)

        self.add_process_to_table(process_name=process_name)

        # For each process append 2 resources
    def select_process(self):
        resources = [self.model.resources[randint(0, 8)], self.model.resources[randint(0, 8)]]
        while resources[0] == resources[1]:
            resources.append(self.model.resources[randint(0, 8)])

        return resources

    def add_process_to_table(self, process_name):
        process_label = Label(self.process_frame, text=process_name)
        process_label.pack()

    # Clear all fields
    def new(self):
        self.input_process_id.delete(0, 'end')
        self.input_process_name.delete(0, 'end')
        self.input_process_weight.delete(0, 'end')
        self.input_process_threads.delete(0, 'end')

    def execute(self):
        # The [Proceso] shall be able to receive a list of process
        # process = Proceso(self.process_to_execute)
        self.clean_process_frame()

        while self.model.hayprocesos():
            process_result = self.model.Corriendo()
            self.map_process_info(process_result)
            self.update_view()
            #process_stats = ProcessStatistics(process_result)
            #process_stats.show_process_stats().destroy_stat_view()
            ##threading.Thread(show_process_stats(process_result)).start()
            #
            #process_stats.destroy_stat_view()

    def clean_process_frame(self):
        for widget in self.process_frame.winfo_children():
            widget.destroy()

        self.new()

    def stats(self):
        # Call [ProcessStatistics] and pass the process information, we have to get this
        # information from model [Process]
        ProcessStatistics(self.process_to_execute)

    ########################

    def map_process_info(self, process_info):
        self.process_name = self.get_process_name(process_info)
        self.process_size = self.get_process_weight(process_info)
        self.process_threads = self.get_process_threads(process_info)
        # Those process resources should be a type of ENUM
        self.process_resources = self.get_process_resources(process_info)
        # Those process resources should be a type of ENUM also
        self.process_state = self.get_process_state(process_info)

        self.show_process_stats()

    def get_process_name(self, process_info):
        names = []
        for process in process_info.get('procesos'):
            names.append(process.nombre)

        return names

    def get_process_weight(self, process_info):
        weights = []
        for process in process_info.get('procesos'):
            weights.append(process.tamaño)

        return weights

    def get_process_threads(self, process_info):
        threads = []
        for process in process_info.get('procesos'):
            threads.append(process.hilos)

        return threads

    def get_process_resources(self, process_info):
        resources = []
        for process in process_info.get('procesos'):
            resources.append(process.recursos)

        return resources

    def get_process_state(self, process_info):
        states = []
        for process in process_info.get('procesos'):
            states.append(process.estado)

        return states

    def show_process_stats(self):

        """
        Those mock are for visualization purpose. As soon as possible we have obtain that info (Processor model)
        from controller layer.
        """

        process_df = pd.DataFrame({
            "Process name": self.process_name,
            "process size": self.process_size,
            "process_threads": self.process_threads,
            "process_resources": self.process_resources,
            "process state": self.process_state
        })

        cols = list(process_df.columns)

        tree = ttk.Treeview(second_frame)
        tree.pack()
        tree["columns"] = cols
        for i in cols:
            tree.column(i, anchor='w')
            tree.heading(i, text=i, anchor='w')

        for index, row in process_df.iterrows():
            tree.insert("", 0, text=index, values=list(row))

    def destroy_stat_view(self):
        window.destroy()

    def update_view(self):
        window.update()


window = Tk()
main_frame = Frame(window)
main_frame.pack(fill=BOTH, expand=1)

# Create a canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add a scrollbar to the canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# Configure the canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

# Create another frame  inside canvas
second_frame = Frame(my_canvas)

# Add that new frame to a window in the canvas
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
my_win = ProcessWindow(main_frame)
window.title('Hello Python')
window.geometry('500x300+10+10')
window.mainloop()
