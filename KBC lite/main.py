from tkinter import *
from tkinter.ttk import Progressbar
from pygame import mixer
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

mixer.init()

mixer.music.load('kbc.mp3')
mixer.music.play()

questions = ["Which is the largest country in the world?",
             "How many days are there in a leap year?",
             "Which one of these four birds has the longest beak and feet?",
             "What is the national currency of the United States of America (USA)?",
             "Guido van Rossum in 1991 designed which language?",
             "Finish the sequence: 9, 18, 27, _?",
             "Which one is the first fully supported 64-bit operating system?",
             "Which animal is called the king of the jungle?",
             "what time corresponds to 23:23 hours ?",
             "Which team has won most number of IPL matches ?",
             "Which is the largest planet in our Solar system?",
             "How many continents are there in the world?",
             "How many years are there in one Millenium?",
             "ipad is manufactured by?",
             "Who founded Microsoft?"]

first_option = ["India", "354",
                "Heron", "Euro",
                "Javascript", "36",
                "Windows 7", "Elephant", "11:23PM", "KKR",
                "Earth", "8",
                "100 years", "Google", "Monty Ritz"]

second_option = ["USA", "366",
                 "Parrot", "Peso ",
                 "Python", "34",
                 "Linux", "Lion", "11.11PM", "CSK",
                 "Uranus", "5",
                 "50 years",
                 "Microsoft", "Danis Lio"]

third_option = ["China", "365",
                "Crow", "Dollar",
                "Java", "30",
                "Mac", "Tiger", "7:23PM", "MI",
                "Mars", "7",
                "500 years",
                "Amazon", "Bill Gates"]

fourth_option = ["Russia", "420",
                 "Pigeon", "Yen",
                 "C++", "37",
                 "Windows XP", "Cow", "9.11PM", "RCB",
                 "Jupiter",
                 "6",
                 "1000 years", "Apple",
                 "Jeff Bezos"]

correct_answers = ["Russia", "366", "Heron", "Dollar", "Python", "36",
                   "Linux", "Lion", "11:23PM", "MI", "Jupiter", "7", "1000 years", "Apple",
                   "Bill Gates"]


