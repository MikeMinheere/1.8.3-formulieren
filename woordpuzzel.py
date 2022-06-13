from string import ascii_lowercase
import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

sbList = list()

def checkWoord():
    foutMessage.pack_forget()
    if len(woordVar.get()) > 7 or len(woordVar.get()) < 4:
        foutMessage.pack()
    else:
        frame.destroy()
        radenGenerator()

def radenGenerator():
    global frame2
    frame2 = Frame(root)
    frame2.place(relheight=1,relwidth=1,relx=0,rely=0)
    global sbList,score,woordVarLen
    woordVarLen=len(woordVar.get())
    score=(woordVarLen*woordVarLen)
    for i in range(len(woordVar.get())):
        ranNum = random.randint(0, 3)
        ansVar = StringVar()
        sb = Spinbox(
            frame2,
            values=[woordVar.get()[i] if x == ranNum else random.choice(ascii_lowercase) for x in range(5)],
            wrap=True,
            font=(14),
            width=5,
            textvariable=ansVar,
            )
        sb.configure(state='readonly')
        sb.place(relheight=0.2, relwidth=0.9 / len(woordVar.get()) , rely=0.4, relx=0.025 + (0.95 / len(woordVar.get()) * i))
        sbList.append(ansVar)
    submitButton = Button(frame2,text='stuur antwoord',command=checkAnswer)
    submitButton.place(rely=0.8,relx=0.42)

def checkAnswer():
    global score
    checkLetter=0
    for i in range(len(sbList)):
        if sbList[i].get() ==woordVar.get()[i]:
            checkLetter +=1
    if checkLetter==len(woordVar.get()):
        print('Gefeliciteerd')
    elif checkLetter!=woordVar.get()[i]:
        print("helaas, er zijn "+ str(checkLetter)+' letters goed')
        score -= 2*(woordVarLen-checkLetter)
        if score <= 0:
            fout =messagebox.askquestion(title='verloren',message='Je hebt verloren. opnieuw spelen?')
            if fout == 'yes':
                frame2.destroy()
                invulGenerator()
            elif fout == 'no':
                root.destroy()
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
root.geometry('500x330')
root.resizable(width=FALSE, height=FALSE)

invulGenerator()
root.mainloop()