import os
import subprocess
import tkinter as tk
from tkinter import messagebox

from PIL import Image, ImageTk
from itertools import count




class ImageLabel(tk.Label):
    """a label that displays images, and plays them if they are gifs"""

    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 10

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image="")
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)


def to_main():
    root.destroy()
    subprocess.call(["python", "gametest.py"])



def to_play():
    root.destroy()
    if(varage<=12):
        subprocess.call(["python", "RISK OF  WORDS/easy.py"])
    if (13 < varage < 18):
        subprocess.call(["python", "RISK OF  WORDS/medium.py"])
    if (varage > 18):
        subprocess.call(["python", "RISK OF  WORDS/hard.py"])
varage=0
varname=""

def confirm():
    global varage
    varage =age.get()
    varname=name.get()
    print(varage,varname)
    if(varage=="admin" and varname=="admin"):
        root.destroy()
        subprocess.call(["python", "AdminGUI.py"])

    else:
        messagebox.showwarning('ERROR', 'Maybe LOGIN or PASSWORD are wrong !! \n\n  Retry again')
        name.delete(0, 'end')
        age.delete(0, 'end')


root = tk.Tk()
root.title('Risk of Words')
lbl = ImageLabel(root)
lbl.pack()
lbl.load('admin2.gif')
root.configure(background="#262626")
root.geometry("720x500")

btn1 = tk.Button(root, text="Enter Your Login :", font="Algerian", width=20, height=1, bg="white",
                 activebackground="#a0fa4c", )
btn1.place(x=50, y=20)
name = tk.Entry(root, text="Enter Your Login :", font="Algerian", width=20, bd=5)
name.place(x=300, y=20)
btn2 = tk.Button(root, text="Enter Your Password :", font="Algerian", width=20, height=1, bg="White",
                 activebackground="#f4ca60")
btn2.place(x=50, y=80)
age = tk.Entry(root, text="Enter Your Password :", font="Algerian", width=20, bd=5)
age.place(x=300, y=80)

btn3 = tk.Button(root, text="CONNECT", font="Algerian", width=20, height=1, bg="White", activebackground="#37d3ff",command=confirm)
btn3.place(x=230, y=150)
btn4 = tk.Button(root, text="Back to MAIN", font="Algerian", width=20, height=1, bg="White", activebackground="#fa7731", command=to_main)
btn4.place(x=230, y=250)
btn5 = tk.Button(root, text="Exit", font="Algerian", width=20, height=1, bg="White", activebackground="#FF0000",command=root.destroy)
btn5.place(x=230, y=300)


root.mainloop()
