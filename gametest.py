import json
import subprocess
import time
import tkinter
from tkinter import *
import random
import os
from tkinter import messagebox
import null

questions = []
answer_choice = []
answers = []

if (os.path.isfile('questions.txt') == True):
    fout = open("questions.txt", 'r')
    for line in fout:
        currentline = line.split(",")
        questions.append(currentline)
    fout.close


else:
    questions = [['is it hot today ?', 'easy'], ['what is Tkinter?', 'easy'], ["what's 1+2 ?", 'med'],
                 ['what is POO ?', 'hard']]
print("before: \n", questions)
print(len(questions))
#     -------------------------------------------*-----------------------------------------------
if (os.path.isfile('answer_choice.txt') == True):
    foutans = open("answer_choice.txt", 'r')
    answer_choice = foutans.read().splitlines()
    foutans.close


else:
    answer_choice = [["cold", "normal", "hot", "very hot", ],
                     ["framework", "API", "request", "library", ],
                     ["4", "3", "1", "0", ],
                     ["Object oriented programming ", "Proclamation Orienté Octé",
                      "Paralilisme Othorodental Olphactive", "Prolongation Octa Oreal", ], ]

# print(answer_choice)
# --------------------------------------------------ANSWERS
if (os.path.isfile('answers.txt') == True):
    foutansw = open("answers.txt", 'r')
    answers = foutansw.read().splitlines()
    foutansw.close


else:
    answers = [1, 3, 1, 0]

print("************questions*************")
print(questions)
print("****************answers***********")
print(answers)
print("***********************")
print(answer_choice)
"""
data = {}
questions = []
answer_choice = []
answers = []
with open("quiz.json") as file:
    data = json.load(file)

print(data)
for d in data:
    questions.append(d["question"])
    answer_choice.append(d["answers"])
    answers.append(d["correctIndex"])


"""

# print(answers)
# --------------SHUFFLE QUESTIONS
c = list(zip(questions, answer_choice, answers))

random.shuffle(c)

questions, answer_choice, answers = zip(*c)

# ---------------
print("after: \n", questions)

qu = []
qu1 = []
qu2 = []
for q in c:
    if ("easy" in q[0][1]):
        qu.append(q)

for q in c:
    if ("med" in q[0][1]):
        qu1.append(q)
for q in c:
    if ("hard" in q[0][1]):
        qu2.append(q)
# ------------------------------------------------------------------CHOOSE PERCENTAGE OF EACH DIFFICULTY----
if (os.path.isfile('percentage.txt') == True):
    foutansw = open("percentage.txt", 'r')
    per = foutansw.read().splitlines()
    foutansw.close


else:
    per = [50, 30, 50]

easy = int(per[0])
medium = int(per[1])
hard = int(per[2])

percent_easy = (len(qu) * easy) / 100
percent_easy = int(percent_easy)
percent_med = (len(qu1) * medium) / 100
percent_med = int(percent_med)
percent_hard = (len(qu2) * hard) / 100
percent_hard = int(percent_hard)

print("percentage of easy :", percent_easy)
print("percentage of med :", percent_med)
print("percentage of hard :", percent_hard)
q0 = []
q1 = []
q2 = []
for q in c:
    if ("easy" in q[0][1]):
        q0.append(q)
    if (len(q0) == percent_easy):
        break
for q in c:
    if ("med" in q[0][1]):
        q1.append(q)
    if (len(q1) == percent_med):
        break
for q in c:
    if ("hard" in q[0][1]):
        q2.append(q)
    if (len(q2) == percent_hard):
        break

print("easy :", len(q0))
print("medium :", len(q1))
print("hard :", len(q2))

z = tuple(q0) + tuple(q1) + tuple(q2)
# print("this is z :\n",z)
# print(len(z))
questions, answer_choice, answers = zip(*z)
# print(questions)
# print(answer_choice)
# print(answers)
question = []
for r in range(len(questions)):
    question.append(questions[r][0])

questions = question
# print(questions)
# print(answer_choice)
ap = []
for r in range(len(answer_choice)):
    a = list(answer_choice[r].split(","))
    ap.append(a)
print(ap)
answer_choice = tuple(ap)
print("---------------------")
print(questions)
print(answer_choice)
print(answers)
ra = []
for r in answers:
    ra.append(eval(r))
ra = tuple(ra)
print(ra)
answers = ra
print("lengh of question:", len(questions))
# ------------------------------------------------------------------------------------------------------------

user_answer = []
indexes = []


def gen():
    global indexes
    while (len(indexes) < len(questions)):
        x = random.randint(0, len(questions) - 1)
        indexes.append(x)
        if x in indexes:
            continue
        else:
            indexes.append(x)


from tkinter import ttk


