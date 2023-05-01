import tkinter as tk
from CSV import CSV
from tkinter import filedialog
from Data_management import Data_management as dm
from PIL import Image, ImageTk
from pandastable import Table


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.home_c = None
        self.home_fm = None
        self.bg_label = None
        self.bg = None
        self.button2 = None
        self.button = None
        self.Label = None
        self.message = None
        self.csv = None
        self.title('Avoid Accident 101')
        self.homepage()
        self.dm = None

    def run(self):
        self.mainloop()

    def readcsv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        self.csv = CSV(file_path)
        if self.csv.get_data() is False:
            self.message = tk.messagebox.showerror('Error', 'open CSV file failed')
        else:
            self.message = tk.messagebox.showinfo('Success', 'open CSV file successfully')
            self.dm = dm(self.csv.get_data())

    def homepage(self):
        # structure
        self.geometry('300x200')
        self.home_fm = tk.Frame(self)
        self.home_fm.pack(fill=tk.BOTH, expand=True)
        self.home_c = tk.Canvas(self.home_fm, width=300, height=200)
        self.home_c.pack()

        # widgets
        self.Label = tk.Label(self.home_fm, text='Welcome to Avoid Accident 101', font=("Arial", 14))
        self.button = tk.Button(self.home_fm, text='Start', command=self.mainpage, height=2, width=10)
        self.button2 = tk.Button(self.home_fm, text='Exit', command=self.destroy, height=2, width=10)

        # background
        img = Image.open('pic/mainbg.jpeg')
        self.bg = ImageTk.PhotoImage(img.resize((300, 200)))
        self.home_c.create_image(0, 0, image=self.bg, anchor=tk.NW)

        # position
        self.Label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        self.button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.button2.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

    def mainpage(self):
        self.home_fm.destroy()
        self.home_c.destroy()
        self.Label.destroy()
        self.button.destroy()
        self.button2.destroy()

        self.title('Avoid Accident 101')
        self.geometry('1200x900')

        # Main Frame
        mainframe = tk.Frame(self)
        mainframe.pack(fill=tk.BOTH, expand=True)

        # Menu Bar
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        menu = tk.Menu(menubar, tearoff=0)
        menu.add_command(label='Load CSV', command=self.readcsv)
        menu.add_command(label='Exit', command=self.destroy)
        menubar.add_cascade(label='Menu', menu=menu)

        # graph frame
        graphframe = tk.LabelFrame(mainframe, text='Graph', height=600)
        graphframe.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # menu frame
        menuframe = tk.LabelFrame(mainframe, text='Menu', height=400)
        menuframe.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        text = tk.StringVar(self)
        text.set("Select an Option")
        choice = ["Show data", "most accident per province", "2", "3", "4"]
        option = tk.OptionMenu(menuframe, text, *choice)
        option.config(width=50)
        option.grid(row=0, column=0, pady=100, sticky=tk.SW)

        def option_list():
            if text.get() == "Select an Option":
                self.message = tk.messagebox.showinfo("Error", "Please select an option")
            elif text.get() == "Show data":
                table_fm = tk.Frame(graphframe)
                table_fm.pack(fill=tk.BOTH, expand=1)
                try:
                    simple_table = Table(table_fm, dataframe=self.csv.get_data(), height=500, showstatusbar=True)
                    simple_table.show()
                except:
                    self.message = tk.messagebox.showinfo("Error", "Please select a CSV file", icon="warning")
                return
            elif text.get() == "most accident per province":
                self.dm.province_bar().pack()
            else:
                print("Selected Option: {}".format(text.get()))
            return None

        # button frame
        submit_button = tk.Button(menuframe, text='Submit', command=option_list)
        submit_button.grid(row=1, column=0)
