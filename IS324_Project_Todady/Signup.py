import tkinter 
import tkinter.messagebox
import db
import re

class Signup:

    def __init__(self):

        # Settings UI Interface :)
        self.color = "#403e3e"
        self.fontColor = "#cccccc"
        self.foreGround = "white"
        self.fontSize = "4"




        self.signup_win = tkinter.Tk()
        self.signup_win.config(bg="#403e3e")
        self.signup_win.title("Ksu Payment")
        self.signup_win.geometry("700x350")


        # Frames
        self.LabelFrame_Singup = tkinter.LabelFrame(self.signup_win, text="Register Account", bg=self.color, padx=100, bd=5, font=self.fontSize,foreground=self.foreGround)
        self.firstN_frame = tkinter.Frame(self.LabelFrame_Singup, bg=self.color)
        self.lastN_frame = tkinter.Frame(self.LabelFrame_Singup, bg=self.color)
        self.stdId_frame = tkinter.Frame(self.LabelFrame_Singup, bg=self.color)
        self.pass_frame = tkinter.Frame(self.LabelFrame_Singup, bg=self.color)
        self.mail_frame = tkinter.Frame(self.LabelFrame_Singup, bg=self.color)
        self.phoneNum_frame = tkinter.Frame(self.LabelFrame_Singup, bg=self.color)
        self.sumb_frame = tkinter.Frame(self.LabelFrame_Singup, bg=self.color)

        # Labels and Inputs
        
        self.firstN_label = tkinter.Label(self.firstN_frame, text="First Name: ", font=self.fontSize, foreground=self.foreGround, bg=self.color)
        self.firstN_label.grid(column=0, row=0)
        self.firstN_input = tkinter.Entry(self.firstN_frame, width=40)
        
        self.lastN_label = tkinter.Label(self.lastN_frame, text = "Last Name: ", font=self.fontSize, foreground=self.foreGround, bg=self.color)
        self.lastN_input = tkinter.Entry(self.lastN_frame, width=40)

        self.stdId_label = tkinter.Label(self.stdId_frame, text = "Student ID: ", font=self.fontSize, foreground=self.foreGround, bg=self.color)
        self.stdId_input = tkinter.Entry(self.stdId_frame, width=40)


        
        self.mail_label = tkinter.Label(self.mail_frame, text = "Email address: ", font=self.fontSize, foreground=self.foreGround, bg=self.color)
        self.mail_input = tkinter.Entry(self.mail_frame, width=40)

        self.pass_lable = tkinter.Label(self.pass_frame, text = "Password: ", font=self.fontSize, foreground=self.foreGround, bg=self.color)
        self.pass_input = tkinter.Entry(self.pass_frame, width = 40)
                
        self.phoneNum_lable = tkinter.Label(self.phoneNum_frame, text = "Phone Number: ", font=self.fontSize, foreground=self.foreGround, bg=self.color)
        self.phoneNum_input = tkinter.Entry(self.phoneNum_frame, width = 40)
        
        self.sumbit_btn = tkinter.Button(self.sumb_frame, text="Sumbit", command=self.submitFunction)
        self.toLogin_btn = tkinter.Button(self.sumb_frame, text="Login", command=self.toLogin)

        
        # Frames packs
        self.firstN_frame.grid(column=0, row=0)
        self.LabelFrame_Singup.grid(column=1, row=0)

        self.LabelFrame_Singup.pack()
        self.firstN_frame.pack()
        self.lastN_frame.pack()
        self.stdId_frame.pack()
        self.mail_frame.pack()
        self.pass_frame.pack()
        self.phoneNum_frame.pack()
        self.sumb_frame.pack()
        
        # Grids
        self.firstN_label.grid(column=0, row=0)

        # Packs Lables and Entry
        self.firstN_label.pack(side='left', pady=10)
        self.firstN_input.pack(side='left', pady=10)
        
        self.lastN_label.pack(side='left', pady=10)
        self.lastN_input.pack(side='left', pady=10)
        
        self.stdId_label.pack(side='left', pady=10)
        self.stdId_input.pack(side='left', pady=10)
        
        self.pass_lable.pack(side='left', pady=10)
        self.pass_input.pack(side='left', pady=10)

        self.mail_label.pack(side='left', pady=10)
        self.mail_input.pack(side='left', pady=10)
        
        self.phoneNum_lable.pack(side='left', pady=10)
        self.phoneNum_input.pack(side='left', pady=10)
        
        self.sumbit_btn.pack(side='right', pady=10, padx= 10)
        self.toLogin_btn.pack(side='right', pady=10, padx= 5)
        
        tkinter.mainloop()
        
    def toLogin(self):
        print("Login Page")
        self.signup_win.destroy()
        import Login
        Login.Login()
        
        
        
    def submitFunction(self):
        if self.isEmpty():
            tkinter.messagebox.showerror("Error", "you can't leave an empty blanck")
        elif not self.checkName():
            # Give an error message for names 
            tkinter.messagebox.showerror("Error", "The First name and Last Name must be letters")
           
        elif not self.checkStdId():
            # Give an error message for id 
            tkinter.messagebox.showerror(" Error", "The Id must be 10 digits and must not contain a letters")
        elif not self.checkMail():
            # Give an error message for Mail 
            tkinter.messagebox.showerror("Error", "The email address must end with example@ksu.edu.sa")
        elif not self.checkPass():
            # Give an error message for Pass 
            tkinter.messagebox.showerror("Error", "The password must be at least 6 digits or letters")
        elif not self.checkPhone():
             # Give an error message for Phone 
            tkinter.messagebox.showerror("Error", "The Phone number must start with 05 and 10 digits")
    
        else:
            '''
                the system generates a 10-digit
                random number that represents the wallet number, current Date & Time,
                wallet type (student), 1000 SR initial balance to any new student wallet.
                Then, the system sends this information along with the student information
                to the central database. If the student has been already registered, the
                system should display an error message.
            '''
            account = {'accId': self.stdId_input.get(), 'firstName': self.firstN_input.get(), 'lastName': self.lastN_input.get(), 'Password': self.pass_input.get() , 'email': self.mail_input.get(), 'PhoneNum': self.phoneNum_input.get()}
            if db.insertStudent(account):
                tkinter.messagebox.showinfo("Info", "The Account created successfully :) Thanks")
                self.signup_win.destroy()
                import Login
                Login.Login()
            else:
                tkinter.messagebox.showerror("Error", "Error! Account has been already registered")


        
    def checkStdId(self):
        # Checks 10 digits of Id num
        id = self.stdId_input.get()
        id_reg = "^[0-9]{10}$"
        id_pat = re.compile(id_reg)
        id_valid = re.search(id_pat, id)
        return id_valid

    def checkPass(self):
        # at least 6 digits or letters
        Password = self.pass_input.get()
        pass_reg = "^[A-Za-z0-9]{6,}$"
        pass_pat = re.compile(pass_reg)
        check_pass = re.search(pass_pat, Password)
        return check_pass


   
    def checkMail(self):
        # Checks in this format XXXXXXXX@ksu.edu.sa
        mail = self.mail_input.get()
        email_reg = "^([a-zA-Z0-9\._-]+)(@ksu.edu.sa)$"
        email_pat = re.compile(email_reg)
        x = re.search(email_pat, mail)
        return x
        
    def checkPhone(self):
        # Checks n this format 05XXXXXXXX
        phone = self.phoneNum_input.get()
        phone_reg = "^(05)[0-9]{8}$"
        phone_pat = re.compile(phone_reg)
        phone_valid = re.search(phone_pat, phone)
        return phone_valid

        
    def checkName(self):
        # Checks if the first and last not include numbers
        fname = self.firstN_input.get()
        lname = self.lastN_input.get()
        name_reg = "^[A-Za-z]*$"
        name_pat = re.compile(name_reg)
        fname_valid = re.search(name_pat, fname)
        lname_valid = re.search(name_pat, lname)
        return fname_valid and lname_valid
            
    def isEmpty(self):
        # Checks all the fields 
        id = self.stdId_input.get()
        Pass = self.pass_input.get() 
        mail = self.mail_input.get()
        phone = self.phoneNum_input.get()
        fname = self.firstN_input.get()
        lname = self.lastN_input.get()
        if len(id) == 0 or len(Pass) == 0 or len(mail) ==0 or len(phone)==0 or len(fname) == 0 or len(lname) ==0:
            return True
        return False
        