def showresult(score):
    global answer_choice, questions, user_answer
    label4text.destroy()
    label3text.destroy()
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()

    labelimage = Label(root, border=0, background="#ffffff")
    # labelimage.pack(pady=(10,10))

    labelresulttext = Label(root, font=("arial", 20), background="#fcfdce")
    labelresulttext.pack(pady=(10, 10))
    labelscore = Label(root, font=("arial", 20))
    labelresulttext.pack()
    # -------------------FRAME TABLE------------------------------------------------
    game_frame = Frame(root, width=300, height=50)
    game_frame.pack(fill="both", expand=1)

    # scrollbar
    game_scroll = Scrollbar(game_frame)
    game_scroll.pack(side=RIGHT, fill=Y)

    game_scroll = Scrollbar(game_frame, orient='horizontal')
    game_scroll.pack(side=BOTTOM, fill=X)

    my_game = ttk.Treeview(game_frame, yscrollcommand=game_scroll.set, xscrollcommand=game_scroll.set, )

    my_game.place(x=0, y=0)

    game_scroll.config(command=my_game.yview)
    game_scroll.config(command=my_game.xview)

    # define our column

    my_game['columns'] = ('Id', 'Questions', 'Votre Reponse', 'La Vrai Reponse')

    # format our column
    my_game.column("#0", width=0, stretch=NO)
    my_game.column("Id", anchor=CENTER, width=100)
    my_game.column("Questions", anchor=CENTER, width=180)
    my_game.column("Votre Reponse", anchor=CENTER, width=200)
    my_game.column("La Vrai Reponse", anchor=CENTER, width=200)
    # Create Headings
    my_game.heading("#0", text="", anchor=CENTER)
    my_game.heading("Id", text="Id", anchor=CENTER)
    my_game.heading("Questions", text="Questions", anchor=CENTER)
    my_game.heading("Votre Reponse", text="Votre Reponse", anchor=CENTER)
    my_game.heading("La Vrai Reponse", text="La Vrai Reponse", anchor=CENTER)

    for i in range(len(user_answer)):
        if (user_answer[i] == 5):
            my_game.insert(parent='', index='end', iid=i, text='',
                           values=(i, questions[i], 'NULL', answer_choice[i][answers[i]]))
        else:
            my_game.insert(parent='', index='end', iid=i, text='',
                           values=(i, questions[i], answer_choice[i][user_answer[i]], answer_choice[i][answers[i]]))

    # label0=Label(root,font=("arial",15),text="QUESTIONS",border=0,background="#ffffff")
    # label0.place(x=20,y=100)

    print("user answers:", user_answer)
    btn4.pack()

    if score >= 20:
        img = ""  # PhotoImage(file="win.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You are Perfect !" + "\n \n Votre Score est : " + str(score))


    elif score < 20 and score >= 10:
        img = ""  # PhotoImage(file="win.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You are not BAD !" + "\n\n Votre Score est : " + str(score))

    else:
        img = ""  # PhotoImage(file="lose.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You are so BAD !" + "\n\n Votre Score est : " + str(score))


def calc():
    global indexes, user_answer, answers, ques, is_done
    x = 0
    global score
    score = 0
    r = 0
    if (len(user_answer) != len(answers)):
        for r in range(len(answers) - len(user_answer)):
            user_answer.append(5)
            r += 1
            if (r == len(answers)):
                break

    print("this is user answers", user_answer)
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 5
            x += 1

    print("votre score est :", score)
    x += 1
    showresult(score)


ques = 1
is_done = False


def selected():
    global radiovar, user_answer, is_done
    global lblQuestion, r1, r2, r3, r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    if ques < len(questions):
        lblQuestion.config(text=questions[indexes[ques]])
        r1["text"] = answer_choice[indexes[ques]][0]
        r2["text"] = answer_choice[indexes[ques]][1]
        r3["text"] = answer_choice[indexes[ques]][2]
        r4["text"] = answer_choice[indexes[ques]][3]
        ques += 1
    else:
        textbtn.set("BACK TO MENU")
        print(indexes)
        print(user_answer)
        print(student_id.get())
        calc()
        is_done = True
    if (ques <= 1):
        textbtn.set("BACK TO MENU")
    else:
        textbtn.set("BACK")


def questionback():
    global radiovar, user_answer
    global lblQuestion, r1, r2, r3, r4
    global ques
    print("this is ques inside back:", ques)
    quest = ques - 2
    if (ques <= 1):
        textbtn.set("BACK TO MENU")
        root.destroy()
        subprocess.call(["python", "gametest.py"])
    else:
        if ques < len(questions):
            lblQuestion.config(text=questions[indexes[quest]])
            r1["text"] = answer_choice[indexes[quest]][0]
            r2["text"] = answer_choice[indexes[quest]][1]
            r3["text"] = answer_choice[indexes[quest]][2]
            r4["text"] = answer_choice[indexes[quest]][3]
            ques -= 1
        else:
            # print(indexes)
            # print(user_answer)
            # print(student_id.get())
            # calc()
            root.destroy()
            subprocess.call(["python", "gametest.py"])


