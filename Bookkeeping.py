#-------------------------------------------------------------------------------
# Name:        Bookkeeping
# Purpose:     Do bookkeeping
#
# Author:      Kristen
#
# Created:     28/08/2016
# Copyright:   (c) Kristen Jordan Koenig 2016
# Licence:     Creative Commons
#-------------------------------------------------------------------------------
from arcpy.da import InsertCursor, SearchCursor
import Tkinter as Tk
from Tkinter import *

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print "hi there, everyone!"

def main():
    root = Tk()

    app = App(root)

    root.mainloop()
    root.destroy() # optional; see description below

if __name__ == '__main__':
    main()
