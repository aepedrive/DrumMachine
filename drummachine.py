#!/usr/bin/env python

from Tkinter import *

#constants
MAX_DRUM_NUM = 5

class DrumMachine():

    def create_top_bar(self):
        """Creates top buttons"""
        topbar_frame = Frame(self.root)
        topbar_frame.config(height=25)
        topbar_frame.grid(row=0, columnspan=12, rowspan=10, padx=5, pady=5)
        #
        Label(topbar_frame, text='Units:').grid(row=0, column=4)
        self.units = IntVar()
        self.units.set(4)
        self.units_widget = Spinbox(topbar_frame, from_=1, to=8, width=5,
                                    textvariable=self.units)
        self.units_widget.grid(row=0, column=5)
        #
        Label(topbar_frame, text='BPUs:').grid(row=0, column=6)
        self.bpu = IntVar()
        self.bpu.set(4)
        self.bpu_widget = Spinbox(topbar_frame, from_=1, to=10, width=5,
                                  textvariable=self.bpu)
        self.bpu_widget.grid(row=0, column=7)

    def create_left_pad(self):
        left_frame = Frame(self.root)
        left_frame.grid(row=10, column=0, columnspan=6, sticky=W+E+N+S)
        tbicon = PhotoImage(file='images/openfile.gif')
        for i in range(0, MAX_DRUM_NUM):
            button = Button(left_frame, image=tbicon)
            button.image = tbicon
            button.grid(row=i, column=0, padx=5, pady=2)
            self.drum_entry = Entry(left_frame)
            self.drum_entry.grid(row=i, column=4, padx=7, pady=2)

    def app(self):
        self.root = Tk()
        self.root.title("Drum Beast")
        self.create_top_bar()
        self.create_left_pad()
        self.root.mainloop()

# ================================================
if __name__ == '__main__':
    
    dm = DrumMachine()
    dm.app()
