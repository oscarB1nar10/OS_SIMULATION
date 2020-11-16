import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import ttk

"""
Those mock are for visualization purpose. As soon as possible we have obtain that info (Processor model)
from controller layer.
"""

# Mock for Process name
process_name = ["Process1", "Process2", "Process3", "Process4", "Process5"]

# Mock for process size
process_size = [40, 50, 100, 200, 50]

# Mock for process threads
process_threads = np.zeros(5)

# Mock for process resources
# Those process resources should be a type of ENUM
process_resources = ["1", "2", "3", "4", "5"]

# Mock for process state
# Those process resources should be a type of ENUM also
process_state = ["ready", "execution", "ready", "block", "ready"]

root = tk.Tk()

process_df = pd.DataFrame({
    "Process name": process_name,
    "process size": process_size,
    "process_threads": process_threads,
    "process_resources": process_resources,
    "process state": process_state
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