def startQuiz():
    global lblQuestion, r1, r2, r3, r4, textbtn, btn, ques
    # Wraplength 400 sonrasına yazma aşağıya yaz der !<3
    lblQuestion = Label(root, text=questions[indexes[0]], font=("arial", 15, "bold"), width=500, justify="center",
                        wraplength=400, background="#1e7fc2")
    lblQuestion.pack(pady=(100, 30))
    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)
    r1 = Radiobutton(root, text=answer_choice[indexes[0]][0],
                     font=("arial", 12), value=0, variable=radiovar,
                     command=selected, background="#a0fa4c")
    r1.pack()
    r2 = Radiobutton(root, text=answer_choice[indexes[0]][1],
                     font=("arial", 12), value=1, variable=radiovar, command=selected, background="#f4ca60")
    r2.pack()
    r3 = Radiobutton(root, text=answer_choice[indexes[0]][2],
                     font=("arial", 12), value=2, variable=radiovar, command=selected, background="#37d3ff")
    r3.pack()
    r4 = Radiobutton(root, text=answer_choice[indexes[0]][3],
                     font=("arial", 12), value=3, variable=radiovar, command=selected, background="Orange")
    r4.pack()
    textbtn = tkinter.StringVar()
    btn = Button(root, textvariable=textbtn,
                 font=("arial", 12),
                 command=questionback, width=20, height=2, background="#FFFF00")
    btn.pack(pady=(80, 0))
    textbtn.set("BACK")
    if (ques <= 1):
        textbtn.set("BACK TO MENU")
    else:
        textbtn.set("BACK")
    btn.pack()


def startIsPressed():
    global label4text
    global label3text
    global textlabel
    label4text = Label(root, text="Name:" + name.get(), font=("arial", 10, "bold"), background="#000000",
                       foreground="#FACA2F")
    label4text.place(x=10, y=10)
    label3text = Label(root, text="Student ID:" + student_id.get(), font=("arial", 10, "bold"), background="#000000",
                       foreground="#FACA2F")
    label3text.place(x=180, y=10)

    textlabel = tkinter.StringVar()
    label5text = Label(root, textvariable=textlabel, font=("arial", 10, "bold"), background="#000000",
                       foreground="#FACA2F")
    label5text.place(x=500, y=10)

    timer()
    root.update()

    # labelimg.destroy()
    labeltext.destroy()
    labeltext2.destroy()
    lblInstruction.destroy()
    btnStart.destroy()
    lblRules.destroy()
    entry1.destroy()
    entry2.destroy()
    btn3.destroy()
    gen()
    startQuiz()


root = Tk()
root.title("Quiz")
root.geometry("700x600")
root.config(background="#ffffff")
root.resizable(0, 0)

# -------------------------------------------------IMAGE BACKGROUND-----------------------------------------------
from PIL import Image, ImageTk

# Create a photoimage object of the image in the path
image1 = Image.open("jack3.jpg")
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test

# Position image
label1.place(x=0, y=0)
# -----------------------------------------------------------------------------------


# img1=""#PhotoImage(file="rsz_quizz.png")
#
# labelimg=Label(root,image=img1,background="#ffffff")
# labelimg.pack(pady=(40,0))

name = StringVar()
student_id = StringVar()

labeltext = Label(root, text="Full Name ", font=("arial", 13, "bold"), background="#ffffff")
labeltext.place(x=220, y=50)
entry1 = Entry(root, textvariable=name, font=("arial", 10), width=15, bg="white")
entry1.place(x=210, y=80)

labeltext2 = Label(root, text="Student ID", font=("arial", 13, "bold"), background="#ffffff")
labeltext2.place(x=390, y=50)
entry2 = Entry(root, textvariable=student_id, font=("arial", 10), width=15, bg="white")
entry2.place(x=380, y=80)

img2 = PhotoImage(file="start6.png")

btnStart = Button(root, image=img2, relief=FLAT, border=0, background="#ffffff", command=startIsPressed)
btnStart.pack(pady=(120, 0))


def to_adminside():
    root.destroy()
    subprocess.call(["python", "InputAdmin.py"])


lblInstruction = Label(root, text="Read The Rules Below and\n Click Start When You Ready", background="#ffffff",
                       font=("Concolas", 14), justify="center")
lblInstruction.pack(pady=(15, 30))

lblRules = Label(root,
                 text="Each Question you answer correctly gives you 5 points ! \n You have 30s to finish the quiz."
                 , width=100, font=("Times", 14), background="#000000", foreground="#FACA2F")
lblRules.pack()
btn4 = Button(root, text="Exit", font=("arial", 10), width=20, height=2, bg="#87409f", activebackground="#FF0000",
              command=root.destroy)
btn4.place(x=260, y=550)
btn3 = Button(root, text="ADMIN SIDE ", font=("Algerian", 10), width=20, height=2, bg="#f7c053",
              activebackground="#eed344", command=to_adminside)
btn3.place(x=20, y=200)

cpt = 30


def timer():
    global cpt, textlabel, is_done
    cpt -= 1
    textlabel.set(cpt)
    if cpt == 0:
        messagebox.showwarning('QUIZ', 'time is UP')
        if (is_done == False):
            print(indexes)
            print(user_answer)
            print(student_id.get())
            calc()
        return;
    root.after(1000, lambda: timer())


root.mainloop()
