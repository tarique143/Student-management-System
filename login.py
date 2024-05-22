from tkinter import *
from tkinter import messagebox
from PIL import ImageTk


def login():
    if(useerNameEntry.get()==''or passwordNameEntry.get()==''):
        messagebox.showerror('error','Fields cannot be empyt')
    elif useerNameEntry.get()=='tarique'and passwordNameEntry.get()=='1234':
        messagebox.showinfo('Success','Welcome')
        window.destroy()
        import sms
      
    else:
        messagebox.showerror('Error','Please enter correct credentials')
       
        
        

window = Tk()
window.geometry('1280x700+0+0')
#window.resizable(False, False)

backgroundImg = ImageTk.PhotoImage(file='img/bgi.jpg')
bglabel = Label(window, image=backgroundImg)
bglabel.place(x=0,y=0)

loginframe = Frame(window,bg='white')
loginframe.place(x=400, y=150)

logoImage = PhotoImage(file='img/login.png')
logoLabel = Label(loginframe, image=logoImage)
logoLabel.grid(row=0, column=0 ,columnspan=2,pady=10)

usernameimg = PhotoImage(file='img/user.png')
userLabel = Label(loginframe, image=usernameimg, text='Username', compound=LEFT,
                  font=('time new roman', 17, 'bold'),bg='white')
userLabel.grid(row=1, column=0,pady=10,padx=20)
useerNameEntry=Entry(loginframe,font=('time new roman', 15, 'bold'),fg='royalblue')
useerNameEntry.grid(row=1, column=1 ,pady=10,padx=20)
passwordimg = PhotoImage(file='img/passimg.png')
passqordLabel = Label(loginframe, image=passwordimg, text='Password', compound=LEFT,
                  font=('time new roman', 17, 'bold'),bg='white')
passqordLabel.grid(row=2, column=0,pady=10,padx=20)
passwordNameEntry=Entry(loginframe,font=('time new roman', 15, 'bold'),fg='royalblue')
passwordNameEntry.grid(row=2, column=1 ,pady=10,padx=20)
loginButton=Button(loginframe,text='Login',font=('time new roman', 15, 'bold'),fg='white',width=10
                   ,bg='cornflowerblue', activebackground='cornflowerblue',cursor='hand2', command=login)
loginButton.grid(row=3,column=1,pady=10)

window.mainloop()
