
import tkinter as tk
from tkinter import Label, Entry, Button,Listbox, Scrollbar, Frame, VERTICAL,END, Toplevel, StringVar
from PIL import ImageTk, Image
import sqlite3

con = sqlite3.connect('chatbot.db')


class Chatbot(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master = master
        self.load_gui()
        self.e1 = StringVar()
        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Chatbote(Chat TEXT)")

    def load_gui(self):
        self.label2 = Label(self.master, text='Hi! I am Sita, your personal chatbot.', font=("Phosphate", 35),
                            bg='#5cd9db', fg='#5670C2')
        self.label2.grid(row=2, column=1)
        self.label1 = Label(self.master, text='How can I help you?', font=("Phosphate", 35), bg='#5cd9db', fg='#5670C2')
        self.label1.grid(row=3, column=1)
        self.button1 = Button(self.master, text='Lets chat', highlightbackground='#5670C2', width=12, height=2,
                              command=lambda: self.Letchat())
        self.button_quit = Button(self.master, text="No,Chat Later", width=12, height=2, highlightbackground='#5670C2',
                                  command=lambda: self.close())
        self.my_img = ImageTk.PhotoImage(Image.open("chatbot.png"))
        self.my_label = Label(root, image=self.my_img, background="#5cd9db")
        self.my_label.grid(row=1, column=1, sticky='nsew')

        self.button_quit.grid(row=5, column=1)
        self.button1.grid(row=4, column=1)

    def close(self):
        self.master.destroy()

    def Letchat(self):
        x1 = Toplevel(root)

        self.chat1 = Entry(x1, width=53, text='')
        self.chat1.grid(row=14, column=1, sticky='s')
        x1.geometry('1013x700')
        self.button = Button(x1, highlightbackground='#f0d8ef', width=10, height=2, text="Chat",
                             command=lambda: self.add())
        self.button.grid(row=15, column=1, sticky='w')
        self.scrollbar1 = Scrollbar(x1, orient=VERTICAL)
        self.lstList1 = Listbox(x1, background="#8EC7F5", fg="black", selectbackground="#b9cced", highlightcolor="Red",
                                width=54, height=36, exportselection=0, yscrollcommand=self.scrollbar1.set)
        self.lstList1.place(relx=0.5, rely=0.5, anchor="e")
        self.lstList1.grid(row=0, column=1)
        self.scrollbar1.config(command=self.lstList1.yview)
        self.scrollbar1.grid(row=1, column=13, rowspan=7, columnspan=12, sticky='nes')
        self.lstList1.grid(row=0, column=1, rowspan=5, columnspan=10, sticky='nw')
        self.greetings = {'hi': 'hey', 'hola': 'hello', 'namaste': 'Namaste', 'kaise ho cutie': 'mast',
                          'aur kya haal': 'bole to jhakaaaaas', 'Hi Sita': 'Namaste',
                          'How you doing': 'Well, I am just trying to stay positive in this Lockdown',
                          'Whats up': 'Just Corona going around', 'What are you upto these days': ' GOOOO CORONA!!!',
                          'Aur kya haal': 'Trying to upgrade myself in this 21 days lockdown period',
                          'Where am I': 'You are in Mumbai', 'What is my location': 'You are in kanpur',
                          'What is this place': 'You are in the City of Dreams',
                          'What does Modiji say': 'Jaha Ho Wahi Raho',
                          'What does doctor advice for COVID-19': 'Wash your hands every hour for 20 seconds',
                          'Corona': 'GOOOOO',
                          'Whats the latest news': 'Dont you know, COVID-19 has been declared as Pandemic by WHO',
                          'What is COVID-19': 'COVID-19 is a new illness that affects your lungs and airways. It is'
                                              ' caused by a virus called coronavirus.',
                          'What are the precuations can we take for COVID-19': 'Regularly and thoroughly clean your'
                            ' hands with an alcohol-based hand rub or wash them with soap and water. If you are the one'
                            ' feeling sick, cover your entire mouth and nose when you cough or sneeze.Stay informed on'
                            ' the latest developments about COVID-19. Follow advice given by your healthcare provider,'
                            ' your national and local public health authority or your employer on how to protect '
                            'yourself and others from COVID-19.',
                          'What are the symptoms': 'Early symptoms include fever, dry cough,and fatique.',
                          'How can we defeat Coronavirus': 'Most important, practice social distancing.Avoid touching'
                            ' eyes, nose and mouth. And until the situations becomes better, STAY HOME!'}
        self.image = Image.open('chatbot1.png')
        self.image = self.image.resize((500, 500), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.label = Label(x1, bg='#D36C6C', image=self.photo)
        self.label.image = self.photo
        self.label.grid(row=3)
        x1.configure(background='#D36C6C')

    def add(self):
        for item in [self.chat1.get()]:
            if item == 'hola' or item == 'hi' or item == 'namaste' or item == 'How you doing' or item == 'Whats up' or \
                    item == 'kaise ho' or item == 'aur kya haal' or item == 'where am i' or item == 'whats my location'\
                    or item == 'what is this place' or item == 'Hi Sita' or item == 'Whats up' or \
                    item == 'What are you upto these days' or item == 'Aur kya haal' or item == 'Where am I' or \
                    item == 'What is my location' or item == 'What is this place' or item == 'Where am I' or \
                    item == 'What is this place' or item == 'What does Modiji say' or item == 'What does doctor advise'\
                    or item == 'What precuations can we take' or item == 'How can we defeat Coronavirus':
                self.lstList1.insert(END, str('HUMAN:'), str(self.chat1.get()), str('SITA:'),
                                     str(self.greetings.get(str(self.chat1.get()))))
            else:
                return 0
        with con:
            cur = con.cursor()
            cur.execute("INSERT INTO Chatbote VALUES(?)", (str(self.chat1.get()),))
            cur.execute("INSERT INTO Chatbote VALUES(?)", (str(self.greetings.get(self.chat1.get())),))
            cur.execute("SELECT * FROM Chatbote")
            rows = cur.fetchall()
            print(rows)


if __name__ == "__main__":
    root = tk.Tk()
    c = Chatbot(root)
    root.configure(background="#5cd9db")
    root.geometry('640x700')
    root.title("Sita- The ChatBot")
    root.mainloop()
