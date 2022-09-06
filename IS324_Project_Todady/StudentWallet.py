import tkinter
import db
import tkinter.messagebox
import logging
import re
logging.basicConfig(filename='StudentWallet.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

class StudentWallet:
    


    def __init__(self, data):
        # Settings UI Interface :)
        self.color = "#403e3e"
        self.fontColor = "#cccccc"
        self.foreGround = "white"
        self.fontSize = "4"
        self.currentBalance = data['Balance']
        print(data)


        self.stdWallet_win = tkinter.Tk()
        self.stdWallet_win.config(bg="#403e3e")

        self.stdWallet_win.title("Ksu Payment")
        self.stdWallet_win.geometry("700x350")
        
        # Frames
        self.StdWallet_LabelFrame = tkinter.LabelFrame(self.stdWallet_win, text="Student Wallet Information", bg=self.color, padx=100, bd=5, font=self.fontSize,foreground=self.foreGround)
        self.Info_frame = tkinter.Frame(self.StdWallet_LabelFrame,bg=self.color)
        self.WalletNum_frame = tkinter.Frame(self.StdWallet_LabelFrame, bg=self.color)
        self.amount_frame = tkinter.Frame(self.StdWallet_LabelFrame, bg=self.color)
        self.btns_frame = tkinter.Frame(self.StdWallet_LabelFrame, bg=self.color)
        self.FrameName = tkinter.Frame(self.StdWallet_LabelFrame, bg=self.color)

        # Labels and Inputs and Button
        self.StdInfo_Label = tkinter.Label(self.FrameName, text=f"Your Full Name is: {data['FirstName']} {data['LastName']}", font=self.fontSize, bg=self.color, foreground=self.fontColor)

        self.walletNum_Label = tkinter.Label(self.Info_frame, text=f"Your Wallet Number: {data['WalletNum']}", font=self.fontSize, bg=self.color, foreground=self.fontColor)
        self.balance_Label = tkinter.Label(self.Info_frame, text=f"Current Balance: {self.currentBalance} SR", font=self.fontSize, bg=self.color, foreground=self.fontColor)
        
        self.walletAnother_Label = tkinter.Label(self.WalletNum_frame, text="Wallet Number: ", font=self.fontSize, bg=self.color, foreground=self.fontColor)
        self.walletAnother_input = tkinter.Entry(self.WalletNum_frame, width=40)
        
        self.amountTrans_Label = tkinter.Label(self.amount_frame, text="Amount you want to pay: ", font=self.fontSize, bg=self.color, foreground=self.fontColor)
        self.amountTrans_input = tkinter.Entry(self.amount_frame, width=40)

        self.btn_pay = tkinter.Button(self.btns_frame, text="Pay", command= lambda: self.checkPayment(data))
        self.btn_back = tkinter.Button(self.btns_frame, text="Back", command=self.backToSignup)
        
        # Frames Packs
        self.StdWallet_LabelFrame.pack()
        self.FrameName.pack()
        self.Info_frame.pack()
        self.WalletNum_frame.pack()
        self.amount_frame.pack()
        self.amount_frame.pack()
        self.btns_frame.pack()
        
        
        # Labels and inputs packs
        self.walletNum_Label.pack(side='left', pady=10)
        self.StdInfo_Label.pack(side='left', pady=10)

        self.balance_Label.pack(side='left', pady=10)
        
        self.walletAnother_Label.pack(side='left', pady=10)
        self.walletAnother_input.pack(side='left', pady=10)
        
        self.amountTrans_Label.pack(side='left', pady=10)
        self.amountTrans_input.pack(side='left', pady=10)
        
        self.btn_pay.pack(side='left', pady=10 , padx= 5)
        self.btn_back.pack(side='left', pady=10 ,  padx= 10)
        
        
        self.stdWallet_win.mainloop()


    def updateCurrentBalance(self, data):
        self.balance_Label['text'] = f"Current Balance: {data['Balance']} SR"

    def checkPayment(self, data):

        if self.walletAnother_input.get() == '' or self.amountTrans_input.get() == '':
            tkinter.messagebox.showerror('Error', 'please check the both field cannot be empty')
        elif not self.checkWalletNum():
            tkinter.messagebox.showerror('Error', 'Wallet number must contain digits only and must be 10')
        elif not self.checkTransMoney():
            tkinter.messagebox.showerror('Error', 'The Transfer money must be a digits')
        else:
            check = db.payStd(self.walletAnother_input.get(), data['Id'], float(data['Balance']), float(self.amountTrans_input.get()))
            if check[0]:
                self.updateCurrentBalance(data)

                # Extra credit
                logging.info(f"Sender [ {data['WalletNum']} ] has paid {float(self.amountTrans_input.get())} To [ {self.walletAnother_input.get()} ]")

                tkinter.messagebox.showinfo('Info', f'{check[1]}')
            else:
                tkinter.messagebox.showerror('Error', f'{check[1]}')

    def checkWalletNum(self):
        wallet = self.walletAnother_input.get()
        wallet_reg = "^[0-9]{10}$"
        wallet_pat = re.compile(wallet_reg)
        wallet_valid = re.search(wallet_pat, wallet)
        return wallet_valid


    def checkTransMoney(self):
        transmony = self.amountTrans_input.get()
        try:
            float(transmony)
            return True
        except ValueError:
            return False


    def backToSignup(self):
        self.stdWallet_win.destroy()
        import Signup
        Signup.Signup()

    def logTransactions(self):
        print('log...')
