import tkinter
from tkinter import ttk
from calendar import month_name
from datetime import datetime

root = tkinter.Tk()
root.geometry('500x400')
root.resizable(False, False)
root.title('days calculator')

label = tkinter.Label(text='date:',font='25')
label.grid(column= 1, row= 2)
label.pack()

maanden = ttk.Combobox(root, textvariable= month_name[2][0:3])
maanden['values'] = [month_name[i][0:3] for i in range(1,13)]
maanden['state'] = 'readonly'
maanden.pack(padx=5, pady=50)

current_month = datetime.now().strftime('%b')

maanden.set(current_month)

root.mainloop()