def select(event):
    callButton.place_forget()
    progressbarA.place_forget()
    progressbarB.place_forget()
    progressbarC.place_forget()
    progressbarD.place_forget()

    progressbarLabelA.place_forget()
    progressbarLabelB.place_forget()
    progressbarLabelC.place_forget()
    progressbarLabelD.place_forget()

    b = event.widget
    value = b['text']
    for i in range(15):
        if value == correct_answers[i]:
            if value == correct_answers[14]:
                amountLabel.config(image=amountImage15)
                def close():
                    root2.destroy()
                    root.destroy()

                def playagain():
                    lifeline50Button.config(state=NORMAL, image=image50)
                    audiencePoleButton.config(state=NORMAL, image=audiencePole)
                    phoneLifelineButton.config(state=NORMAL, image=phoneImage)

                    root2.destroy()
                    questionArea.insert(END, questions[0])

                    optionButton1.config(text=first_option[0])
                    optionButton2.config(text=second_option[0])
                    optionButton3.config(text=third_option[0])
                    optionButton4.config(text=fourth_option[0])
                    amountLabel.config(image=amountImage0)

                mixer.music.stop()
                mixer.music.load('Kbcwon.mp3')
                mixer.music.play()

                root2 = Toplevel()
                root2.overrideredirect(True)
                root2.config(bg='black')
                root2.geometry('560x400+440+130')
                root2.title('you won 0 pound')
                imgLabel = Label(root2, image=centreImage, bd=0)
                imgLabel.pack(pady=30)

                loseLabel = Label(root2, text='You Won', font=('arial', 20, 'bold'), bg='black', fg='white')
                loseLabel.pack()

                playagainButton = Button(root2, text='Play Again', font=('arial', 20, 'bold'), bg='black', fg='white',
                                         activebackground='black', activeforeground='white', bd=0, cursor='hand2',
                                         command=playagain)
                playagainButton.pack()

                closeButton = Button(root2, text='Close', font=('arial', 20, 'bold'), bg='black', fg='white',
                                     activebackground='black', activeforeground='white', bd=0, cursor='hand2',
                                     command=close)
                closeButton.pack()

                happyImage = PhotoImage(file='happy.png')
                happyLabel = Label(root2, image=happyImage, bg='black')
                happyLabel.place(x=80, y=280)

                happyLabel1 = Label(root2, image=happyImage, bg='black')
                happyLabel1.place(x=400, y=280)

                root2.mainloop()
                break

            questionArea.delete(1.0, END)
            questionArea.insert(END, questions[i+1])

            optionButton1.config(text=first_option[i+1])
            optionButton2.config(text=second_option[i+1])
            optionButton3.config(text=third_option[i+1])
            optionButton4.config(text=fourth_option[i+1])
            amountLabel.config(image=amountImage[i])

        if value not in correct_answers:
            def close():
                root1.destroy()
                root.destroy()

            def tryagain():
                lifeline50Button.config(state=NORMAL, image=image50)
                audiencePoleButton.config(state=NORMAL, image=audiencePole)
                phoneLifelineButton.config(state=NORMAL, image=phoneImage)

                root1.destroy()
                questionArea.insert(END, questions[0])

                optionButton1.config(text=first_option[0])
                optionButton2.config(text=second_option[0])
                optionButton3.config(text=third_option[0])
                optionButton4.config(text=fourth_option[0])
                amountLabel.config(image=amountImage0)

            root1 = Toplevel()
            root1.overrideredirect(True)
            root1.config(bg='black')
            root1.geometry('560x400+440+130')
            root1.title('you won 0 pound')
            imgLabel = Label(root1, image=centreImage, bd=0)
            imgLabel.pack(pady=30)

            loseLabel = Label(root1, text='You Lose', font=('arial', 20, 'bold'), bg='black', fg='white')
            loseLabel.pack()

            tryagainButton = Button(root1, text='Try Again', font=('arial', 20, 'bold'), bg='black', fg='white',
                                    activebackground='black', activeforeground='white', bd=0, cursor='hand2',
                                    command=tryagain)
            tryagainButton.pack()

            closeButton = Button(root1, text='Close', font=('arial', 20, 'bold'), bg='black', fg='white',
                                 activebackground='black', activeforeground='white', bd=0, cursor='hand2',
                                 command=close)
            closeButton.pack()

            sadImage = PhotoImage(file='sad.png')
            sabLabel = Label(root1, image=sadImage, bg='black')
            sabLabel.place(x=80, y=280)

            sabLabel1 = Label(root1, image=sadImage, bg='black')
            sabLabel1.place(x=400, y=280)

            root1.mainloop()
            break

def lifeline50():
    lifeline50Button.config(image=image50x, state=DISABLED)

    if questionArea.get(1.0, 'end-1c') == questions[0]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[1]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[2]:
        optionButton3.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[3]:
        optionButton2.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[4]:
        optionButton3.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[5]:
        optionButton2.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[6]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[7]:
        optionButton3.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[8]:
        optionButton2.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[9]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[10]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[11]:
        optionButton1.config(text='')
        optionButton2.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[12]:
        optionButton1.config(text='')
        optionButton2.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[13]:
        optionButton2.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[14]:
        optionButton1.config(text='')
        optionButton4.config(text='')

