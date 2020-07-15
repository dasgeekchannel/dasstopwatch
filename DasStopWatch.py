#!/usr/bin/env python3
# Special thanks to https://www.sourcecodester.com for the template
# Modified and geek'i'fied by DasGeek
# www.dasgeekcommunity.com
# Updates to code include output each time stop button is pushed to TXT file. Print to console segment length.
# Image support
# Turned off Milliseconds (still in code if you need it)

from tkinter import *
import tkinter.messagebox as tkMessageBox
import PIL
from PIL import Image, ImageTk  # import package to allow for image display (Pillow)
import time  # used to make calculations for stopwatch
import sys  # used to export printed segment times to a txt file
import os # used to read the SNAP environment variable, to access resources 

# We'll reference the path to segments.txt multiple times, so let's put it in a variable

if "SNAP" in os.environ: # If running from the snap,...
    path = os.environ.get("HOME") # ... segments.txt will be placed in snap's home dir (~/snap/dasstopwatch/current) 
else:
    path = "." # ... otherwise, segments.txt will be placed in current directory
segments_txt = "{}/segments.txt".format(path)

def Main():
    global root
    # Design for Tkinter GUI
    root = Tk()
    root.title("DasStopWatch")
    width = 600
    height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    root.geometry(f"{width}x{height}+{x}+{y}")
    Top = Frame(root, width=600)
    Top.pack(side=TOP)
    resources = os.environ.get("SNAP", ".") # Set resources to the root of the snap, and defaults to "."
    img = Image.open("{}/das-stopwatch-logo.png".format(resources))  # import dasgeeklogo
    photo = ImageTk.PhotoImage(img)  # picture file you want to import location
    lab = Label(image=photo).place(x=120, y=100)  # img location on x,y axis
    stopWatch = StopWatch(root)
    stopWatch.pack(side=TOP)
    Bottom = Frame(root, width=600)
    Bottom.pack(side=BOTTOM)
    Start = Button(Bottom, text='Start', command=stopWatch.Start, width=10, height=2)
    Start.pack(side=LEFT)
    Stop = Button(Bottom, text='Stop', command=stopWatch.Stop, width=10, height=2)
    Stop.pack(side=LEFT)
    Reset = Button(Bottom, text='Reset', command=stopWatch.Reset, width=10, height=2)
    Reset.pack(side=LEFT)
    Exit = Button(Bottom, text='Exit', command=stopWatch.Exit, width=10, height=2)
    Exit.pack(side=LEFT)
    Title = Label(Top, text="DasStop Watch", font=("arial", 20), fg="white", bg="black")
    Title.pack(fill=X)
    root.config(bg="black")
    # Check if segements.txt already exists. We might not want to append to it, so we'll delete it if needed.
    if os.path.exists(segments_txt):
        result = tkMessageBox.askquestion('DLN', 'File {} already exits. Do you want to delete it?'.format(segments_txt), icon='warning')
        if result == 'yes':
            os.remove(segments_txt)
    root.mainloop()



class StopWatch(Frame):

    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self.startTime = 0.0
        self.nextTime = 0.0
        self.onRunning = 0
        self.timestr = StringVar()
        self.MakeWidget()

    def MakeWidget(self):
        timeText = Label(self, textvariable=self.timestr, font=("times new roman", 50), fg="green", bg="black")
        self.SetTime(self.nextTime)
        timeText.pack(fill=X, expand=NO, pady=2, padx=2)

    def Updater(self):
        self.nextTime = time.time() - self.startTime
        self.SetTime(self.nextTime)
        self.timer = self.after(50, self.Updater)

    def SetTime(self, nextElap):
        minutes = int(nextElap / 60)
        seconds = int(nextElap - minutes * 60.0)
        # miliSeconds = int((nextElap - minutes*60.0 - seconds)*100) #uncomment to turn on milliseconds
        self.timestr.set('%02d:%02d' % (
        minutes, seconds))  # add another %02d and add millisecond after seconds to turn on milliseconds

    # Define Start button actions
    def Start(self):
        if not self.onRunning:
            self.startTime = time.time() - self.nextTime
            self.Updater()
            self.onRunning = 1

    # Define Stop button functionality
    def Stop(self):
        if self.onRunning:
            self.after_cancel(self.timer)
            self.nextTime = time.time() - self.startTime
            self.SetTime(self.nextTime)
            self.onRunning = 0
            print(self.nextTime)  # print segment times to console
            with open(segments_txt, 'a+') as fd:
                fd.write('%.2f\n' % self.nextTime)
                # by using the `with` keyword as shown
                # fd.close() is implicit once you get out of the block

    # Define Exit button actions
    def Exit(self):
        result = tkMessageBox.askquestion('DLN', 'Are you sure you want to exit?', icon='warning')
        if result == 'yes':
            root.destroy()
            # If we have recorded some segments, we dump the path on the console, so we can easily copy/paste the path.
            #  Otherwise, we notify that we recorded nothing.
            if os.path.exists(segments_txt):
                print("segments.txt is located at {}".format(segments_txt))
            else:
                print("No segments were recorded")
            exit()

    # Define Reset button actions
    def Reset(self):
        self.startTime = time.time()
        self.nextTime = 0.0
        self.SetTime(self.nextTime)


if __name__ == '__main__':
    Main()
