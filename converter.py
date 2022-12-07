from tkinter import *

window = Tk()
window.title("Miles to kilometers")
window.minsize(width=300, height=300)


my_label = Label(text='is equal to')
my_label.place(x=30, y=70)
my_label.config(padx=50, pady=50)

entry = Entry(width=10)
entry.place(x=130, y=80)
entry.insert(END, string='0')

mile = Label(text='Miles')
mile.place(x=160, y=80)

km = Label(text='Km')
km.place(x=160,  y=140)

output = Label(text='0')
output.place(x=130, y=140)


def convert():
    value = float(entry.get())
    result = value*1.609
    output.config(text=f"{result}")


button = Button(text='Calculate', command=convert)
button.place(x=130, y=180)


window.mainloop()