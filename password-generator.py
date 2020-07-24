from tkinter import *
import random
import tkinter.messagebox as tmsg

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
        if len<4:
            staVar.set('weak')
            passvar.set('to weak!')
            tmsg.askretrycancel('weak pass','Youe pass strength is too weak!\ntry a strong one.')
        elif 3<len<7:
            staVar.set('weak')
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
        svaepass.config(state=ACTIVE)
    except Exception as e:
        tmsg.showerror('error','Please enter the length!')
        passvar.set('Error')

def save():
    orgn = orgVar.get()
    strength = staVar.get()
    if strength == 'weak':
        value = tmsg.askyesno('weak pass','Your password strength is weak!\nAre sure to set this password?')
        if value == True:
            with open('pass-gen.txt','a') as f:
                f.write(f'{orgn} - {passvar.get()}\n')
    else:
        with open('pass-gen.txt','a') as f:
            f.write(f'{orgn} - {passvar.get()}\n')
    svaepass.config(state=DISABLED)
def About():
    root3=Tk()
    root3.geometry('400x400')
    Label(root3, text='by Prabal Gupta', anchor='e', fg='white', bg='black').pack(side=BOTTOM, fil=X)
    root3.configure(background='orange')
    root3.title('Password Generator- About')
    head=Label(root3, text='About', font='arial 18 bold')
    head.pack(pady='20')
    cont=Label(root3, text='Name - Password Generator\nVersion - str.PG.0.3\nDeveloper - Prabal Gupta\ngithub - https://github.com/prabal-007', font='arial 12 bold',padx='5',pady='5')
    cont.pack(pady='20')
    root3.mainloop()
def hel():
    root2=Tk()
    root2.geometry('500x400')
    root2.configure(background='orange')
    Label(root2, text='by Prabal Gupta', anchor='e', fg='white', bg='black').pack(side=BOTTOM, fil=X)
    root2.title("PassGenerator- Help")
    head=Label(root2, text='HELP', font='arial 18 bold')
    head.pack(pady='20')
    cont=Label(root2, text='Step-0. Enter organisation for which you want\n to generate password for.\nStep-2. Enter length of ypor password.\nstep-2. click Generate botton\nStep-3. Click "Save" button.\n(All the saved passwords are kept in pass-gene.txt file.\nExample : org_name - password)', font='arial 12 bold',padx='5',pady='5')
    cont.pack(pady='20')
    root2.mainloop()
def exi():
    if svaepass(state=DISABLED):
        val1 = tmsg.askyesnocancel('Error','You have not saved your password,\ndo you want to save it?')
        if val1 == 'Yes':
            save()
        elif val1 == 'No':
            exit()
    else:
        value = tmsg.askyesno('Exit','You want to Exit?')
        if value == True:
            exit()
        else: pass
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
Label(root,text='*pass length must be in range 4-22.', fg='red', bg='orange').pack()
Button(root,text='Generate',font='arial 10 bold',pady='2', relief=RAISED,activebackground='gold', command=generate).pack(pady=5)

passvar = StringVar()
Entry(root,textvariable=passvar, font='arial 15', relief=SUNKEN,width='25', state=DISABLED).pack(pady=10)
frm3= Frame(root,bg='orange')
Label(frm3,text='Strength : ', font='helvetica 10',bg='orange').pack(side=LEFT)
staVar = StringVar()
strengthlist = ['weak','good','strong','very strong']
for i in range (len(strengthlist)):
    radio =Radiobutton(frm3,text=strengthlist[i], variable=staVar,state=DISABLED, value=strengthlist[i],padx='5',bg='orange').pack(side=LEFT)
frm3.pack()
svaepass = Button(root,text='Save', font='aral 10 bold', relief=RAISED, activebackground='gold', command=save, state=DISABLED)
svaepass.pack(pady=5)
endfrm = Frame(root,bg='gold')
Label(endfrm,text="By Starkk's", bg='gold').pack(side=RIGHT)
Label(endfrm,text='©by sta.PG.0.3').pack(side=LEFT)
endfrm.pack(side=BOTTOM, fill=X)
frm4 = Frame(root,bg='orange')
Button(frm4,text='About us',bg='gray', command=About).pack(side=LEFT,padx=5,pady=2)
Button(frm4,text='Exit',bg='gray', command=exi).pack(side=LEFT,padx=5,pady=2)
Button(frm4,text='Help',bg='gray', command=hel).pack(side=LEFT,padx=5,pady=2)

frm4.pack(side=BOTTOM,fill=X,padx=120)
root.mainloop()
