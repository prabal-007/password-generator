# # import random

# CAP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# low = CAP.lower()
# num = str(range(0, 10))
# symbole = "!@#$%^&*?/."

# raw = CAP + low + num + symbole
# len = int(input("Enter the length of the password : "))

# password = ''.join(random.sample(raw, len))
# print(f"Your password is {password} ")

from tkinter import *
import random

root = Tk()

root.title('Password Generator')
root.geometry('400x400')
root.configure(background='orange')

def generate():
    CAP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    low = CAP.lower()
    num=str(range(0,10))
    symbole = '!@#$%&*?/.'

    raw1 = CAP+low+num+symbole
    raw2 = CAP+low+num
    raw3 = low+num
    raw4 = num+symbole
    raw5 = low+symbole
    len = int(lenVer.get())
    pass1 = ''.join(random.sample(raw1,len))
    pass2 = ''.join(random.sample(raw2,len))
    pass3 = ''.join(random.sample(raw3,len))
    pass4 = ''.join(random.sample(raw4,len))
    pass5 = ''.join(random.sample(raw5,len))
    strength = staVar.get()
    if strength == 'weak':
        passvar.set(pass3)
    elif strength == 'good':
        passvar.set(random.choice(pass4,pass5))
    elif strength == 'strong':
        passvar.set(pass2)
    else:
        passvar.set(pass1)
    
    # passlist = [pass1,pass2,pass3]
    # password = random.choice(passlist)
    # passvar.set(password)
    # strength(password)

# def strength(password):
#     etr = Label(root,text='wer', font='arial 10')
#     etr.pack()
#     strengthlist = ['Enter Something','weak','good','strong','very strong']
#     score = 1
#     if len(password) < 6:
#         etr.config(text = strengthlist[1])
#         # etr.update()
#         return
#     else:
#         pass


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
Button(root,text='Generate',font='arial 10 bold',pady='2', relief=RAISED,activebackground='gold', command=generate).pack(pady=5)
frm3= Frame(root,bg='orange')
Label(frm3,text='Strength : ', font='helvetica 10',bg='orange').pack(side=LEFT)
staVar = StringVar()
staVar.set('weak')
strengthlist = ['weak','good','strong','very strong']
for i in range (len(strengthlist)):
    radio =Radiobutton(frm3,text=strengthlist[i], variable=staVar, value=strengthlist[i],padx='5',bg='orange').pack(side=LEFT)
frm3.pack()
passvar = StringVar()
Entry(root,textvariable=passvar, font='arial 15', relief=SUNKEN).pack(pady=10)


root.mainloop()
