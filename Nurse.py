#!/usr/bin/python

# All the import
from tkinter import *
from tkinter import messagebox as msg
from bs4 import BeautifulSoup
from datetime import datetime
import mysql.connector
import urllib3, json
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
    proxies = {'http': 'http://172.30.137.29:3128'}
    print("Using HTTP proxy %s" % proxies['http'])
    http = urllib3.proxy_from_url('http://172.30.137.29:3128')
    response = http.request("GET", "http://www.btssio-carcouet.fr/ppe4/public/connect2/"+identifiant+"/"+mdp+"/infirmiere")
    soup = BeautifulSoup(response.data)
    print(soup)
    data = json.loads(str(soup.text))
    print(data)
    checkStatus(data, identifiant)
    
def checkStatus(json, identifiant):
    check = json.get('nom', 'id mdp invalide')
    if(check == "id mdp invalide"):
        print(datetime.now())
        msg.showinfo("Erreur", check)
        insertBDD(identifiant, "Id/MDP", "1", "0")
    else :
        msg.showinfo("Auth", check)
        
def insertBDD(idInf, commentaire, etape, etat):
    print("ok")
    # Connection DB
    try :
        Connection = mysql.connector.connect(host='127.0.0.1',
        database='Infirmerie',
        user='nurse',
        password='nurse1')
        print("Connection database Sucessful")
        mycursor = Connection.cursor()
        mycursor.execute("Insert into history (Idinf,commentaire,Netape,etat) values ('"+idInf+"', '"+commentaire+"', "+etape+", "+etat+");")
        Connection.commit()
    except Error as e:
        print("Error Connection database",e)

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