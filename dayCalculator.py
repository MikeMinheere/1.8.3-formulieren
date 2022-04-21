import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import datetime
from datetime import date


#functie om de dagen te updaten
def update(arg1,arg2,arg3):
    global months, monthsCombo,jaar,dagen
    if int(jaar.get()) % 4 == 0:
        months['Feb'] = [i for i in range(1,30)]
    else: months['Feb'] = [i for i in range(1,29)]

    if int(dagen.get()) > months[monthsCombo.get()][-1]:
        dagen.current(months[monthsCombo.get()][-2])

    dagen.configure(values= months[monthsCombo.get()])

def calculate():
    date1 = date.today()
    date2 = date(int(jaar.get()),list(months.keys()).index(monthsCombo.get()) + 1,int(dagen.get())) 
    deltaDate = date2-date1
    if deltaDate.days > 0:
        if deltaDate.days == 1:
            tkinter.messagebox.showinfo('days calculator', 'dat is morgen')
        elif deltaDate.days > 1:
            tkinter.messagebox.showinfo('days calculator', f'dat is {deltaDate.days} dagen in de toekomst')
    elif deltaDate.days < 0:
        if deltaDate.days == -1:
            tkinter.messagebox.showinfo('days calculator', 'dat was gisteren')
        elif deltaDate.days < -1:
            tkinter.messagebox.showinfo('days calculator', f'dat is {-deltaDate.days} dagen in het verleden')
    else: tkinter.messagebox.showinfo('days calculator', 'dat is vandaag')

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
root.geometry('300x200')
root.resizable(False, False)
root.title('days calculator')

label = tk.Label(text='date:',font='25')
label.grid(column= 1, row= 2)
label.pack()

#de dagen box
dagen = ttk.Combobox(root, values=[i for i in range(1,32)])
dagen['state'] = 'readonly'
dagen.pack(pady=5)
dagen.set(currentDate.strftime('%d'))

#de monthsCombo box
monthsVar = tk.StringVar()
monthsCombo = ttk.Combobox(root, values = [i for i in months.keys()],textvariable= monthsVar)
monthsCombo['state'] = 'readonly'
monthsCombo.pack(pady=5)
monthsCombo.set(currentDate.strftime('%b'))

#de jaren box
jaarInvullen = tk.StringVar(value = currentDate.strftime('%Y'))
jaar = tk.Entry(root, textvariable=jaarInvullen)
jaar.pack(pady=5)
jaarInvullen.trace('w',update)
monthsVar.trace('w',update)

button = tk.Button(text = 'press to calculate!',command = calculate)
button.pack(pady=30)

root.mainloop()
