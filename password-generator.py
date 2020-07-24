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
    
    try:
        len = int(lenVer.get())
        pass1 = ''.join(random.sample(raw1,len))
        pass2 = ''.join(random.sample(raw2,len))
        pass3 = ''.join(random.sample(raw3,len))
        pass4 = ''.join(random.sample(raw4,len))
        pass5 = ''.join(random.sample(raw5,len))
        strength = staVar.get()
        if len < 7:
            staVar.set('weak')
            print(strength)
            passvar.set(pass3)
        elif 6<len<11:
            staVar.set('good')
            lis = [pass4,pass5]
            passvar.set(random.choice(lis))
        elif 10<len<16:
            staVar.set('strong')
            passvar.set(pass2)
        elif 15<len<23:
            staVar.set('very strong')
            passvar.set(pass1)
        else:
            passvar.set('Error')
    except Exception as e:
        passvar.set('Error')
    # passlist = [pass1,pass2,pass3]
    # password = random.choice(passlist)
    # passvar.set(password)
    # strength(password)

Label(root,text='Pass Generator',font='arial 20 bold',padx=5).pack(pady=20)
frm1 = Frame(root,bg='orange')
Label(frm1,text='Org - ',font='arial 10 bold', bg='orange').pack(side=LEFT, padx=15)
orgVar = StringVar()
Entry(frm1,textvariable=orgVar, font='arial 10', relief=SUNKEN).pack(side=RIGHT)
frm1.pack()
frm2 = Frame(root,bg='orange')
paslen = Label(frm2,text='Pass Length - ', font='arial 10 bold', bg='orange').pack(side=LEFT,padx=10,pady=10)
lenVer = StringVar()
Entry(frm2,textvariable=lenVer,font='arial 10', relief=SUNKEN, width='8').pack(side=LEFT,padx=5)
frm2.pack()
Label(root,text='*pass length must be in range 4-23.', fg='red', bg='orange').pack()
Button(root,text='Generate',font='arial 10 bold',pady='2', relief=RAISED,activebackground='gold', command=generate).pack(pady=5)

passvar = StringVar()
Entry(root,textvariable=passvar, font='arial 15', relief=SUNKEN, state=DISABLED).pack(pady=10)
frm3= Frame(root,bg='orange')
Label(frm3,text='Strength : ', font='helvetica 10',bg='orange').pack(side=LEFT)
staVar = StringVar()
# staVar.set('weak')
strengthlist = ['weak','good','strong','very strong']
for i in range (len(strengthlist)):
    radio =Radiobutton(frm3,text=strengthlist[i], variable=staVar,state=DISABLED, value=strengthlist[i],padx='5',bg='orange').pack(side=LEFT)
frm3.pack()
root.mainloop()
