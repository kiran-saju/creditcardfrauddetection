from tkinter import *
import sqlite3
from credit_gui import *
w=Tk()
w.configure(bg="white")


def signin():
    def sign_submit():
        print(name_in.get(),age_in.get(),username_in.get(),password_in.get())
        top = sqlite3.connect("credit_check")
        n=name_in.get()
        a=age_in.get()
        u=username_in.get()
        p=password_in.get()
        top.execute("""INSERT INTO USERDATA(NAME,AGE,USERNAME,PASSWORD) VALUES (?,?,?,?)""",(n,a,u,p))
        top.commit()
        h1 = Label(w_sign, text="successfully uploaded")
        h1.pack(side=BOTTOM)
        print("successfully uploaded")

    w_sign = Tk()
    w_sign.geometry("500x400")
    w_sign.configure(bg="#b2e1ed")
    h1 = Label(w_sign, text="REGISTRATION")
    h1.pack()
    name=Label(w_sign,text="NAME")
    age=Label(w_sign,text="AGE")
    username=Label(w_sign,text="USERNAME")
    password=Label(w_sign,text="PASSWORD")
    name.place(x=50,y=50)
    age.place(x=50, y=100)
    username.place(x=50, y=150)
    password.place(x=50, y=200)
    name_in=Entry(w_sign)
    age_in=Entry(w_sign,show='*')
    username_in=Entry(w_sign)
    password_in=Entry(w_sign)
    name_in.place(x=150,y=50)
    age_in.place(x=150, y=100)
    username_in.place(x=150, y=150)
    password_in.place(x=150, y=200)
    sub=Button(w_sign,text="SUBMIT",command=sign_submit)
    sub.place(x=150,y=250)
    sub_home = Button(w_sign, text="LOGIN", command=loging)
    sub_home.place(x=230, y=250)

def loging():
    def login_submit():
        top = sqlite3.connect("credit_check")
        print(username_in.get(),password_in.get())
        u=username_in.get()
        p=password_in.get()
        d={}
        user_data=top.execute("SELECT * FROM USERDATA")
        for i in user_data:
            d.update({i[2]:i[3]})
        print(d)
        if u in d:
            if d.get(u) == p:
                print("Valid user")
                final()
            else:
                print("Not valid user")
    w_sign = Tk()
    w_sign.geometry("400x300")
    w_sign.configure(bg="#b2e1ed")
    h1 = Label(w_sign, text="LOGIN PAGE")
    h1.pack()
    username = Label(w_sign, text="USERNAME")
    password = Label(w_sign, text="PASSWORD")
    username_in = Entry(w_sign)
    password_in = Entry(w_sign,show='*')
    username_in.place(x=150, y=50)
    password_in.place(x=150, y=100)
    username.place(x=50, y=50)
    password.place(x=50, y=100)
    sub = Button(w_sign, text="LOGIN", command=login_submit)
    sub.place(x=150, y=200)



w.geometry("400x400")
label=Label(w,text="CREDIT CARD FRAUD DETECTION",fg="blue")
label.pack()
sign=Button(w,text='SIGN UP',command=signin,fg="blue")
log=Button(w,text='LOGIN',command=loging,fg="blue")
sign.place(x=100,y=200)
log.place(x=200,y=200)
w.mainloop()
