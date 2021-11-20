from tkinter import *
import tkinter
def getdata():
    x=value.get()
    lab = Label(window,x).pack()
    
root = Tk()
root.geometry("590x390")
root.resizable(False,False)
root.title("Corona tracker Login Page")
"""l1=Label(root,text="hello").pack()
bt=Button(root,text="click",command=func()).pack()"""
users=tkinter.StringVar()
passod=tkinter.StringVar()
value=tkinter.StringVar()
 
lab=Label(root,text="Login Page", background="yellow",font=("sansserif",20),border=5).pack(side="top")
u = Label(root,text="UserName : ").place(x=40,y=80)
p = Label(root,text="Password : ").place(x=40,y=120)
user = Entry(root,width="30").place(x=140,y=80)
passo = Entry(root,width="30").place(x=140,y=120)
btn = Button(root,text="Log in").place(x=140,y=150)
window = Toplevel(root)
window.geometry("590x390")
window.title("Data Page")
l=Label(window,text="Enter the country Name").place(x=250,y=200)
c=Entry(window,textvariable="value").place(x=250,y=250)
bt=Button(window,text="Submit",background="yellow",command=getdata).place(x=50,y=100)

root.mainloop()