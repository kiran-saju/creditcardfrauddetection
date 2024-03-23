from tkinter import *
import sqlite3
from PIL import ImageTk
import PIL.Image 
from credit_gui import *
win = Tk()

def performance_ckecking():
    w = Tk()
    w.configure(bg="white")
    def signin():
        def sign_submit():
            print(name_in.get(), age_in.get(), username_in.get(), password_in.get())
            top = sqlite3.connect("credit_check")
            n = name_in.get()
            a = age_in.get()
            u = username_in.get()
            p = password_in.get()
            top.execute("""INSERT INTO USERDATA(NAME,AGE,USERNAME,PASSWORD) VALUES (?,?,?,?)""", (n, a, u, p))
            top.commit()
            h1 = Label(w_sign, text="successfully uploaded")
            h1.pack(side=BOTTOM)
            print("successfully uploaded")

        w_sign = Tk()
        w_sign.geometry("500x400")
        w_sign.configure(bg="#b2e1ed")
        h1 = Label(w_sign, text="REGISTRATION")
        h1.pack()
        name = Label(w_sign, text="NAME")
        age = Label(w_sign, text="AGE")
        username = Label(w_sign, text="USERNAME")
        password = Label(w_sign, text="PASSWORD")
        name.place(x=50, y=50)
        age.place(x=50, y=100)
        username.place(x=50, y=150)
        password.place(x=50, y=200)
        name_in = Entry(w_sign)
        age_in = Entry(w_sign, show='*')
        username_in = Entry(w_sign)
        password_in = Entry(w_sign)
        name_in.place(x=150, y=50)
        age_in.place(x=150, y=100)
        username_in.place(x=150, y=150)
        password_in.place(x=150, y=200)
        sub = Button(w_sign, text="SUBMIT", command=sign_submit)
        sub.place(x=150, y=250)
        sub_home = Button(w_sign, text="LOGIN", command=loging)
        sub_home.place(x=230, y=250)

    def loging():
        def login_submit():
            top = sqlite3.connect("credit_check")
            print(username_in.get(), password_in.get())
            u = username_in.get()
            p = password_in.get()
            d = {}
            user_data = top.execute("SELECT * FROM USERDATA")
            for i in user_data:
                d.update({i[2]: i[3]})
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
        password_in = Entry(w_sign, show='*')
        username_in.place(x=150, y=50)
        password_in.place(x=150, y=100)
        username.place(x=50, y=50)
        password.place(x=50, y=100)
        sub = Button(w_sign, text="LOGIN", command=login_submit)
        sub.place(x=150, y=200)

    w.geometry("400x400")
    label = Label(w, text="CREDIT CARD FRAUD DETECTION", fg="blue")
    label.pack()
    sign = Button(w, text='SIGN UP', command=signin, fg="blue")
    log = Button(w, text='LOGIN', command=loging, fg="blue")
    sign.place(x=100, y=200)
    log.place(x=200, y=200)
    w.mainloop()


def fraud_check():
    wf = Tk()
    wf.configure(bg="white")
    wf.geometry("400x300")

    def checking():
        print("oj")
        top = sqlite3.connect("credituser_check")
        c=cardno.get()
        N=name.get()
        C=cvv.get()
        A=amt.get()
        country=cou.get()

        credit_data = top.execute("SELECT * FROM CREDIT")
        for i in credit_data:
            if i[2]==c: #card no
                print(1)
                
                if i[4]==country:
                    print(2)

                    if i[3]==int(C): #cvv
                        print(2)

                        if int(A)<=int(i[5]): #cash
                            print(3)
                            result=Label(wf,text="Transaction Allowed                         ",fg="blue")
                            print("Transaction Allowed")
                            result.place(x=100,y=220)
                        else:
                            result = Label(wf, text="CREDIT LIMIT EXCEEDED                    ", fg="blue")
                            result.place(x=100, y=220)
                            print("CREDIT LIMIT EXCEEDED")
                    else:
                        result = Label(wf, text="INVALID CVV                    ", fg="blue")
                        result.place(x=100, y=220)
                        print("INVALID CVV")
                else:
                    result = Label(wf, text="INVALID COUNTRY                    ", fg="blue")
                    result.place(x=100, y=220)
                    print("INVALID COUNTRY")
            else:
                result = Label(wf, text="INVALID CARD NUMBER                    ", fg="blue")
                result.place(x=100, y=220)
                print("INVALID CARD NUMBER")





    heading=Label(wf,text="Fraud Check",fg="blue")
    heading.pack()
    no=Label(wf,text="Card No",fg="blue")
    n=Label(wf,text="Name",fg="blue")
    cv=Label(wf,text="CVV",fg="blue")
    am=Label(wf,text="Amount",fg="blue")
    co = Label(wf, text="Country", fg="blue")
    cardno=Entry(wf)
    name=Entry(wf)
    cvv=Entry(wf)
    amt=Entry(wf)
    cou = Entry(wf)
    no.place(x=30,y=50)
    cardno.place(x=100, y=50)
    n.place(x=30, y=80)
    name.place(x=100, y=80)
    cv.place(x=30, y=110)
    cvv.place(x=100, y=110)
    am.place(x=30, y=130)
    amt.place(x=100, y=130)
    cou.place(x=100, y=150)
    co.place(x=30,y=150)
    final=Button(wf,text="Submit",command=checking)
    final.place(x=90,y=180)



win.geometry("500x600")
frame = Frame(win, width=800, height=400)
frame.pack()
frame.place(anchor='s', relx=0.5, rely=0.5)
img = ImageTk.PhotoImage(PIL.Image.open("D:\credit card fraud detection\intro.webp"))
label = Label(frame, image = img)
label.pack()
label1=Label(win,text="Credit card fraud is a term that has been coined for unauthorized access of payment cards")
label2=Label(win,text="like credit cards or debit cards to pay for using services or goods.Hackers or fraudsters ")
label3=Label(win,text="may obtain the confidential details of the card from unsecured websites.When a fraudster")
label4=Label(win,text="compromises an individual's credit/debit card, everyone involved in the process suffers, ")
label5=Label(win,text=" right from the individual whose confidential data has been leaked to the businesses who ")
label6=Label(win,text="issue the credit card and the merchant who is finalizing the transaction with purchase.")
label1.place(x=20,y=350)
label2.place(x=20,y=370)
label3.place(x=20,y=390)
label4.place(x=20,y=410)
label5.place(x=20,y=430)
label6.place(x=20,y=450)
b1=Button(win,text="PERFORMANCE ANALYSIS",bg="#D04628",command=performance_ckecking)
b2=Button(win,text="ACCOUNT CHECK",bg="#D04628",command=fraud_check)
b1.place(x=50,y=490)
b2.place(x=260,y=490)
win.mainloop()