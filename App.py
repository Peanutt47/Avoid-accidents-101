import tkinter as tk
from CSV import CSV
from Data_management import Data_managemnt as dm


class app(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Avoid Accident 101')
        self.geometry('800x600')

        # Main Frame
        mainframe = tk.Frame(self)
        mainframe.pack(fill=tk.BOTH, expand=True)

        # Menu Bar
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        menu = tk.Menu(menubar, tearoff=0)
        menu.add_command(label='Open CSV', command=self.readcsv)
        menu.add_command(label='Exit', command=self.destroy)

        menubar.add_cascade(label='Menu', menu=menu)

        # graph frame
        graphframe = tk.LabelFrame(mainframe, text='Graph', height=400)
        graphframe.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # menu frame
        menuframe = tk.LabelFrame(mainframe, text='Menu', height=200)
        menuframe.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)


    def run(self):
        self.mainloop()

    def readcsv(self):
        csv = CSV()
        dm(csv.get_data())


