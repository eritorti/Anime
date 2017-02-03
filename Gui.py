from tkinter import *
import sqlite3
connection=sqlite3.connect("sqlite-test.sqlite")
cursor=connection.cursor()

def cb():
    v.set("Geben sie bitte ihr Genre ein:")

def dy():
    

    
main=Tk()
main.title('Anime')
main.configure(bg="white")
main.configure(height=400,width=600)

container1=Frame(main,height=200,width=400,bg='white')
container1.pack(expand=YES)

container2=Frame(main,height=200,width=400,bg="white")
container2.pack(expand=YES)

v = StringVar()
k = StringVar()
text1=Label(container1,textvariable=v,bg="white")

#text_text1(text1)
taste1=Button(container1,text="Starten",command=cb and dy)

taste1.pack()
text1.pack()
