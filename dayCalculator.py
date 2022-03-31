import tkinter as tk
from tkinter import ttk
import datetime
from datetime import date

def update(arg1,arg2,arg3):
    global months, maanden
    dagen.config(values= months[maanden.get()])

months = {
    'Jan': [i for i in range(1,32)],
    'Feb': [i for i in range(1,29)],
    'Mar': [i for i in range(1,32)],
    'Apr': [i for i in range(1,31)],
    'May': [i for i in range(1,32)],
    'Jun': [i for i in range(1,31)],
    'Jul': [i for i in range(1,32)],
    'Aug': [i for i in range(1,32)],
    'Sep': [i for i in range(1,31)],
    'Okt': [i for i in range(1,32)],
    'Nov': [i for i in range(1,31)],
    'Dec': [i for i in range(1,32)]
}

currentDate = datetime.datetime.now()

root = tk.Tk()
root.geometry('500x400')
root.resizable(False, False)
root.title('days calculator')

label = tk.Label(text='date:',font='25')
label.grid(column= 1, row= 2)
label.pack()

#de maanden box
maandenVar = tk.StringVar()
maandenVar.trace('w',update)
maanden = ttk.Combobox(root, values = [i for i in months.keys()],textvariable= maandenVar)
maanden['state'] = 'readonly'
maanden.pack(padx=3, pady=50)
maanden.set(currentDate.strftime('%b'))

#de dagen box
dagen = ttk.Combobox(root, values=[i for i in range(1,32)])
dagen['state'] = 'readonly'
dagen.pack(padx=7, pady=50)
dagen.set(currentDate.strftime('%d'))

#de jaren box
jaarInvullen = tk.StringVar(value = currentDate.strftime('%Y'))
jaar = tk.Entry(root, textvariable=jaarInvullen)
jaar.pack(padx=50, pady=50)
root.mainloop()