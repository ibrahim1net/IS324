import sqlite3
import random
import datetime
import csv


def create():
    conn = sqlite3.connect("KSU_payment.db")
    print("Opened database successfully")

    try:
        conn.executescript('''
            CREATE TABLE ACCOUNT
                ( 
                    AccID              TEXT    NOT NULL,
                    FirstName     TEXT           NOT NULL,
                    LastName       TEXT           NOT NULL,
                    Password        TEXT           NOT NULL,
                    email           TEXT           NOT NULL,
                    PhoneNum       VARCHAR(10)     NOT NULL,
                    AccType      VARCHAR(20) NOT NULL,
                    PRIMARY KEY (AccID),
                    UNIQUE(email),
                    UNIQUE(PhoneNum) 

                );
                       
            CREATE TABLE WALLET
                ( 
                    WalletNum    INT             NOT NULL, 
                    DATE_TIME       DATETIME        NOT NULL,
                    BALANCE         FLOAT           NOT NULL, 
                    WalletType         VARCHAR(20)  NOT NULL,
                    AccId          TEXT              NULL,             
                    EntityName          TEXT,
                    PRIMARY KEY(WalletNum)
                    FOREIGN KEY(AccId) REFERENCES ACCOUNT(AccId)
                );
                   
                
           ''')
        print("Table created successfully")
        conn.close()


    except sqlite3.OperationalError:
        print('** Database has been created previously')
    createAdmin()


# checks all wallet tables if the generater duplicated ***********
def createAdmin():
    conn = sqlite3.connect("KSU_payment.db")

    id = 1234567890
    password = 123123
    firstName = "Ibrahim"
    lastName = "Alkhudair"
    email = "admin@ksu.edu.sa"
    phoneNumber = "0548406969"
    AccType = "Admin"

    try:
        conn.execute(f"INSERT INTO ACCOUNT VALUES ({id}, '{firstName}', '{lastName}', '{password}', '{email}', '{phoneNumber}', '{AccType}')")
        conn.commit()
        conn.close()
        print(f'The admin account is created successfully with ID {id}')
    except sqlite3.IntegrityError:
        print('The admin account has been created previously')

def genertateWallet():
    generater = random.randint(1000000000, 9999999999)
    return generater


def insertStudent(account):

    conn = sqlite3.connect("KSU_payment.db")
    try:

        now = datetime.datetime.now()
        now = now.strftime("%d/%m/%Y-%H:%M:%S")
        BALANCE = 1000

        conn.execute(f"INSERT INTO ACCOUNT VALUES ('{account['accId']}', '{account['firstName']}', '{account['lastName']}', '{account['Password']}', '{account['email']}', '{account['PhoneNum']}', 'Student') ")
        conn.commit()
        conn.execute(f"INSERT INTO WALLET VALUES({genertateWallet()}, '{now}', {BALANCE}, 'Student', '{account['accId']}', NULL) ")
        conn.commit()
        conn.close()
        print("Registered Successfully")
        return True
    except sqlite3.IntegrityError:
        print('The Student Already Register')
        return False



def loginUser(accLog):
    # print(accLog['id'])
    conn = sqlite3.connect("KSU_payment.db")
    data = conn.execute(f"SELECT * FROM ACCOUNT WHERE AccID='{accLog['id'] }' and Password='{accLog['password']}' ")

    global AccountInfo
    AccountInfo = {}
    count = 0
    for row in data:
        count += 1
        AccountInfo = {"Id": row[0], "FirstName": row[1], "LastName": row[2], "Email": row[4], "PhoneNumber": row[5], "AccType": row[6]}

    if count ==0:
        print("************ Passsword or User Id Wrong ")
        conn.close()
        return False, None
    else:
        if AccountInfo['AccType'] == "Student":
            data2 = conn.execute(f"SELECT * FROM ACCOUNT, WALLET WHERE ACCOUNT.AccID='{accLog['id']}' and Password='{accLog['password']}' and WALLET.AccId='{accLog['id']}' ")
            for row in data2:
                AccountInfo['WalletNum'] = row[7]
                AccountInfo['Balance'] = row[9]

        print("Logined Successfully")
        conn.close()
        return True, AccountInfo


