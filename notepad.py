from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as tsmg

root = Tk()
root.geometry('444x444')
root.title('Notepad')
root.iconbitmap('note.ico')

# Textbox widget
Textbox = Text(root, height=200, width=444)
Textbox.pack()

# File menu functions
def new_file():
    Textbox.delete(1.0, END)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            Textbox.delete(1.0, END)
            Textbox.insert(1.0, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            text_content = Textbox.get(1.0, END)
            file.write(text_content)



# Edit menu functions
def cut_text():
    Textbox.event_generate("<<Cut>>")

def copy_text():
    Textbox.event_generate("<<Copy>>")

def paste_text():
    Textbox.event_generate("<<Paste>>")

def help_f():
    tsmg.showinfo("Help",'Mail at amaankhan12e4@gmail.com')

# Menu
menu = Menu(root, tearoff=0)  # Top-level menu

# File submenu
file_menu = Menu(menu, tearoff=0)
file_menu.add_command(label='New', command=new_file)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_command(label='Quit', command=quit)
menu.add_cascade(label='File', menu=file_menu)

# Edit submenu
edit_menu = Menu(menu, tearoff=0)
edit_menu.add_command(label='Cut', command=cut_text)
edit_menu.add_command(label='Copy', command=copy_text)
edit_menu.add_command(label='Paste', command=paste_text)
menu.add_cascade(label='Edit', menu=edit_menu)


help_menu = Menu(menu, tearoff=0)
help_menu.add_command(label='Help', command=help_f)
help_menu.add_command(label='Support', command=help_f)
help_menu.add_command(label='Contact us', command=help_f)
menu.add_cascade(label='Help', menu=help_menu)

root.config(menu=menu)
root.mainloop()
