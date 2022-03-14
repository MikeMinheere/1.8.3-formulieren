from itertools import count
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import random

#de list voor knoppen die je moet klikken
randomAction=['<space>','a','w','s','d','<Double-Button-1>','<Triple-Button-1>', '<Button-1>' ]

random.shuffle(randomAction)
score = 0
a = True
#hier word de score toegevoegd na een actie
def addScore():
    global score
    if randomAction[0] == '<Double-Button-1>' or randomAction[0] == '<Triple-Button-1>'or randomAction[0] == '<Button-1>':
        pressNumber.unbind(randomAction[0])
        score += 2
    else:root.unbind(randomAction[0]);score+=1

    random.shuffle(randomAction)

    #de plek van waar de scorecounter komt en waar de text word veranderd
    scoreLabel.place(x=840, y = 15)
    scoreLabel['text'] = score

    if randomAction[0] == '<Double-Button-1>':
        pressNumber['text'] = 'Double click'
    elif randomAction[0] == '<Triple-Button-1>':
        pressNumber['text'] = 'Triple click'
    elif randomAction[0] == '<Button-1>':
        pressNumber['text'] = 'Single click'
    elif randomAction[0] == '<space>':
        pressNumber['text'] = 'Press the space button'
    else: pressNumber['text'] = 'Press the '+randomAction[0]+' button'
    if a == True:
        trainer()

#de functie waarmee die opnieuw start
def opnieuw():
    global a
    a=False
    pressNumber.place(x=100000)
    opnieuwLabel.place(x=450, y=300, anchor=tk.CENTER)
    opnieuwLabel.config(text='your score was: '+str(score)+'\n play again?',)
    yes.place(relx=0.4,rely=0.7,anchor=tk.CENTER)
    yes.configure(command=yesClick)
    no.place(relx=0.6,rely=0.7,anchor=tk.CENTER)
    no.configure(command=noClick)

def countdown(aantalTijd):
    label.place(x=35, y=15)
    # verander de tektst in de label 
    label['text'] = str(aantalTijd)
    if aantalTijd > 0:
        # call de countdown opnieuw na 1 seconden
        root.after(1000, countdown, aantalTijd-1)
    elif aantalTijd == 0:
        opnieuw()

def tussenstap():
    startButton.place(x=10000,y=100000)
    pressNumber.pack()
    trainer()
    aantalTijd = int(tijd.get())
    countdown(aantalTijd)

def yesClick():
    global a,score
    a = True
    score = 0
    scoreLabel['text'] = score
    startButton.pack()
    startButton.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    opnieuwLabel.place(x=100000)
def noClick():
    root.destroy()

#de plek waar de gehele trainer in komt
def trainer():
    pressNumber.place(x= random.randint(0,730), y = random.randint(0,500))

    if randomAction[0] == '<Double-Button-1>': 
        pressNumber.bind('<Double-Button-1>',lambda event:addScore())
    elif randomAction[0] == '<Triple-Button-1>':
        pressNumber.bind('<Triple-Button-1>',lambda event:addScore())
    elif randomAction[0] == '<Button-1>':
        pressNumber.bind('<Button-1>',lambda event:addScore()) 
    else:root.bind(randomAction[0],lambda event:addScore())
    
def destroy():
    tijdButton.destroy()
    tijdEntry.destroy()
    
#dit is de configuration
root = tk.Tk()
root.geometry('900x600')
root.config(bg='light green')
root.title('FPS trainer')

#hier word de startknop gemaakt
startButton = tk.Button(
root,
bg='white',
text='start FPS trainer',
font=("Courier", 14)
)

#voor de score
scoreLabel = tk.Label(
root,
bg = 'light green',
font=('courier', 18)
)

#voor de timer
label = tk.Label(
root,
bg='light green',
font=('courier', 18)
)

#dit is de label die ik gebruik om de 'testen' uit te voeren.
pressNumber = tk.Label(
root,
bg='white',
text='random',
font=("Courier", 18),
borderwidth = 2,
relief="groove",
)

opnieuwLabel = tk.Label(
root,
bg='white',
width=30, 
height=10,
font=("Courier", 25),
borderwidth = 5,
relief="groove",
)

#de knoppen om opnieuw te spelen
yes = tk.Button(
opnieuwLabel,
bg='light green',
text='yes',
font=("Courier", 25)
)
no = tk.Button(
opnieuwLabel,
bg='light green',
text='no',
font=("Courier", 25)
)

tijd = tk.StringVar(value='20')
tijdEntry = ttk.Entry(
    root,
    textvariable=tijd
)
tijd
tijdEntry.pack(padx=50, pady=70)
tijdButton = ttk.Button(command=destroy)
tijdButton.pack()

#plek van de knop
startButton.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
startButton.configure(command=tussenstap)
scoreLabel.pack()
if randomAction[0] == '<Double-Button-1>':
    pressNumber['text'] = 'Double click'
elif randomAction[0] == '<Triple-Button-1>':
    pressNumber['text'] = 'Triple click'
elif randomAction[0] == '<Button-1>':
    pressNumber['text'] = 'Single click'
elif randomAction[0] == '<space>':
    pressNumber['text'] = 'Press the space button'
else: pressNumber['text'] = 'Press the '+randomAction[0]+' button'
root.mainloop()