def audiencePolelifeline():
    audiencePoleButton.config(image=image50x, state=DISABLED)

    progressbarA.place(x=580, y=190)
    progressbarB.place(x=620, y=190)
    progressbarC.place(x=660, y=190)
    progressbarD.place(x=700, y=190)

    progressbarLabelA.place(x=580, y=320)
    progressbarLabelB.place(x=620, y=320)
    progressbarLabelC.place(x=660, y=320)
    progressbarLabelD.place(x=700, y=320)

    if questionArea.get(1.0, 'end-1c') == questions[0]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=60)
        progressbarD.config(value=90)

    if questionArea.get(1.0, 'end-1c') == questions[1]:
        progressbarA.config(value=20)
        progressbarB.config(value=80)
        progressbarC.config(value=50)
        progressbarD.config(value=40)

    if questionArea.get(1.0, 'end-1c') == questions[2]:
        progressbarA.config(value=80)
        progressbarB.config(value=60)
        progressbarC.config(value=50)
        progressbarD.config(value=70)

    if questionArea.get(1.0, 'end-1c') == questions[3]:
        progressbarA.config(value=30)
        progressbarB.config(value=70)
        progressbarC.config(value=90)
        progressbarD.config(value=50)

    if questionArea.get(1.0, 'end-1c') == questions[4]:
        progressbarA.config(value=30)
        progressbarB.config(value=80)
        progressbarC.config(value=40)
        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c') == questions[5]:
        progressbarA.config(value=80)
        progressbarB.config(value=10)
        progressbarC.config(value=40)
        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c') == questions[6]:
        progressbarA.config(value=30)
        progressbarB.config(value=80)
        progressbarC.config(value=20)
        progressbarD.config(value=40)

    if questionArea.get(1.0, 'end-1c') == questions[7]:
        progressbarA.config(value=10)
        progressbarB.config(value=70)
        progressbarC.config(value=50)
        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c') == questions[8]:
        progressbarA.config(value=90)
        progressbarB.config(value=80)
        progressbarC.config(value=70)
        progressbarD.config(value=20)

    if questionArea.get(1.0, 'end-1c') == questions[9]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=70)
        progressbarD.config(value=60)

    if questionArea.get(1.0, 'end-1c') == questions[10]:
        progressbarA.config(value=40)
        progressbarB.config(value=20)
        progressbarC.config(value=50)
        progressbarD.config(value=70)

    if questionArea.get(1.0, 'end-1c') == questions[11]:
        progressbarA.config(value=30)
        progressbarB.config(value=80)
        progressbarC.config(value=90)
        progressbarD.config(value=40)

    if questionArea.get(1.0, 'end-1c') == questions[12]:
        progressbarA.config(value=20)
        progressbarB.config(value=60)
        progressbarC.config(value=50)
        progressbarD.config(value=80)

    if questionArea.get(1.0, 'end-1c') == questions[13]:
        progressbarA.config(value=60)
        progressbarB.config(value=35)
        progressbarC.config(value=40)
        progressbarD.config(value=80)

    if questionArea.get(1.0, 'end-1c') == questions[14]:
        progressbarA.config(value=60)
        progressbarB.config(value=65)
        progressbarC.config(value=90)
        progressbarD.config(value=80)

def phoneLifeline():
    mixer.music.load('calling.mp3')
    mixer.music.play()
    callButton.place(x=70, y=260)
    phoneLifelineButton.config(image=phoneImagex, state=DISABLED)

def phoneClick():
    for i in range(15):
        if questionArea.get(1.0, 'end-1c') == questions[i]:
            engine.say(f'the answer is {correct_answers[i]}')
            engine.runAndWait()

root = Tk()

root.geometry('1270x652+300+100')
root.overrideredirect(True)
# root.title('Who Wants To Be A Millionaire')
root.resizable(False, False)
root.config(bg='black')

leftFrame = Frame(root, bg='black', padx=90)
leftFrame.grid(row=0, column=0)

rightFrame = Frame(root, bg='black', padx=50, pady=25)
rightFrame.grid(row=0, column=1)

topFrame = Frame(leftFrame, bg='black', pady=15)
topFrame.grid(row=0, column=0)

middleFrame = Frame(leftFrame, bg='black', pady=15)
middleFrame.grid(row=1, column=0)

bottomFrame = Frame(leftFrame, bg='black')
bottomFrame.grid(row=2, column=0)

image50 = PhotoImage(file='50-50.png')
image50x = PhotoImage(file='50-50-X.png')
lifeline50Button = Button(topFrame, image=image50, bd=0, bg='black', cursor='hand2', activebackground='black',
                          width=180, height=80, command=lifeline50)
lifeline50Button.grid(row=0, column=0)

audiencePole = PhotoImage(file='audiencePole.png')
audiencePolex = PhotoImage(file='audiencePoleX.png')
audiencePoleButton = Button(topFrame, image=audiencePole, bd=0, bg='black', cursor='hand2', activebackground='black',
                            width=180, height=80, command=audiencePolelifeline)
audiencePoleButton.grid(row=0, column=1)

phoneImage = PhotoImage(file='phoneAFriend.png')
phoneImagex = PhotoImage(file='phoneAFriendX.png')
phoneLifelineButton = Button(topFrame, image=phoneImage, bd=0, bg='black', cursor='hand2', activebackground='black',
                             width=180, height=80, command=phoneLifeline)
phoneLifelineButton.grid(row=0, column=2)

callimage = PhotoImage(file='phone.png')
callButton = Button(root, image=callimage, bd=0, bg='black', activebackground='black', cursor='hand2',
                    command=phoneClick)

centreImage = PhotoImage(file='center.png')
logoLabel = Label(middleFrame, image=centreImage, bd=0, width=300, height=200, bg='black')
logoLabel.grid(row=0, column=0)

