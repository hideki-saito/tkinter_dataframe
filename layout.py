from tkinter import *
from size_config import *

class layout(Frame):
    """Basic test frame for the table"""
    def __init__(self, parent=None):
        self.parent = parent
        Frame.__init__(self)
        self.main = self.master
        self.main.geometry(main_window_geometry)
        # self.main.title('Data Frame')

        self.control_frame = Frame(self.main, width=control_frame_width, height=control_frame_height)
        self.control_frame.pack(side=LEFT)

        self.lb1 = Listbox(self.control_frame)
        self.lb1.pack()
        self.lb1.place(x=listbox1_x, y=listbox1_y, width=listbox1_width, height=listbox1_height)
        self.lb1.bind("<Double-Button-1>", self.OnDouble_lb1)

        self.lb2 = Listbox(self.control_frame)
        self.lb2.pack()
        self.lb2.place(x=listbox2_x, y=listbox1_y, width=listbox1_width, height=listbox1_height)
        self.lb2.bind("<Double-Button-1>", self.OnDouble_lb2)

        self.include = IntVar()
        rb1 = Radiobutton(self.control_frame, text="Include", variable=self.include, value=1, activebackground=self.control_frame.cget('bg'))
        rb1.pack(anchor=W)
        rb1.place(x=radiobutton1_x, y=radiobutton1_y, width=radiobutton1_width)
        rb2 = Radiobutton(self.control_frame, text="exclude", variable=self.include, value=0, activebackground=self.control_frame.cget('bg'))
        rb2.pack(anchor=W)
        rb2.place(x=radiobutton1_x, y=radiobutton2_y, width=radiobutton1_width)

        self.table_frame = Frame(self.main)
        self.table_frame.pack(fill=BOTH, expand=1)

        # df = TableModel.getSampleData()
        # self.table = pt = Table(self.table_frame, dataframe=df)
        # pt.show()

        return

    def OnDouble_lb1(self, event):
        widget = event.widget
        selection = widget.curselection()
        value = widget.get(selection[0])
        if value not in self.lb2.get(0, END):
            self.lb2.insert(END, value)
        else:
            pass

    def OnDouble_lb2(self, event):
        widget = event.widget
        selection = widget.curselection()
        widget.delete(selection[0])