# Pay Student method
def payStd(walletNumber, stdId, balance, transAmount):
    if transAmount <= 0:
        return False, 'The transform money cannot be less than 0'

    if balance < transAmount:
        return False, 'The Balance is less than the amount you want to transfer'

    if str(walletNumber) == str(AccountInfo['WalletNum']):
        return False, 'Cannot transfer to your self'

    conn = sqlite3.connect("KSU_payment.db")

    try:
        data = conn.execute(f"SELECT * FROM WALLET WHERE WalletNum='{walletNumber}' ")

        count = 0
        walletBalance = 0
        for row in data:
            count +=1
            print(row)
            walletBalance = row[2]
            print(walletBalance)

        if count ==0:
            return False, 'The Wallet Number is not exist'
        else:

            newBalance = balance - transAmount
            print(newBalance)
            conn.execute(f"UPDATE WALLET SET Balance={newBalance} WHERE AccId='{stdId}'")
            conn.execute(f"UPDATE WALLET SET Balance={walletBalance+transAmount} WHERE WalletNum={walletNumber}")
            conn.commit()
            conn.commit()
            AccountInfo['Balance'] = newBalance
            print('The Balance has been updated')
            conn.close()
            return True, 'The money transfered successfully'

    except sqlite3.IntegrityError:
        print('Error')
        return False, 'Error'

def listAll_Wallet():
    conn = sqlite3.connect("KSU_payment.db")

    data = conn.execute(f"SELECT * FROM Wallet WHERE WalletType='KSU' ")

    listOfEntites = []
    for row in data:
        listOfEntites.append(row)
    conn.close()
    return listOfEntites


def insertKsuEntity(name):
    conn = sqlite3.connect("KSU_payment.db")
    try:

        now = datetime.datetime.now()
        now = now.strftime("%d/%m/%Y-%H:%M:%S")
        BALANCE = 0

        conn.execute(f"INSERT INTO WALLET VALUES ('{genertateWallet()}', '{now}', '{BALANCE}', 'KSU', NULL, '{name}') ")
        conn.commit()
        conn.close()

        print("The New Entity has been Inserted Successfully Successfully")
        return True

    except sqlite3.IntegrityError:
        print('The entity has been already registered')
        return False

def depositsALL():
    conn = sqlite3.connect("KSU_payment.db")

    try:
        conn.execute("UPDATE Wallet SET Balance=Wallet.Balance+1000 WHERE WalletType='Student' ")
        conn.commit()
        conn.close()

        print("All The Student gets 1000.0 SR Successfully")
        return True
    except sqlite3.IntegrityError:
        print('Error')
        return False

def AllSetZero():
    conn = sqlite3.connect("KSU_payment.db")

    try:
        conn.execute("UPDATE Wallet SET Balance=0 WHERE WalletType='KSU' ")
        conn.commit()
        conn.close()

        print("All The Entity update to 0 SR Successfully")
        return True
    except sqlite3.IntegrityError:
        print('Error')
        return False

def totalBalanceEntites():
    conn = sqlite3.connect("KSU_payment.db")

    try:
        data = conn.execute("SELECT Balance FROM Wallet WHERE WalletType='KSU' ")
        totalBalance = 0
        for row in data:
            totalBalance += row[0]

        conn.commit()
        conn.close()

        return True, totalBalance
    except sqlite3.IntegrityError:
        print('Error')
        return False, 0

# the system backups all information of
# the central database into a CSV file format
def backup():
    print('Backing up the system ... ')
    conn = sqlite3.connect("KSU_payment.db")
    data = conn.execute("SELECT * FROM WALLET,ACCOUNT WHERE WalletType='Student' and WALLET.AccId=ACCOUNT.AccID")
    file = open("backup.csv", "w", newline="")
    csvwriter = csv.writer(file)

    # =================================
    heading = "Wallet Number, DateTime, Balance, Wallet Type, Student Id, First Name, Last Name, Password, Email, Phone Number"
    csvwriter.writerow(heading.split(","))
    for row in data:
        newstudentString = f"{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[6]}, {row[7]}, {row[8]}, {row[9]}, {row[10]}, {row[11]}"
        print(newstudentString)
        csvwriter.writerow(newstudentString.split(","))


    # =========================================
    data_entites = conn.execute("SELECT * FROM WALLET WHERE WalletType='KSU' ")

    heading_entites = "Wallet Number, DateTime, Balance, Wallet Type, Entity Name"
    csvwriter.writerow(heading_entites.split(","))

    for row in data_entites:
        entityString = f"{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[5]}"
        print(entityString)
        csvwriter.writerow(entityString.split(","))

    # =========================================

    data_admin = conn.execute("SELECT * FROM ACCOUNT WHERE AccType='Admin'")

    heading_admin = "Admin Id, Admin First Name, Admin Last Name, Password, Email, Phone Number"
    csvwriter.writerow(heading_admin.split(","))

    for row in data_admin:
        AdminString = f"{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}"
        print(AdminString)
        csvwriter.writerow(AdminString.split(","))

    file.close()
    conn.close()

create()
