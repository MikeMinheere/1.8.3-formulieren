from tkinter import *

def checkWoord():
    global gekozenWoord
    foutMessage.pack_forget()
    if len(woordVar.get()) > 7 or len(woordVar.get()) < 4:
        foutMessage.pack()
    else:
        gekozenWoord = list(woordVar.get())
        frame.destroy()
        print(gekozenWoord)
        radenGenerator()

def radenGenerator():
    radenFrame = Frame(root)
    radenFrame.pack()
    for i in range(len(gekozenWoord)):
        globals()[f"letter{i}"] = Spinbox(radenFrame)

def invulGenerator():
    global foutMessage, woordVar, frame
    frame = Frame(root)
    frame.pack()

    vulIn = Label(frame, text='vul een woord in')
    vulIn.pack(pady=5)

    woordVar = StringVar(value = '')
    woordInvullen = Entry(frame,textvariable=woordVar)
    woordInvullen.pack(pady=5)

    text = Label(frame, text='tussen 4 en 7 letters')
    text.pack()

    foutMessage = Label(frame,text='kies een ander woord.')

    woordButton = Button(frame,text='stel woord in', command =checkWoord)
    woordButton.pack(pady=50)

root = Tk()
root.title('word guesser')
root.geometry('400x230')

invulGenerator()
root.mainloop()