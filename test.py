# from Tkinter import *
#
# root = Tk()
# text = Text(root)
# text.insert(INSERT, "Hello.....")
# text.insert(END, "Bye Bye.....")
# text.pack()
#
# text.tag_add("here", "1.0", "1.4")
# text.tag_add("start", "1.8", "1.13")
# text.tag_config("here", background="yellow", foreground="blue")
# text.tag_config("start", background="black", foreground="green")
#
# root.mainloop()

# import Tkinter
# root = Tkinter.Tk()
#
# for r in range(100):
#     for c in range(100):
#         Tkinter.Entry(root, text='R%s/C%s'%(r,c),
#             borderwidth=1 ).grid(row=r,column=c)
# root.mainloop(  )


# from Tkinter import *
# from pandastable import Table
# #assuming parent is the frame in which you want to place the table
# root = Tk()
# frame = Frame(root)
# frame.pack()
#
# pt = Table()
# pt.show()
# root.mainloop()

# from tkintertable import TableCanvas, TableModel
# from Tkinter import *
#
# master = Tk()
# tframe = Frame(master)
# tframe.pack()
# table = TableCanvas(tframe)
# table.createTableFrame()
#
# master.mainloop()

# import tkinter as tk
#
# class Demo1:
#     def __init__(self, master):
#         self.master = master
#         self.frame = tk.Frame(self.master)
#         self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
#         self.button1.pack()
#         self.frame.pack()
#
#     def new_window(self):
#         self.newWindow = tk.Toplevel(self.master)
#         self.app = Demo2(self.newWindow)
#
# class Demo2:
#     def __init__(self, master):
#         self.master = master
#         self.frame = tk.Frame(self.master)
#         self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
#         self.quitButton.pack()
#         self.frame.pack()
#
#     def close_windows(self):
#         self.master.destroy()
#
# def main():
#     root = tk.Tk()
#     app = Demo1(root)
#     root.mainloop()
#
# if __name__ == '__main__':
#     main()

# from Tkinter import *
# class MyFirstGUI:
#     def __init__(self, master):
#         self.master = master
#         master.title("A simple GUI")
#
#         self.label = Label(master, text="This is our first GUI!")
#         self.label.pack()
#
#         self.greet_button = Button(master, text="Greet", command=self.greet)
#         self.greet_button.pack()
#
#         self.close_button = Button(master, text="Close", command=master.quit)
#         self.close_button.pack()
#
#     def greet(self):
#         print("Greetings!")
#
# root = Tk()
# my_gui = MyFirstGUI(root)
# root.mainloop()

# from tkinter import Tk, Label, Button, StringVar
#
# class MyFirstGUI:
#     LABEL_TEXT = [
#         "This is our first GUI!",
#         "Actually, this is our second GUI.",
#         "We made it more interesting...",
#         "...by making this label interactive.",
#         "Go on, click on it again.",
#     ]
#     def __init__(self, master):
#         self.master = master
#         master.title("A second simple GUI")
#
#         self.label_index = 0
#         self.label_text = StringVar()
#         self.label_text.set(self.LABEL_TEXT[self.label_index])
#         self.label = Label(master, textvariable=self.label_text)
#         self.label.bind("<Button-1>", self.cycle_label_text)
#         self.label.pack()
#
#         self.greet_button = Button(master, text="Greet", command=self.greet)
#         self.greet_button.pack()
#
#         self.close_button = Button(master, text="Close", command=master.quit)
#         self.close_button.pack()
#
#     def greet(self):
#         print("Greetings!")
#
#     def cycle_label_text(self, event):
#         self.label_index += 1
#         self.label_index %= len(self.LABEL_TEXT) # wrap around
#         self.label_text.set(self.LABEL_TEXT[self.label_index])
#
# root = Tk()
# my_gui = MyFirstGUI(root)
# root.mainloop()

from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E

class Calculator:

    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.total = 0
        self.entered_number = 0

        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)

        self.label = Label(master, text="Total:")

        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.add_button = Button(master, text="+", command=lambda: self.update("add"))
        self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))

        # LAYOUT

        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)

        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)

        self.add_button.grid(row=2, column=0)
        self.subtract_button.grid(row=2, column=1)
        self.reset_button.grid(row=2, column=2, sticky=W+E)

    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        if method == "add":
            self.total += self.entered_number
        elif method == "subtract":
            self.total -= self.entered_number
        else: # reset
            self.total = 0

        self.total_label_text.set(self.total)
        self.entry.delete(0, END)

root = Tk()
my_gui = Calculator(root)
root.mainloop()

