import tkinter
import tkinter as tk
import tkinter.messagebox
import db
import re
class Admin:
   def __init__(self, data):
      # Settings UI Interface :)
      self.color = "#853731"
      self.fontColor = "#cccccc"
      self.foreGround = "white"
      self.fontSize = "4"
      self.totalBalance = db.totalBalanceEntites()[1]
      print(data)
      self.admin_window = tk.Tk()
      self.admin_window.configure(bg='#853731')

      self.admin_window.title("Admin")
      self.admin_window.geometry('700x350')


      self.admin_LabelFrame = tkinter.LabelFrame(self.admin_window, text="Admin Page", bg=self.color, padx=100, bd=5, font=self.fontSize,foreground=self.foreGround)
      self.info_Frame = tkinter.Frame(self.admin_LabelFrame, bg=self.color)
      self.Submit_Frame = tkinter.Frame(self.admin_LabelFrame, bg=self.color)
      self.btns_Frames = tkinter.Frame(self.admin_LabelFrame, bg=self.color, padx=20, pady=30)

      self.fieldEntity_frame = tkinter.LabelFrame(self.admin_LabelFrame, text="Info", padx=20, pady=20, bg="#853731")
      self.total_frame = tkinter.Frame(self.admin_LabelFrame, bg="#853731")


      self.total_label = tk.Label(self.total_frame, text=f"The Total of all ksu enities wallets is: {self.totalBalance} SR" , bg=self.color, font=self.fontSize, foreground=self.fontColor)
      self.fieldEntity_Label = tk.Label(self.fieldEntity_frame, text="KSU Entity Name: ", bg=self.color, font=self.fontSize, foreground=self.fontColor)
      self.fieldEntity_Input = tk.Entry(self.fieldEntity_frame, width=20, font=self.fontSize)

      self.submit_btn = tk.Button(self.Submit_Frame, text='Submit', command=self.submitEntity)
      self.pay_btn = tk.Button(self.btns_Frames, text='Pay Stipends', command=self.checkDespoite)
      self.cashout_btn = tk.Button(self.btns_Frames, text='Cash out', command=self.checkCashOut)

      # for the Extra credit
      self.backUp_btn = tk.Button(self.btns_Frames, text='Backup', command=self.backUp_db)

      self.buttonBack = tk.Button(self.btns_Frames, text='Back Logout', command=self.logout)

      # Packing Frames
      self.admin_LabelFrame.pack()
      self.total_frame.pack()
      self.fieldEntity_frame.pack()

      self.info_Frame.pack()
      self.Submit_Frame.pack()
      self.btns_Frames.pack()


      #Packing Btn
      self.total_label.pack(side='left', pady=10)

      self.fieldEntity_Label.pack(side='left', pady=10)
      self.fieldEntity_Input.pack(side='left', pady=10)

      self.buttonBack.pack(side='left', pady=10 , padx= 5)
      self.backUp_btn.pack(side='left', pady=10,  padx= 7)
      self.submit_btn.pack(side='left', pady=10, padx= 9)
      self.pay_btn.pack(side='left', pady=10 ,  padx= 11)
      self.cashout_btn.pack(side='left', pady=10 , padx= 13)

      self.admin_window.mainloop()

   def logout(self):
      self.admin_window.destroy()
      import Signup
      Signup.Signup()

   def submitEntity(self):
      if not self.validateName():
         tkinter.messagebox.showerror('Error', 'Invalid Entity Name , must contain only letters')
         return

      check = db.insertKsuEntity(self.fieldEntity_Input.get())

      if check:
         tkinter.messagebox.showinfo('Success', 'The Entity has been added successfully')
      else:
         tkinter.messagebox.showerror('Error', 'The Entity has been already registered')

   def updateTotalBalance(self):

      check = db.totalBalanceEntites()
      if check[0]:
         self.total_label['text'] = f"The Total of all ksu enities wallets is: {check[1]} SR"
      else:
         tkinter.messagebox.showerror('Error', 'The total entites will show 0')
         self.total_label['text'] = f"The Total of all ksu Enities wallets is: {check[1]} SR"


   def checkDespoite(self):
      check = db.depositsALL()

      if check:
         tkinter.messagebox.showinfo('Success', 'The money has been deposited to all the students')
      else:
         tkinter.messagebox.showerror('Error', 'Error')

   def checkCashOut(self):
      check = db.AllSetZero()

      if check:
         self.updateTotalBalance()
         tkinter.messagebox.showinfo('Success', 'All Entity has been cash out! ')
      else:
         tkinter.messagebox.showerror('Error', 'Error')

   def backUp_db(self):
      db.backup()
      tkinter.messagebox.showinfo('Success', 'The system backup the database successfully')

   def validateName(self):
      name = self.fieldEntity_Input.get()
      name_reg = "^[A-Za-z]*$"
      name_pat = re.compile(name_reg)
      name_valid = re.search(name_pat, name)
      return name_valid