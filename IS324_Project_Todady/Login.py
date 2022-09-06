import tkinter
import tkinter.messagebox
import db
import re

class Login:
    
    def __init__(self):
        # Settings UI Interface :)
        self.color = "#403e3e"
        self.fontColor = "#cccccc"
        self.foreGround = "white"
        self.fontSize = "4"

        self.login_win = tkinter.Tk()
        self.login_win.config(bg="#403e3e")

        self.login_win.title("Ksu Payment")
        self.login_win.geometry("700x350")

        
        # Frames
        self.Login_Labelframe = tkinter.LabelFrame(self.login_win, text="Login Account ",bg=self.color, padx=100, bd=5, font=self.fontSize,foreground=self.foreGround)
        self.id_frame = tkinter.Frame(self.Login_Labelframe, bg=self.color)
        self.password_frame = tkinter.Frame(self.Login_Labelframe, bg=self.color)
        self.btnLogin_frame = tkinter.Frame(self.Login_Labelframe, bg=self.color)

        
        # Inputs and Lables 
        self.Id_label = tkinter.Label(self.id_frame, text="Id: ", font=self.fontSize, foreground=self.foreGround, bg=self.color)
        self.Id_Entry = tkinter.Entry(self.id_frame, width=40)
        
        self.password_label = tkinter.Label(self.password_frame, text="Password: ", font=self.fontSize, foreground=self.foreGround, bg=self.color)
        self.password_Entry = tkinter.Entry(self.password_frame, width=40)

        self.btnLogin = tkinter.Button(self.btnLogin_frame, text="Login", command=self.checkLogin)
        
        
        # Frames Pack
        self.Login_Labelframe.pack()
        self.id_frame.pack()
        self.password_frame.pack()
        self.btnLogin_frame.pack()
        
        # Packs
        self.Id_label.pack(side='left', pady=10)
        self.Id_Entry.pack(side='left', pady=10)
        
        self.password_label.pack(side='left', pady=10)
        self.password_Entry.pack(side='left', pady=10)
        
        self.btnLogin.pack()
        
        self.login_win.mainloop()
    
    def checkLogin(self):
        print("Login....")
        if self.isEmpty():
            tkinter.messagebox.showerror("Error", "Please Enter Id and Password")
        elif not self.checkId():
            tkinter.messagebox.showerror("Error", "The Id must be 10 digits and must not contain a letters")
        elif not self.checkPass():
            tkinter.messagebox.showerror("Error", "The password must be at least 6 digits or letters")
        else:
            print("Check Id and Password if correct")
            '''
                it connects with the central database to
                check the validity of the entered credentials. In case of success, if the user
                is a student, it opens the Student Wallet window, and if the user is an
                admin, it opens the Admin window. In case of failure, the system should
                display an error message to the user.
            '''
            loginInfo = {'id': self.Id_Entry.get(), 'password': self.password_Entry.get()}

            loginUser = db.loginUser(loginInfo)
            checkLogin = loginUser[0]
            saveData = loginUser[1]

            if checkLogin == True:
                if saveData['AccType'] == "Student":
                    print("* Your are in The Student Wallet Window")
                    self.login_win.destroy()
                    import StudentWallet
                    StudentWallet.StudentWallet(saveData)
                else:
                    print("* Your are in The Admin Window")
                    self.login_win.destroy()
                    import Admin
                    Admin.Admin(saveData)
            else:
                tkinter.messagebox.showerror("Error", "Wrong Id or password please try again")

            # if self.Id_Entry.get() == "1234567890":
            #     print("Admin")
            #     self.login_win.destroy()
            #     import Admin
            #     Admin.Admin()
            #
            # else:
            #     print("Student Wallet")
            #     self.login_win.destroy()
            #     import StudentWallet
            #     StudentWallet.StudentWallet()

        
    def checkId(self):
        # violation such as the ID is not digits or less than 10 digits.
        id = self.Id_Entry.get()
        id_reg = "^[0-9]{10}$"
        id_pat = re.compile(id_reg)
        id_valid = re.search(id_pat, id)
        return id_valid


    def checkPass(self):
        # at least 6 digits or letters
        Password = self.password_Entry.get()
        pass_reg = "^[A-Za-z0-9]{6,}$"
        pass_pat = re.compile(pass_reg)
        check_pass = re.search(pass_pat, Password)
        return check_pass

    def isEmpty(self):
        id = self.Id_Entry.get()
        Pass = self.password_Entry.get()
        if len(id) == 0 or len(Pass) == 0:
            return True 
        else: 
            return False

