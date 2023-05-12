import tkinter as tk
from CSV import CSV
from tkinter import filedialog
from Data_management import Data_management as Dm
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from PIL import Image, ImageTk
from pandastable import Table
from screeninfo import get_monitors


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.mainframe = None
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
        self.graphframe = None
        self.menuframe = None
        self.mainframe = None

    def run(self):
        self.mainloop()

    def readcsv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        self.csv = CSV(file_path)
        if self.csv.get_data() is False:
            self.message = tk.messagebox.showerror('Error', 'open CSV file failed')
        else:
            self.dm = Dm(self.csv.get_data())
            self.message = tk.messagebox.showinfo('Success', 'open CSV file successfully')

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
        img = Image.open('../file/mainbg.jpeg')
        self.bg = ImageTk.PhotoImage(img.resize((300, 200)))
        self.home_c.create_image(0, 0, image=self.bg, anchor=tk.NW)

        # position
        self.Label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        self.button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.button2.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

    def mainpage(self):
        try:
            self.title('Avoid Accident 101')
            self.geometry('600x400')
            self.home_fm.destroy()
            self.home_c.destroy()
            self.Label.destroy()
            self.button.destroy()
            self.button2.destroy()
            self.home_fm = None
            self.home_c = None
            self.Label = None
            self.button = None
            self.button2 = None
        except Exception as e:
            # print(e)
            self.mainframe.destroy()
            self.mainframe = None
        # Main Frame
        self.mainframe = tk.Frame(self)
        self.mainframe.pack(fill=tk.BOTH, expand=True)

        # Menu Bar
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        menu = tk.Menu(menubar, tearoff=0)
        menu.add_command(label='back to menu', command=self.mainpage)
        menu.add_command(label='Exit', command=self.destroy)

        csv_menu = tk.Menu(menu, tearoff=0)
        csv_menu.add_command(label='Load CSV', command=self.readcsv)

        menubar.add_cascade(label='Menu', menu=menu)
        menubar.add_cascade(label='CSV', menu=csv_menu)


        # menu frame
        self.menuframe = tk.LabelFrame(self.mainframe)
        self.menuframe.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        menu_text = tk.Label(self.menuframe, text='Avoid Accident 101', font=("Arial", 36))
        menu_text.pack(side=tk.TOP, padx=10, pady=10)
        text = tk.StringVar(self)
        text.set("Select an Option")

        # option menu
        choice = ["Show data", "most accident per province", "create own visualization", "find path", "4"]
        option = tk.OptionMenu(self.menuframe, text, *choice)
        option.config(width=40, height=1, font=("Arial", 10))
        option.pack(side=tk.TOP, padx=10, pady=10)

        def option_list():
            try:
                self.csv.get_data()
                if self.csv.check_file() is False:
                    raise Exception('Please load CSV file')
            except Exception as e:
                # print(e)
                self.message = tk.messagebox.showinfo("Error", "Please select a CSV file", icon="warning")
            else:
                if text.get() != "Select an Option":
                    self.menuframe.destroy()
                    # graph frame
                    self.graphframe = tk.LabelFrame(self.mainframe, text='Graph', height=600, width=1200)
                    self.graphframe.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
                    self.geometry('1200x600')
                if text.get() == "Select an Option":
                    self.message = tk.messagebox.showinfo("Error", "Please select an option")
                elif text.get() == "Show data":
                    try:
                        self.table_fm.destroy()
                    except Exception as e:
                        # print(e)
                        pass
                    try:
                        self.canvas.get_tk_widget().destroy()
                    except:
                        pass
                    self.table_fm = tk.Frame(self.graphframe)
                    self.table_fm.pack(fill=tk.BOTH, expand=1)
                    try:
                        simple_table = Table(self.table_fm, dataframe=self.csv.get_data(), height=500, showstatusbar=True)
                        simple_table.show()
                    except Exception as e:
                        # print(e)
                        self.message = tk.messagebox.showinfo("Error", "Please select a CSV file", icon="warning")
                    return
                elif text.get() == "most accident per province":
                    try:
                        self.table_fm.destroy()
                    except Exception as e:
                        # print(e)
                        pass
                    try:
                        self.canvas.get_tk_widget().destroy()
                    except:
                        pass
                    self.canvas = FigureCanvasTkAgg(self.dm.province_bar(), master=self.graphframe)
                    self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
                elif text.get() == "create own visualization":
                    self.graphframe.destroy()
                    self.ov = tk.LabelFrame(self.mainframe)
                    self.ov.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
                    self.listbox = tk.Listbox(self.ov, selectmode=tk.MULTIPLE, height=10)
                    self.listbox.pack(side=tk.LEFT)
                elif text.get() == "find path":
                    self.geometry('900x400')
                    if self.csv.check_file():
                        self.graphframe.destroy()
                        self.fp = tk.LabelFrame(self.mainframe)
                        self.fp.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

                        menu_text = tk.Label(self.fp, text='Avoid Accident 101', font=("Arial", 36), anchor=tk.CENTER)
                        menu_text.grid(row=0, column=0, columnspan=10, padx=10, pady=10, sticky=tk.N)

                        # Departure listbox and scrollbar
                        departure_frame = tk.Frame(self.fp)
                        departure_frame.grid(row=1, column=0, padx=50, pady=10)

                        self.departure = tk.Label(departure_frame, text='Departure', font=("Arial", 10))
                        self.departure.pack()

                        self.listbox1 = tk.Listbox(departure_frame, height=15, width=30)
                        self.listbox1.pack(side=tk.LEFT)

                        sc_bar1 = tk.Scrollbar(departure_frame, orient=tk.VERTICAL, command=self.listbox1.yview)
                        sc_bar1.pack(side=tk.LEFT, fill=tk.Y)

                        self.listbox1.config(yscrollcommand=sc_bar1.set)

                        for i in self.dm.get_province():
                            self.listbox1.insert(tk.END, i)

                        # Destination listbox and scrollbar
                        destination_frame = tk.Frame(self.fp)
                        destination_frame.grid(row=1, column=1, padx=50, pady=10)

                        self.destination = tk.Label(destination_frame, text='Destination', font=("Arial", 10))
                        self.destination.pack()

                        self.listbox2 = tk.Listbox(destination_frame, height=15, width=30)
                        self.listbox2.pack(side=tk.LEFT)

                        sc_bar2 = tk.Scrollbar(destination_frame, orient=tk.VERTICAL, command=self.listbox2.yview)
                        sc_bar2.pack(side=tk.LEFT, fill=tk.Y)

                        self.listbox2.config(yscrollcommand=sc_bar2.set)
                        for i in self.dm.get_province():
                            self.listbox2.insert(tk.END, i)

                        t_frame = tk.LabelFrame(self.fp)
                        t_frame.grid(row=1, column=2, columnspan=2, padx=50, pady=30, sticky=tk.N)
                        self.sdep = tk.LabelFrame(t_frame, text="Departure", font=("Arial", 10), width=200)
                        self.sdes = tk.LabelFrame(t_frame, text="Destination", font=("Arial", 10), width=200)
                        var_dep = tk.StringVar()
                        var_des = tk.StringVar()

                        self.selected_departure = tk.Entry(self.sdep, textvariable=var_dep, state='disabled', width=30)
                        self.selected_destination = tk.Entry(self.sdes, textvariable=var_des, state='disabled', width=30)

                        self.sdep.pack()
                        self.selected_departure.grid(row=0, column=0)
                        self.sdes.pack()
                        self.selected_destination.grid(row=0, column=0)

                        def update_selected_departure(event):
                            if self.listbox1.curselection():
                                selected_item = self.listbox1.get(self.listbox1.curselection())
                                var_dep.set(selected_item)

                        def update_selected_destination(event):
                            if self.listbox2.curselection():
                                selected_item = self.listbox2.get(self.listbox2.curselection())
                                var_des.set(selected_item)

                        self.listbox1.bind('<<ListboxSelect>>', update_selected_departure)
                        self.listbox2.bind('<<ListboxSelect>>', update_selected_destination)

                        def find_path():
                            self.fp.destroy()
                            self.geometry('900x600')
                            self.fpg = tk.LabelFrame(self.mainframe)
                            self.fpg.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
                            # print(var_dep.get(), var_des.get())
                            self.canvas = FigureCanvasTkAgg(self.dm.create_basemap_plot(var_dep.get(), var_des.get()), master=self.fpg)
                            self.toolbar = NavigationToolbar2Tk(self.canvas, self.fpg)
                            self.toolbar.update()
                            self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

                        submit_button = tk.Button(self.fp, text='Submit', command=find_path, height=1, width=10)
                        submit_button.grid(row=3, column=0, columnspan=4, padx=50, pady=10, sticky=tk.N)
                    else:
                        self.message = tk.messagebox.showinfo("Error", "Please select a CSV file", icon="warning")

                else:
                    print("Selected Option: {}".format(text.get()))
                return None

        # button frame
        submit_button = tk.Button(self.menuframe, text='Submit', command=option_list, height=1, width=10)
        submit_button.pack(side=tk.BOTTOM, pady=10)