amountImage0 = PhotoImage(file='Picture0.png')
amountImage1 = PhotoImage(file='Picture1.png')
amountImage2 = PhotoImage(file='Picture2.png')
amountImage3 = PhotoImage(file='Picture3.png')
amountImage4 = PhotoImage(file='Picture4.png')
amountImage5 = PhotoImage(file='Picture5.png')
amountImage6 = PhotoImage(file='Picture6.png')
amountImage7 = PhotoImage(file='Picture7.png')
amountImage8 = PhotoImage(file='Picture8.png')
amountImage9 = PhotoImage(file='Picture9.png')
amountImage10 = PhotoImage(file='Picture10.png')
amountImage11 = PhotoImage(file='Picture11.png')
amountImage12 = PhotoImage(file='Picture12.png')
amountImage13 = PhotoImage(file='Picture13.png')
amountImage14 = PhotoImage(file='Picture14.png')
amountImage15 = PhotoImage(file='Picture15.png')

amountImage = [amountImage1, amountImage2, amountImage3, amountImage4, amountImage5, amountImage6, amountImage7,
               amountImage8, amountImage9, amountImage10, amountImage11, amountImage12, amountImage13, amountImage14,
               amountImage15]

amountLabel = Label(rightFrame, image=amountImage0, bg='black')
amountLabel.grid(row=0, column=0)

layoutImage = PhotoImage(file='lay.png')
layoutLabel = Label(bottomFrame, image=layoutImage, bg='black')
layoutLabel.grid(row=0, column=0)

questionArea = Text(bottomFrame, bg='black', fg='white', width=34, height=2, wrap='word', bd=0,
                    font=('arial', 18, 'bold'))
questionArea.place(x=70, y=10)
questionArea.insert(END, questions[0])

labelA = Label(bottomFrame, text='A:', bg='black', fg='white', font=('arial', 16, 'bold'))
labelA.place(x=60, y=110)

optionButton1 = Button(bottomFrame, text=first_option[0], bg='black', fg='white', cursor='hand2', bd=0,
                       activebackground='black', activeforeground='white', font=('arial', 18, 'bold'))
optionButton1.place(x=100, y=100)

labelB = Label(bottomFrame, text='B:', bg='black', fg='white', font=('arial', 16, 'bold'))
labelB.place(x=330, y=110)

optionButton2 = Button(bottomFrame, text=second_option[0], bg='black', fg='white', cursor='hand2', bd=0,
                       activebackground='black', activeforeground='white', font=('arial', 18, 'bold'))
optionButton2.place(x=370, y=100)

labelC = Label(bottomFrame, text='C:', bg='black', fg='white', font=('arial', 16, 'bold'))
labelC.place(x=60, y=190)

optionButton3 = Button(bottomFrame, text=third_option[0], bg='black', fg='white', cursor='hand2', bd=0,
                       activebackground='black', activeforeground='white', font=('arial', 18, 'bold'))
optionButton3.place(x=100, y=180)

labelD = Label(bottomFrame, text='D:', bg='black', fg='white', font=('arial', 16, 'bold'))
labelD.place(x=330, y=190)

optionButton4 = Button(bottomFrame, text=fourth_option[0], bg='black', fg='white', cursor='hand2', bd=0,
                       activebackground='black', activeforeground='white', font=('arial', 18, 'bold'))
optionButton4.place(x=370, y=180)

progressbarA = Progressbar(root, orient=VERTICAL, length=120)
progressbarB = Progressbar(root, orient=VERTICAL, length=120)
progressbarC = Progressbar(root, orient=VERTICAL, length=120)
progressbarD = Progressbar(root, orient=VERTICAL, length=120)

progressbarLabelA = Label(root, text='A', font=('arial', 20, 'bold'), bg='black', fg='white')
progressbarLabelB = Label(root, text='B', font=('arial', 20, 'bold'), bg='black', fg='white')
progressbarLabelC = Label(root, text='C', font=('arial', 20, 'bold'), bg='black', fg='white')
progressbarLabelD = Label(root, text='D', font=('arial', 20, 'bold'), bg='black', fg='white')

optionButton1.bind('<Button-1>', select)
optionButton2.bind('<Button-1>', select)
optionButton3.bind('<Button-1>', select)
optionButton4.bind('<Button-1>', select)

root.mainloop()
