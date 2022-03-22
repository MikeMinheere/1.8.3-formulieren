import tkinter
import time
from tkinter import CENTER,N,S,ttk

number = 0
upPressed = False
DownPressed = False
autoC = False

def update():
    if number == 0:
        root.config(bg='grey')
    elif number > 0:
        root.config(bg='green')
    elif number < 0:
        root.config(bg='red')
    displayNumber.config(text=number)

def tripleScore():
    global number,upPressed
    if upPressed:
       number *= 3
    elif downPressed:
        number /= 3   
    displayNumber.config(text=number)
        
def hoverMouse():
    root.config(bg='yellow')

def numUp():
    global number,upPressed,downPressed
    autoClicker.configure(state='active')
    number += 1
    upPressed = True
    downPressed = False
    update()

def numDown():
    global number,upPressed, downPressed
    autoClicker.configure(state='active')
    number -= 1
    upPressed = False
    downPressed = True
    update()



def autoClkr():
    global autoC,upPressed,downPressed   
    if not autoC:
        autoC = True
        while autoC:
            root.update()
            if upPressed: root.after(200, numUp())
            elif downPressed: root.after(200, numDown())   
    elif autoC:
        autoC = False

root = tkinter.Tk()
root.config(bg='grey')
root.geometry('600x550')
root.title('Clicker')

autoClicker = tkinter.Checkbutton(
    root,
    text='autoClicker',
    state = "disabled",
    command = autoClkr
)
autoClicker.place(x=1,y=1)
autoClicker.pack()

buttonUp=tkinter.Button(
    root,
    text='Up',
    font=("Courier", 14),
    anchor=N,
    command = numUp
)
buttonUp.pack(fill='x',padx=40,pady=60)

displayNumber = tkinter.Label(
    root,
    bg='white',
    text=number,
    font=("Courier", 14),
)
displayNumber.pack(fill='x',padx=40)

buttonDown=tkinter.Button(
    root
)

root.bind('<Up>',lambda event:numUp()),root.bind('+',lambda event:numUp())
root.bind('<Down>',lambda event:numDown()),root.bind('-',lambda event:numDown())
root.bind('<space>',lambda event:tripleScore())

buttonUp.bind('<Enter>',lambda event: hoverMouse())
buttonUp.bind('<Leave>',lambda event: update())

displayNumber.bind('<Enter>',lambda event: hoverMouse())
displayNumber.bind('<Leave>',lambda event: update())
displayNumber.bind('<Double-Button-1>',lambda event:tripleScore())

buttonDown.bind('<Enter>',lambda event: hoverMouse())
buttonDown.bind('<Leave>',lambda event: update())
buttonDown.configure(text='Down',font=("Courier", 14),anchor=S, command=numDown)
buttonDown.pack(fill='x',padx=40,pady=60)

root.mainloop()