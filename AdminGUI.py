import json
import subprocess
import tkinter as tk
from tkinter import messagebox, IntVar

import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class AdminGUI(ttk.Window):
    APP_NAME = "Quize Game - Admin"
    WIDTH = 900
    HEIGHT = 570

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title(AdminGUI.APP_NAME)
        self.geometry(str(AdminGUI.WIDTH) + "x" + str(AdminGUI.HEIGHT))
        self.minsize(AdminGUI.WIDTH, AdminGUI.HEIGHT)
        self.resizable(False, False)

        self.id_question = IntVar()
        self.data = []

        self.head_frame = ttk.Labelframe(bootstyle="secondary", master=self, width=AdminGUI.WIDTH-50, height=60)
        self.head_frame.place(relx=0.98, rely=0.05, anchor=tk.E)
        left_frame = ttk.Labelframe(bootstyle="secondary", master=self, width=320, height=AdminGUI.HEIGHT - 70,
                                    text="Questions")
        left_frame.place(relx=0.432, rely=0.55, anchor=tk.E)
        right_frame = ttk.Labelframe(bootstyle="info", master=self, width=450, height=AdminGUI.HEIGHT - 75,
                                     text="Opérations")
        right_frame.place(relx=0.98, rely=0.55, anchor=tk.E)



        self.back = ttk.ttk.Button(master=self.head_frame, text="Back", bootstyle="light", width=10, command=self.retourner)
        self.back.place(relx=0.1, rely=0.3, anchor=CENTER)


        self.easy_percent = ttk.Entry(master=self.head_frame,bootstyle="secondary", width=5)
        self.easy_percent.insert(0, "0")
        self.easy_percent.place(relx=0.63, rely=0.3, anchor=CENTER)
        self.med_percent = ttk.Entry(master=self.head_frame, bootstyle="secondary", width=5)
        self.med_percent.insert(0, "0")
        self.med_percent.place(relx=0.70, rely=0.3, anchor=CENTER)
        self.hard_percent = ttk.Entry(master=self.head_frame, bootstyle="secondary", width=5)
        self.hard_percent.insert(0, "0")
        self.hard_percent.place(relx=0.77, rely=0.3, anchor=CENTER)

        self.btnSavePercent = ttk.Button(master=self.head_frame, text="save", bootstyle="secondary", width=10, command=self.ecrire)
        self.btnSavePercent.place(relx=0.93, rely=0.3, anchor=CENTER)


        # define columns
        columns = ("Questions")

        self.liste = ttk.Treeview(master=left_frame, columns=columns, height=21, show='headings')
        self.liste.pack(side=LEFT, padx=20, pady=5)
        self.liste.column("# 1", anchor="w", stretch=NO, width=300)

        # add a scrollbar
        scrollbar = ttk.Scrollbar(bootstyle="dark-round", master=left_frame, orient=tk.VERTICAL,
                                  command=self.liste.yview)
        self.liste.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)

        # define headings
        self.liste.heading('Questions', text='Les Questions')

        self.txtEntry = ttk.Entry(master=right_frame, bootstyle="danger")
        self.txtEntry.place(relx=0.5, rely=0.1, anchor=CENTER)
        self.txtEntry.configure(width=50)

        self.lblAnswers = ttk.Labelframe(master=right_frame, bootstyle="secondary", width=415, height=300,
                                         text="Réponses")
        self.lblAnswers.place(relx=0.5, rely=0.47, anchor=CENTER)
        self.reponse = IntVar()
        self.reponse.set(-1)
        self.checkans1 = ttk.Checkbutton(master=self.lblAnswers, variable=self.reponse, onvalue=0, offvalue=-1, bootstyle="success")
        self.checkans2 = ttk.Checkbutton(master=self.lblAnswers, variable=self.reponse, onvalue=1, offvalue=-1, bootstyle="success")
        self.checkans3 = ttk.Checkbutton(master=self.lblAnswers, variable=self.reponse, onvalue=2, offvalue=-1, bootstyle="success")
        self.checkans4 = ttk.Checkbutton(master=self.lblAnswers, variable=self.reponse, onvalue=3, offvalue=-1, bootstyle="success")
        self.answer1 = ttk.Entry(master=self.lblAnswers, bootstyle="secondary", width=40)
        self.answer2 = ttk.Entry(master=self.lblAnswers, bootstyle="secondary", width=40)
        self.answer3 = ttk.Entry(master=self.lblAnswers, bootstyle="secondary", width=40)
        self.answer4 = ttk.Entry(master=self.lblAnswers, bootstyle="secondary", width=40)

        self.niveau = IntVar()
        self.niveau.set(-1)
        self.easy = ttk.Checkbutton(master=self.lblAnswers, text="Easy", variable=self.niveau, onvalue=1, offvalue=-1, bootstyle="secondary")
        self.easy.place(relx=0.23, rely=0.92, anchor=CENTER)
        self.medium = ttk.Checkbutton(master=self.lblAnswers, text="Medium", variable=self.niveau, onvalue=2, offvalue=-1, bootstyle="secondary")
        self.medium.place(relx=0.45, rely=0.92, anchor=CENTER)
        self.hard = ttk.Checkbutton(master=self.lblAnswers, text="Hard", variable=self.niveau, onvalue=3, offvalue=-1, bootstyle="secondary")
        self.hard.place(relx=0.67, rely=0.92, anchor=CENTER)



        self.btnAjouter = ttk.Button(bootstyle="dark", master=right_frame, text="Ajouter", command=self.add_question)
        self.btnAjouter.place(relx=0.1, rely=0.92, anchor=tk.W)
        self.btnModifier = ttk.Button(bootstyle="dark", master=right_frame, text="Modifier", command=self.edit_question)
        self.btnModifier.place(relx=0.3, rely=0.92, anchor=tk.W)
        self.btnSupprimer = ttk.Button(bootstyle="dark", master=right_frame, text="Supprimer", command=self.delete_question)
        self.btnSupprimer.place(relx=0.51, rely=0.92, anchor=tk.W)
        self.btnEffacer = ttk.Button(bootstyle="dark", master=right_frame, text="Effacer", command=self.clearChamps)
        self.btnEffacer.place(relx=0.75, rely=0.92, anchor=tk.W)

        self.answer1.place(relx=0.5, rely=0.16, anchor=CENTER)
        self.checkans1.place(relx=0.06, rely=0.16, anchor=CENTER)
        self.answer2.place(relx=0.5, rely=0.36, anchor=CENTER)
        self.checkans2.place(relx=0.06, rely=0.36, anchor=CENTER)
        self.answer3.place(relx=0.5, rely=0.56, anchor=CENTER)
        self.checkans3.place(relx=0.06, rely=0.56, anchor=CENTER)
        self.answer4.place(relx=0.5, rely=0.76, anchor=CENTER)
        self.checkans4.place(relx=0.06, rely=0.76, anchor=CENTER)

        def item_selected(event):
            for selected_item in self.liste.selection():
                item = self.liste.item(selected_item)
                record = item['values']
                # show a message
                # messagebox.showinfo(title='Information', message=','.join(record))
                self.clearChamps()
                self.affiche(record)

        self.liste.bind('<<TreeviewSelect>>', item_selected)

        with open("quiz.json") as file:
            self.data = json.load(file)
            self.getQuestions()

        # ck.set_appearance_mode("System") Dark Light

        self.mainloop()

    def retourner(self):
        self.withdraw()
        subprocess.call(["python", "gametest.py"])

    def ecrire(self):
        with open("percentage.txt", "w") as file:
            file.write(f"{self.easy_percent.get()}\n")
            file.write(f"{self.med_percent.get()}\n")
            file.write(f"{self.hard_percent.get()}\n")

    def getQuestions(self):
        for item in self.liste.get_children():
            self.liste.delete(item)
        for index, d in enumerate(self.data):
            self.liste.insert('', tk.END, text="", iid=index, open=False, value=(d["question"],))

    def affiche(self, record):
        for index, d in enumerate(self.data):
            print(d["niveau"])
            if d["question"] == record[0]:
                self.id_question.set(d["ID"])
                rep = d["answers"]
                self.setContent(txt=record[0], rep1=rep[0], rep2=rep[1], rep3=rep[2], rep4=rep[3],
                                checkbtn=d["correctIndex"], nbr=d["niveau"])

    def add_question(self):
        self.data.append({
            "ID": self.data[-2]["ID"]+1,
            "question": self.txtEntry.get(),
            "answers": [
                self.answer1.get(),
                self.answer2.get(),
                self.answer3.get(),
                self.answer4.get()
            ],
            "correctIndex": self.reponse.get(),
            "niveau" : self.niveau.get()
        })
        with open("quiz.json", 'w') as json_file:
            json.dump(self.data, json_file,
                      indent=4,
                      separators=(',', ': '))
        self.write(self.data)
        self.getQuestions()
        lbl = ttk.Label(master=self.head_frame, bootstyle="inverse-success", text="La question a été ajoutée avec succés")
        lbl.place(relx=0.6, rely=0.3, anchor=tk.W)
        self.clearChamps()
        self.after(4000, lbl.destroy)

    def write(self, donnees):
        with open("questions.txt", "w") as file:
            for donnee in donnees:
                a = donnee["niveau"]
                niveau = "easy" if a==1 else ("med" if a==2 else "hard")
                print(niveau)
                file.write(f"'{donnee['question']}',{niveau}\n")
        with open("answer_choice.txt", "w") as file:
            for donnee in donnees:
                file.write(f"{donnee['answers'][0]},{donnee['answers'][1]},{donnee['answers'][2]},{donnee['answers'][3]}\n")
        with open("answers.txt", "w") as file:
            for donnee in donnees:
                file.write(f"{donnee['correctIndex']}\n")


    def delete_question(self):
        for index, q in enumerate(self.data):
            print(q["question"]," == ",self.txtEntry.get())
            if q["ID"] == self.id_question.get():
                print(type(self.data), index, self.data[index])
                self.data.pop(index)
        with open("quiz.json", 'w') as json_file:
            json.dump(self.data, json_file,
                      indent=4,
                      separators=(',', ': '))
        self.write(self.data)
        self.getQuestions()
        lbl = ttk.Label(master=self.head_frame, bootstyle="inverse-success", text="La question a été supprimée avec succés")
        lbl.place(relx=0.6, rely=0.3, anchor=tk.W)
        self.clearChamps()
        self.after(4000, lbl.destroy)

    def edit_question(self):
        for index, q in enumerate(self.data):
            if q["ID"] == self.id_question.get():
                print(type(self.data), index, self.data[index])
                self.data[index]["question"] = self.txtEntry.get()
                self.data[index]["answers"] = [self.answer1.get(), self.answer2.get(), self.answer3.get(), self.answer4.get()]
                self.data[index]["correctIndex"] = self.reponse.get()
                self.data[index]["niveau"] = self.niveau.get()
        with open("quiz.json", 'w') as json_file:
            json.dump(self.data, json_file,
                      indent=4,
                      separators=(',', ': '))
        self.write(self.data)
        self.getQuestions()
        lbl = ttk.Label(master=self.head_frame, bootstyle="inverse-success", text="La question a été modifiée avec succés")
        lbl.place(relx=0.6, rely=0.3, anchor=tk.W)
        self.clearChamps()
        self.after(4000, lbl.destroy)



    def clearChamps(self):
        self.txtEntry.delete(0, END)
        self.answer1.delete(0, END)
        self.answer2.delete(0, END)
        self.answer3.delete(0, END)
        self.answer4.delete(0, END)
        self.reponse.set(-1)
        self.niveau.set(-1)


    def setContent(self, txt, rep1, rep2, rep3, rep4, checkbtn=-1, nbr=-1):
        self.txtEntry.insert(0, txt)
        self.answer1.insert(0, rep1)
        self.answer2.insert(0, rep2)
        self.answer3.insert(0, rep3)
        self.answer4.insert(0, rep4)
        self.reponse.set(checkbtn)
        self.niveau.set(nbr)


if __name__ == "__main__":
    AdminGUI(themename="superhero")
