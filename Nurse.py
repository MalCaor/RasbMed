#!/usr/bin/python

# All the import
from tkinter import *
from tkinter import messagebox as msg
import mysql.connector
from mysql.connector import Error

window = Tk()

window.title("welcome")
window.geometry('350x200')

lbl=Label(window, text="Hello")
lbl.grid(column=0,row=0)


txtId=Entry(window, width=10)
txtId.grid(column=1,row=0)
txtMDP=Entry(window, width=10)
txtMDP.grid(column=2,row=0)

def clicked():
    mdp = txtMDP.get()
    identifiant = txtId.get()
    with urllib.request.urlopen("http://www.btssio-carcouet.fr/ppe4/public/connect2/"+identifiant+"/"+mdp+"/infirmiere") as url:
        data = json.loads(url.read().decode())
        #print(data['id'])
        checkStatus(data, identifiant)
    
def checkStatus(json, identifiant):
    check = json.get('nom', 'id mdp invalide')
    #print(check)
    if(check == "id mdp invalide"):
        print(datetime.now())
        messagebox.showinfo("Erreur", check)
        insertBDD(identifiant, "Id/MDP", "1", "0")

# Connection DB
try :   
    Connection = mysql.connector.connect(host='localhost',
    database='Infirmerie',  
    user='nurse',
    password='nurse1')
    print("Connection database Sucessful")
except Error as e:
    print("Error Connection database",e)
    msg.showinfo("Error", "Can't connect to database")

btn = Button(window, text="Click", command=clicked)
btn.grid(column=0, row=1)

# Code
#top = tk.Tk()
# Code to add wigets will go here
#top.mainloop()