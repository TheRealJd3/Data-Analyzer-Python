from tkinter import *
import tkinter.messagebox

import data
class gui:
    #Variables
    root = Tk()
    global entry2a
    global entry5
    global uuid


    def __init__(self, dataframe):
        #define panda datframes obj &json file both
        self.dataframe= dataframe
#task2 comps
        label_task2 = Label(self.root, text='Task 2')
        label2a = Label(self.root, text='Document ID')
        self.entry2a = Entry(self.root)
        task2a_button = Button(self.root, text='Plot by country', command=self.task2a)
        task2b_button = Button(self.root, text='Plot by continent', command=self.task2b)

        label_task2.grid(row=0, columnspan=4, sticky=W)
        label2a.grid(row=1, column=0)
        self.entry2a.grid(row=1, column=1)
        task2a_button.grid(row=2, column=1, sticky=W)
        task2b_button.grid(row=2, column=2, sticky=W)

        hint_task2 = Label(self.root, text='Enter document id to get histo by country/continent')
        hint_task2.grid(row=1, column=2, sticky=W)

#For task 3 comps
        label_task3a = Label(self.root, text='Task 3a')
        label_task3a.grid(row=3, column=0, columnspan=4, sticky=W)
        task3a_button = Button(self.root, text='Verbose-Browser plot', command=self.task3a)
        task3a_button.grid(row=4, column=0, columnspan=2, sticky=W)

        label_task3b = Label(self.root, text='Task 3b')
        label_task3b.grid(row=5, column=0, columnspan=4, sticky=W)
        task3b_button = Button(self.root, text='Popular-Browser plot', command=self.task3b)
        task3b_button.grid(row=6, column=0, columnspan=2, sticky=W)
        hint_task3 = Label(self.root, text='To get histogram of view by verbose browsers, click a button')

        hint_task3.grid(row=4, column=2, sticky=W)

        hint_task3 = Label(self.root, text='To get histogram of views by popular browsers, click a button')
        hint_task3.grid(row=6, column=2, sticky=W)

        #for task5
        label_task5 = Label(self.root, text='Task 5')
        label5 = Label(self.root, text='Document ID')
        labeluid = Label(self.root, text='User ID')
        self.entry5 = Entry(self.root)
        self.uuid = Entry(self.root)
        task5_button = Button(self.root, text='Draw also like graph', command=self.task5)
        label_task5.grid(row=7, columnspan=4, sticky=W)
        label5.grid(row=8, column=0)
        self.entry5.grid(row=8, column=1)
        labeluid.grid(row=8, column=2,sticky=W)
        self.uuid.grid(row=8, column=3)
        label_dummy= Label(self.root, text='')
        label_dummy.grid(row=8, column=4,sticky=W)
        task5_button.grid(row=10, column=1, sticky=W)
        self.root.mainloop()

#All methods below this on clicking respective buttons call respective functions
    def task2a(self):
        data.bycountry(self.dataframe, self.entry2a.get())
        self.root.mainloop()
    def task2b(self):
        data.bycontinent(self.dataframe, self.entry2a.get())
        self.root.mainloop()

    def task3a(self):
        data.verbosehisto(self.dataframe)
        self.root.mainloop()

    def task3b(self):
        data.properhisto(self.dataframe)
        self.root.mainloop()

    def task5(self):
        data.task5(self.dataframe,self.entry5.get(),self.uuid.get())
        self.root.mainloop()

