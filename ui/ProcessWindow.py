from tkinter import *

from OS_SIMULATION.class_Proceso import Proceso


class ProcessWindow:

    def __init__(self, win):
        self.lb_process_id = Label(win, text="Process id")
        self.lb_process_name = Label(win, text="Name")
        self.lb_process_weight = Label(win, text="Weight")
        self.lb_process_threads = Label(win, text="Number of threads")
        self.lb_process_resources = Label(win, text="Resources")

        self.input_process_id = Entry()
        self.input_process_name = Entry()
        self.input_process_weight = Entry()
        self.input_process_threads = Entry()

        #TODO("Resources should be treated like a resources predefined list")

        self.lb_process_id.place(x=100, y=50)
        self.input_process_id.place(x=200, y=50)
        self.lb_process_name.place(x=100, y=100)
        self.input_process_name.place(x=200, y=100)
        self.lb_process_weight.place(x=100, y=150)
        self.input_process_weight.place(x=200, y=150)
        self.lb_process_threads.place(x=100, y=200)
        self.input_process_threads.place(x=200, y=200)

        self.btn_create_process = Button(win, text='Accept', command=self.create, width=5, height=1)
        self.btn_new_process = Button(win, text='New', command=self.new)
        self.btn_create_process.place(x=0, y=280)
        self.btn_new_process.place(x=60, y=280)

    def create(self):
        process_id = int(self.input_process_id.get())
        process_name = str(self.input_process_name.get())
        process_weight = int(self.input_process_weight.get())
        process_threads = int(self.input_process_threads.get())

        process_characteristics_to_save = [
            process_id,
            process_name,
            process_weight,
            process_threads,
            "resoruces is pending"
        ]

        process = Proceso(process_characteristics_to_save)

    # Clear all fields
    def new(self):
        self.input_process_id.delete(0, 'end')
        self.input_process_name.delete(0, 'end')
        self.input_process_weight.delete(0, 'end')
        self.input_process_threads.delete(0, 'end')


window = Tk()
my_win = ProcessWindow(window)
window.title('Hello Python')
window.geometry('500x300+10+10')
window.mainloop()
