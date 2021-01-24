import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import ttk


class ProcessStatistics:

    def __init__(self, process_info, frame):

        self.frame = frame
        self.process_info = process_info
        self.process_name = self.get_process_name()
        self.process_size = self.get_process_weight()
        self.process_threads = self.get_process_threads()
        # Those process resources should be a type of ENUM
        self.process_resources = self.get_process_resources()
        # Those process resources should be a type of ENUM also
        self.process_state = self.get_process_state()

        self.show_process_stats()

    def get_process_name(self):
        names = []
        for process in self.process_info.get('procesos'):
            names.append(process.nombre)

        return names

    def get_process_weight(self):
        weights = []
        for process in self.process_info.get('procesos'):
            weights.append(process.tamaño)

        return weights

    def get_process_threads(self):
        threads = []
        for process in self.process_info.get('procesos'):
            threads.append(process.hilos)

        return threads

    def get_process_resources(self):
        resources = []
        for process in self.process_info.get('procesos'):
            resources.append(process.recursos)

        return resources

    def get_process_state(self):
        states = []
        for process in self.process_info.get('procesos'):
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

        tree = ttk.Treeview(self.frame)
        tree.pack()
        tree["columns"] = cols
        for i in cols:
            tree.column(i, anchor='w')
            tree.heading(i, text=i, anchor='w')

        for index, row in process_df.iterrows():
            tree.insert("", 0, text=index, values=list(row))

    def destroy_stat_view(self):
        self.frame.destroy()

    def update_view(self):
        self.frame.update()
