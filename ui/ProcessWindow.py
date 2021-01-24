from tkinter import *

from model.class_Proceso import Proceso
from model.modelo import Modelo
from ui.ProcessStatistics import ProcessStatistics
from random import randint
from tkinter import ttk


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
            process_stats = ProcessStatistics(process_result, third_frame)
            process_stats.update_view()

    def clean_process_frame(self):
        for widget in self.process_frame.winfo_children():
            widget.destroy()

        self.new()

    def stats(self):
        # Call [ProcessStatistics] and pass the process information, we have to get this
        # information from model [Process]
        ProcessStatistics(self.process_to_execute, third_frame)


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
third_frame = Frame(my_canvas)

# Add that new frame to a window in the canvas
my_canvas.create_window((0, 300), window=third_frame, anchor="nw")

my_win = ProcessWindow(main_frame)
window.title('Hello Python')
window.geometry('500x300+10+10')
window.mainloop()
