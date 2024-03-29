from tkinter import *
from tkinter import filedialog

root=Tk("Text Editor")

#Text Area
text=Text(root)
text.grid()

def saveas():
    global text
    t = text.get("1.0", "end-1c")
    savelocation=filedialog.asksaveasfilename()
    file1=open(savelocation, "w+")
    file1.write(t)
    file1.close()

def FontHelvetica():
    global text
    text.config(font="Helvetica")

def FontCourier():
    global text
    text.config(font="Courier")

def FontArial():
    global text
    text.config(font="Arial")

# Save Button
button=Button(root, text="Save", command=saveas)
button.grid()

#Font Button
font=Menubutton(root, text="Font") 
font.grid() 

font.menu=Menu(font, tearoff=0) 
font["menu"]=font.menu

helvetica=IntVar()
courier=IntVar()
arial=IntVar()

font.menu.add_checkbutton(label="Courier", variable=courier, command=FontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=helvetica, command=FontHelvetica)
font.menu.add_checkbutton(label="Arial", variable=arial, command=FontArial)

root.mainloop()