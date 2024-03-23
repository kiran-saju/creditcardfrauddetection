from tkinter import *
import pandas as pd
# import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


import warnings
warnings.filterwarnings("ignore")

def final():

    global window
    window=Tk()
    window.geometry("500x400")
    window.configure(bg="#b2e1ed")
    l1=Label(window,text="Credit Card Fraud Detection",bg="white")
    l1.pack()
    e1=Label(window,text="Dataset",fg="blue",bg="#b2e1ed")
    d=Entry(window)
    e1.place(x=50,y=50)
    d.place(x=190,y=50)
    
    
        

    def test():

        data = d.get()        
        data = pd.read_csv(data)
        scaler = StandardScaler() #for normalization
        data['Amount'] = scaler.fit_transform(data[['Amount']]) #standardize trainning data
        X = data.drop('Class', axis = 1).values
        y = data['Class'].values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .2, random_state = 50)
        print("Loading Models")
        names = ['KNN', 'LogReg', 'dtree']
        scores=[]

        
        # to display of gui
        # result_label=Label(window,text=results)
        # result_label.place(x=200,y=200)
        


        models1 =KNeighborsClassifier()
        models2= LogisticRegression()
        models3= DecisionTreeClassifier()
        models4= RandomForestClassifier()
        print("KNN Evaluation")
        models1.fit(X_train, y_train) #standardize trained data
        y_pred1 = models1.predict(X_test)
        
        score1 = accuracy_score( y_test,y_pred1)
        scores.append(score1)
        print("Logistic Regression Evaluation")
        models2.fit(X_train, y_train)
        y_pred2 = models2.predict(X_test)
        
        score2 = accuracy_score( y_test,y_pred2)
        scores.append(score2)
        print("Decision tree Evaluation")
        models3.fit(X_train, y_train)
        y_pred3= models3.predict(X_test)
        
        score3= accuracy_score(y_test,y_pred3)
        scores.append(score3)

        results = pd.DataFrame({'model': names, 'score': scores})
        results.sort_values(by='score', ascending=False)
        print(results)

        # Random Forest
    
        # models4.fit(X_train, y_train)
        # y_pred4 = models4.predict(X_test)
        # score5 = accuracy_score(y_test,y_pred4)
        # print(score5)
        # scores.append(score5)
        

        
                 
         
        fraud = data[data['Class'] == 1]
        valid = data[data['Class'] == 0]
        x=len(data[data['Class'] == 1])
        y=len(data[data['Class'] == 0])
        print(x)
        fraud_label=Label(window,text="Fraud Transactions : "+str(x),bg="#b2e1ed")
        valid_label=Label(window,text="Valid Transactions : "+str(y),bg="#b2e1ed")
        fraud_label.place(x=180,y=200)
        valid_label.place(x=180,y=220)
        

        
    button=Button(window,text="Submit",command=test,bg="white")
    button.place(x=200,y=150)
    window.mainloop()

