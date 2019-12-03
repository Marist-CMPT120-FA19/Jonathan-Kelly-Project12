#Jonathan Kelly, jonathan.kelly2@marist.edu
#Creates an ATM GUI and allows a registered user to check balances, transfer money, or withdraw money

from tkinter import *

root = Tk()   
HEIGHT = 500
WIDTH = 600
accounts = open('Accounts', 'r').readlines()

def getID():
    return IDbox.get()

def logIn(ID, PIN):
    if ID != '' and PIN != '':    
        for x in accounts:
            x = x.split(',')
            if((str(ID) == x[0]) and (str(PIN) == x[1])):
                
                frame2.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)
            else:
                wrongLogIn = Label(frame, text = 'Wrong ID or PIN')
                wrongLogIn.place(relx = 0.4, rely = 0.9, relwidth = 0.2, relheight = 0.05)
                
def withdrawBack():
    frame3.place_forget()
    
def viewBack():
    frame4.place_forget()
    
def transferBack():
    frame5.place_forget()
    
def withdraw1():
    frame3.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)

    account = Entry(frame3)
    account.place(relx = 0.2, rely = 0.1, relwidth = 0.2, relheight = 0.05)
    accLabel = Label(frame3, text = 'Which account:')
    accLabel.place(relx = 0, rely = 0.1, relwidth = 0.2, relheight = 0.05)
    
    amount = Entry(frame3)
    amount.place(relx = 0.2, rely = 0.3, relwidth = 0.2, relheight = 0.05)
    amountLabel = Label(frame3, text = "How Much:")
    amountLabel.place(relx = 0, rely = 0.3, relwidth = 0.2, relheight = 0.05)
    
    withdrawButton = Button(frame3, text = 'Withdraw', command = lambda: withdraw2(account.get(), amount.get()))
    withdrawButton.place(relx = 0, rely = 0.5, relwidth = 0.2, relheight = 0.05)
    
    
def withdraw2(account, amount):
    users = open('Accounts', 'r').readlines()
    
    #gets Account
    for x in users:
        if((getID() in x)):
            user = x.split(',')
    
    #withdraws money
    if 'savings' in account:
        if int(user[2]) >= int(amount):
            user[2] = int(user[2]) - int(amount)
            
            success = Label(frame3, text = "Success")
            success.place(relx = 0, rely = 0.7, relwidth = 0.2, relheight = 0.05)
            
            backButton = Button(frame3, text = 'Go Back', command = lambda: withdrawBack())
            backButton.place(relx = 0, rely = 0.8, relwidth = 0.2, relheight = 0.05)
    else:
        if int(user[3])>= int(amount):
            user[3] = int(user[3]) - int(amount)
            
            success = Label(frame3, text = "Success")
            success.place(relx = 0, rely = 0.7, relwidth = 0.2, relheight = 0.05) 
            
            backButton = Button(frame3, text = 'Go Back', command = lambda: withdrawBack())
            backButton.place(relx = 0, rely = 0.8, relwidth = 0.2, relheight = 0.05)
    
    #updates file
    for x in users:
        num = users.index(x)
        if(user[0] in x):
            users[num] = user[0] + ',' + str(user[1]) + ',' + str(user[2]) + ',' + str(user[3]) + '\n'
            
            Updateusers = open('Accounts', 'w+')
            for i in users:
                Updateusers.write(i)
    Updateusers.close()
    
def viewBalance():
    frame4.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)
    
    users = open('Accounts', 'r').readlines()
    
    for x in users:
        if((getID() in x)):
            user = x.split(',')
            
    savings = Label(frame4, text = 'Savings:  ' + str(user[2]), font = 35)
    savings.place(relx = 0, rely = 0.1, relwidth = 0.4, relheight = 0.1)
    
    checking = Label(frame4, text = 'Checking:  ' + str(user[3]), font = 30)
    checking.place(relx = 0, rely = 0.3, relwidth = 0.4, relheight = 0.1)
    
    backButton = Button(frame4, text = 'back', command = lambda: viewBack())
    backButton.place(relx = 0, rely = 0.5, relwidth = 0.2, relheight = 0.05)
    
