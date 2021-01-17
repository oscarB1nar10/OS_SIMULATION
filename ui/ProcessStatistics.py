import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import ttk


class ProcessStatistics:

    def __init__(self, process):

        # Mock for Process name
        self.process_name = ["Process1", "Process2", "Process3", "Process4", "Process5"]

        # Mock for process size
        self.process_size = [40, 50, 100, 200, 50]

        # Mock for process threads
        self.process_threads = np.zeros(5)

        # Mock for process resources
        # Those process resources should be a type of ENUM
        self.process_resources = ["1", "2", "3", "4", "5"]

        # Mock for process state
        # Those process resources should be a type of ENUM also
        self.process_state = ["ready", "execution", "ready", "block", "ready"]

        self.show_process_stats()

    def show_process_stats(self):

        """
        Those mock are for visualization purpose. As soon as possible we have obtain that info (Processor model)
        from controller layer.
        """

        root = tk.Tk()

        process_df = pd.DataFrame({
            "Process name": self.process_name,
            "process size": self.process_size,
            "process_threads": self.process_threads,
            "process_resources": self.process_resources,
            "process state": self.process_state
        })

        cols = list(process_df.columns)

        tree = ttk.Treeview(root)
        tree.pack()
        tree["columns"] = cols
        for i in cols:
            tree.column(i, anchor='w')
            tree.heading(i, text=i, anchor='w')

        for index, row in process_df.iterrows():
            tree.insert("", 0, text=index, values=list(row))

        root.mainloop()
