# import random

CAP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low = CAP.lower()
num = str(range(0, 10))
symbole = "!@#$%^&*?/."

raw = CAP + low + num + symbole
len = int(input("Enter the length of the password : "))

password = ''.join(random.sample(raw, len))
print(f"Your password is {password} ")

from tkinter import *

def generate():
    CAP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    low = 

root = Tk()
root.title('Password Generator')
root.geometry('400x400')
root.configure(background='orange')
Label(root,text='Pass Generator',font='arial 20 bold',padx=5).pack(pady=20)
frm1 = Frame(root,bg='orange')
Label(frm1,text='Org - ',font='arial 10 bold', bg='orange').pack(side=LEFT, padx=15)
orgVar = StringVar()
Entry(frm1,textvariable=orgVar, font='arial 10', relief=SUNKEN).pack(side=RIGHT)
frm1.pack()
frm2 = Frame(root,bg='orange')
paslen = Label(frm2,text='Pass Length - ', font='arial 10 bold', bg='orange').pack(side=LEFT,padx=10,pady=10)
lenVer = StringVar()
Entry(frm2,textvariable=lenVer,font='arial 10', relief=SUNKEN, width='12').pack(side=RIGHT,padx=10)
frm2.pack()
Button(root,text='Generate',font='arial 10 bold',pady='2', relief=SUNKEN,activebackground='gold', command=generate).pack(pady=5)
passvar = StringVar()
Entry(root,textvariable=passvar, font='arial 15', relief=SUNKEN).pack(pady=10)
root.mainloop()