def transfer1():
    frame5.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)
    
    tranFrom = Entry(frame5)
    tranFrom.place(relx = 0.2, rely = 0.1, relwidth = 0.2, relheight = 0.05)
    accLabel = Label(frame5, text = 'From: ')
    accLabel.place(relx = 0, rely = 0.1, relwidth = 0.2, relheight = 0.05)
    
    amount = Entry(frame5)
    amount.place(relx = 0.2, rely = 0.3, relwidth = 0.2, relheight = 0.05)
    amountLabel = Label(frame5, text = "Amount: ")
    amountLabel.place(relx = 0, rely = 0.3, relwidth = 0.2, relheight = 0.05)
    
    transferButton = Button(frame5, text = 'Transfer', command = lambda: transfer2(tranFrom.get(), amount.get()))
    transferButton.place(relx = 0, rely = 0.5, relwidth = 0.2, relheight = 0.05)
    
def transfer2(tranFrom, Amount):
    users = open('Accounts', 'r').readlines()
    
    #gets Account
    for x in users:
        if((getID() in x)):
            user = x.split(',')
    
    #transfers money
    if 'savings' in tranFrom:
        if int(user[2]) >= int(Amount):
            user[2] = int(user[2]) - int(Amount)
            user[3] = int(user[3]) + int(Amount)
            
            success = Label(frame5, text = "Success")
            success.place(relx = 0, rely = 0.8, relwidth = 0.2, relheight = 0.05)
            
            backButton = Button(frame5, text = 'Go Back', command = lambda: transferBack())
            backButton.place(relx = 0, rely = 0.9, relwidth = 0.2, relheight = 0.05)
    else:
        if int(user[3])>= int(Amount):
            user[3] = int(user[3]) - int(Amount)
            user[2] = int(user[2]) + int(Amount)
            
            success = Label(frame5, text = "Success")
            success.place(relx = 0, rely = 0.8, relwidth = 0.2, relheight = 0.05) 
            
            backButton = Button(frame5, text = 'Go Back', command = lambda: transferBack())
            backButton.place(relx = 0, rely = 0.9, relwidth = 0.2, relheight = 0.05)
    
    #updates file
    for x in users:
        num = users.index(x)
        if(user[0] in x):
            users[num] = user[0] + ',' + str(user[1]) + ',' + str(user[2]) + ',' + str(user[3]) + '\n'
            
            Updateusers = open('Accounts', 'w+')
            for i in users:
                Updateusers.write(i)
    Updateusers.close()
    
canvas = Canvas(root, height=HEIGHT, width = WIDTH, bg = 'blue')
canvas.pack()

frame = Frame(root, bg = '#fafafa')
frame2 = Frame(root, bg = '#fafafa')
frame3 = Frame(root, bg = '#fafafa')
frame4 = Frame(root, bg = '#fafafa')
frame5 = Frame(root, bg = '#fafafa')

frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)

title = Label(frame, text = 'Welcome', fg = 'black', font = 30)
title.place(relx = 0.42, rely = 0.1, relwidth = 0.2, relheight = 0.05)

ID = Label(frame, text = 'User ID', fg = 'black')
ID.place(relx = 0.28, rely = 0.3, relwidth = 0.2, relheight = 0.05)

IDbox = Entry(frame)
IDbox.place(relx = 0.5, rely = 0.3, relwidth = 0.2, relheight = 0.05)

PIN = Label(frame, text = 'PIN', fg = 'black')
PIN.place(relx = 0.28, rely = 0.5, relwidth = 0.2, relheight = 0.05)

PINbox = Entry(frame)
PINbox.place(relx = 0.5, rely = 0.5, relwidth = 0.2, relheight = 0.05)

logInButton = Button(frame, text = 'Log In',command =lambda: logIn(IDbox.get(), PINbox.get()))
logInButton.place(relx = 0.4, rely = 0.7, relwidth = 0.2, relheight = 0.05)

withdraw = Button(frame2, text = 'Withdraw', font = 15, command = lambda: withdraw1())
withdraw.place(relx = 0, rely = 0.3, relwidth = 0.21, relheight = 0.1)

transfer = Button(frame2, text = 'Transfer', font = 25, command = lambda: transfer1())
transfer.place(relx = 0, rely = 0.6, relwidth = 0.21, relheight = 0.1)

view = Button(frame2, text = 'View Balance', font = 15, command = lambda: viewBalance())
view.place(relx = 0, rely = 0, relwidth = 0.21, relheight = 0.1)

logOutButton = Button(frame2, text = 'Log out', command = lambda: root.destroy())
logOutButton.place(relx = 0, rely = 0.9, relwidth = 0.2, relheight = 0.05)


def main():
    root.mainloop()
main()
