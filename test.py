

from tkinter import messagebox
from tkinter import filedialog
from tkinter import *
import os

def process_file():
    i = 0
    for name in os.listdir(root.filename):
        try:
            head, tail = os.path.splitext(name)
            print(tail)
            os.rename(root.filename + "/" + name, root.filename + "/addd" + tail)
        except FileExistsError:
            os.rename(root.filename + "/" + name, root.filename + "/addd" + str(i) + tail)
            i += 1
            continue




root = Tk()
root.filename = filedialog.askdirectory()
proceed = messagebox.askyesno(title="Warning", message="Do u want to rename the file in" + root.filename)
print(proceed)
if proceed == True:
    print(root.filename)
    process_file()



