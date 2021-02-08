import pandas as pd
from tkinter import ttk


class ProcessStatistics:

    def __init__(self, process_info, frame):

        self.frame = frame
        self.process_info = process_info
        process_info_filtered = self.get_process_info_filtered()
        self.process_name = process_info_filtered.get("names")
        self.process_size = process_info_filtered.get("weights")
        self.process_threads = process_info_filtered.get("threads")
        # Those process resources should be a type of ENUM
        self.process_resources = process_info_filtered.get("resources")
        # Those process resources should be a type of ENUM also
        self.process_state = process_info_filtered.get("states")

        self.show_process_stats()

    def get_process_info_filtered(self):
        names = []
        weights = []
        threads = []
        resources = []
        states = []
        for process in self.process_info.get('procesos'):
            names.append(process.nombre)
            weights.append(process.tamaño)
            threads.append(process.hilos)
            resources.append(process.recursos)
            states.append(process.estado)

        return {
            "names": names,
            "weights": weights,
            "threads": threads,
            "resources": resources,
            "states": states
        }

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
