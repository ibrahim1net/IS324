import tkinter
import tkinter.messagebox
from tkinter import filedialog as fd

class MyGUI:

    def __init__(self):

        self.main_window = tkinter.Tk()
        self.main_window.configure(bg='#005555')
        self.main_window.title('Assignment 6 Ibrahim Alkhudair :)')
        self.main_window.geometry("400x250")
        self.path = " "
        # Frames
        self.titleFrame = tkinter.Frame(self.main_window)
        self.nameFrame = tkinter.Frame(self.main_window, borderwidth=10)
        self.idFrame = tkinter.Frame(self.main_window)
        self.phoneFrame = tkinter.Frame(self.main_window)
        self.GpaFrame = tkinter.Frame(self.main_window)
        self.radioFrame = tkinter.Frame(self.main_window)
        self.fileFrame = tkinter.Frame(self.main_window)
        self.submitFrame = tkinter.Frame(self.main_window)

        # Lables and Entry
        self.Title = tkinter.Label(self.titleFrame, text="Internship Form", font=("Helvetical", 12) )
        self.label1 = tkinter.Label(self.nameFrame, text="Full Name : ")
        self.Name_Entry = tkinter.Entry(self.nameFrame, width=40)

        self.label2 = tkinter.Label(self.idFrame, text="ID : ")
        self.IdEntry = tkinter.Entry(self.idFrame, width=40)

        self.label3 = tkinter.Label(self.phoneFrame, text="Phone Number : ")
        self.PhoneEntry = tkinter.Entry(self.phoneFrame, width=40)

        self.label4 = tkinter.Label(self.GpaFrame, text="GPA : ")
        self.GpaEntry = tkinter.Entry(self.GpaFrame, width=40)
        self.label5 = tkinter.Label(self.radioFrame, text="Dep : ")

        self.label6 = tkinter.Label(self.fileFrame, text=" File to be saved : ")
        self.fileEntry = tkinter.Button(self.fileFrame, text="Open the file" ,command=self.action)

        # Submit button
        self.Sumbit_btn = tkinter.Button(self.submitFrame, text="Submit file", command= self.submitBtn)
        # Radio buttons
        self.radio_btn = tkinter.IntVar()
        self.rb1 = tkinter.Radiobutton(self.radioFrame, text="IS", variable=self.radio_btn, value=1)
        self.rb2 = tkinter.Radiobutton(self.radioFrame, text="CS", variable=self.radio_btn, value=2)
        self.rb3 = tkinter.Radiobutton(self.radioFrame, text="SE", variable=self.radio_btn, value=3)
        self.radio_btn.set(1)

        # Buttons


        # Packs Frames to organize
        self.titleFrame.pack()
        self.nameFrame.pack()
        self.idFrame.pack()
        self.phoneFrame.pack()
        self.GpaFrame.pack()
        self.radioFrame.pack()
        # Packs
        self.Title.pack(fill="x", padx="3", pady="3", side="left")
        self.label1.pack(padx="3", pady="3", side="left")
        self.Name_Entry.pack(padx="3", pady="3", side="left")

        self.label2.pack(fill="x", padx="3", pady="3", side="left")
        self.IdEntry.pack(fill="x", padx="3", pady="3", side="left")
        #
        self.label3.pack(fill="x", padx="3", pady="3", side="left")
        self.PhoneEntry.pack(fill="x", padx="3", pady="3", side="left")
        #
        self.label4.pack(fill="x", padx="3", pady="3", side="left")
        self.GpaEntry.pack(fill="x", padx="3", pady="3", side="left")

        # Packs radio btns
        self.label5.pack(side='left')
        self.rb1.pack(side='left')
        self.rb2.pack(side='left')
        self.rb3.pack(side='left')

        # File input
        self.fileFrame.pack()
        self.label6.pack(padx="3", pady="3", side="left")
        self.fileEntry.pack(padx="3", pady="3", side="left")


        self.submitFrame.pack()
        self.Sumbit_btn.pack(fill="x", padx="3", pady="3", side="left")
        tkinter.mainloop()

    def action(self):
        self.path = fd.askopenfilename()



    def checkPhoneNum(self):
        phone = str(self.PhoneEntry.get())
        # Phone num must be 10 digit
        if len(phone) != 10:
            return False
        if phone[:2] != "05":
            return False

        # Checking all string is digit
        for p in phone:
            if not p.isdigit():
                return False

        return True

    def checkId(self):
        id = str(self.IdEntry.get())
        if len(id) != 10:
            return False
        for i in id:
            if not i.isdigit():
                return False
        return True

    def checkName(self):
        name = str(self.Name_Entry.get())
        for n in name:
            if n.isdigit():
                return False
        return True

    def checkGpa(self):
        try:
            gpa = float(self.GpaEntry.get())
            if gpa >= 0 and gpa <= 5:
                return True
            return False
        except ValueError:
            return False

    def checkValidate(self):
        if self.checkPhoneNum() == True and self.checkName() == True and self.checkId() == True and self.checkGpa() == True:
            return True
        return False

    def saveToFile(self):
        values = {1: 'IS', 2:'CS', 3:'SE'}
        if str(self.path) != " ":
            File = open(str(self.path), "w")
            File.write(f"FullName: {self.Name_Entry.get()}\n")
            File.write(f"Phone: {self.PhoneEntry.get()}\n")
            File.write(f"Id: {self.IdEntry.get()}\n")
            File.write(f"Gpa: {self.GpaEntry.get()}\n")
            File.write(f"Department: {values[self.radio_btn.get()]}\n")
            File.close()
        else:
            tkinter.messagebox.showerror("Error", " You need to select a path")



    def submitBtn(self):
        if self.checkValidate() == True:
            self.saveToFile()
            if str(self.path) != " ":
                tkinter.messagebox.showinfo("Accept", "All information has been saved to the file")
        else:
            tkinter.messagebox.showerror("Error", "Make sure that, \nfull name must be all string,\n Id must be 10 Digits, "
                                                  "\nand Phone Number must start with 05 and 10 digits \n and Gpa must be between 0-5 \n and file must be selected ")

new_window = MyGUI()