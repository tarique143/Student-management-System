from tkinter import *
import pymysql
from ttkthemes import ThemedTk
from tkinter import ttk,messagebox,filedialog
import time
import pandas


# functionality part
def iexit():
  result=messagebox.askyesno('Confirm','Do you want to exit')
  if result:
    root.destroy()
  else:
    pass

#export data function
def export_data():
  url= filedialog.asksaveasfile(defaultextension='.csv')
  print(url)
  indexing=StudentTable.get_children()
  newlist=[]
  for index in indexing:
    content=StudentTable.item(index)
    datalist=content['values']
    newlist.append(datalist)
  
  table=pandas.DataFrame(newlist,columns=['Id','Student_name','Mobile','Email','address','Gender','D.O.B','Added Date','Added Time'])
  table.to_csv(url,index=False)
  messagebox.showinfo('success','Data is save successfully')
 
    
  



#update function
def update_student():
  def update_data():
    query = 'UPDATE students SET Student_Name=%s, Mobile_No=%s, Email=%s, Address=%s, Gender=%s, D_O_B=%s, Added_Date=%s, Added_Time=%s WHERE id=%s'

    mycursor.execute(query,(nameEntry.get(), mobileEntry.get(), emailEntry.get(), addressEntry.get(), genderEntry.get(),dobEntry.get(),date,currenttime,idEntry.get()))
    con.commit()
    messagebox.showinfo('success',f'Id{idEntry.get()} is modified successfully',parent=update_window)
    update_window.destroy()
    show_student()
    
    
    
  update_window=Toplevel()
  #update_window.destroy()
  update_window.resizable(False,False)
  update_window.grab_set()
  idLable=Label(update_window,text='Id',font=('time new roman',20,'bold'))
  idLable.grid(row=0,column=0,padx=30,pady=15 )
  idEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
  idEntry.grid(row=0,column=1,pady=30,padx=30)
  
  nameLable=Label(update_window,text='Name',font=('time new roman',20,'bold'))
  nameLable.grid(row=1,column=0,padx=30,pady=15 )
  nameEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
  nameEntry.grid(row=1,column=1,pady=15,padx=10)
  
  mobileLable=Label(update_window,text='Mobile_NO',font=('time new roman',20,'bold'))
  mobileLable.grid(row=2,column=0,padx=30,pady=15 )
  mobileEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
  mobileEntry.grid(row=2,column=1,pady=15,padx=10)
  
  emailLable=Label(update_window,text='Email',font=('time new roman',20,'bold'))
  emailLable.grid(row=3,column=0,padx=30,pady=15 )
  emailEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
  emailEntry.grid(row=3,column=1,pady=15,padx=10)
  
  addressLable=Label(update_window,text='Address',font=('time new roman',20,'bold'))
  addressLable.grid(row=4,column=0,padx=30,pady=15 )
  addressEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
  addressEntry.grid(row=4,column=1,pady=15,padx=10)
  
  genderLable=Label(update_window,text='Gender',font=('time new roman',20,'bold'))
  genderLable.grid(row=5,column=0,padx=30,pady=15 )
  genderEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
  genderEntry.grid(row=5,column=1,pady=15,padx=10)
  
  dobLable=Label(update_window,text='D.O.B',font=('time new roman',20,'bold'))
  dobLable.grid(row=6,column=0,padx=30,pady=15 )
  dobEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
  dobEntry.grid(row=6,column=1,pady=15,padx=10)
  
  
  search_student_button=ttk.Button(update_window,text='Update',command=update_data )
  search_student_button.grid(row=7,columnspan=2,padx=20)
  
  indexing=StudentTable.focus()
  content=StudentTable.item(indexing)
   
  listdata=content['values']
  idEntry.insert(0,listdata[0])
  nameEntry.insert(0,listdata[1])
  mobileEntry.insert(0,listdata[2])
  emailEntry.insert(0,listdata[3])
  addressEntry.insert(0,listdata[4])
  genderEntry.insert(0,listdata[5])
  
  
  dobEntry.insert(0,listdata[6])
  
#show studnt details
def show_student():
  query='select * from students'
  mycursor.execute(query)
  fetched_data=mycursor.fetchall()
  StudentTable.delete(*StudentTable.get_children())
  for data in fetched_data:
    StudentTable.insert('',END,values=data)
  
  pass

#delete function
def delete_student():
  indexing=StudentTable.focus()
  
  content=StudentTable.item(indexing)
  content_id=content['values'][0]
  query='delete from students where id=%s'
  mycursor.execute(query,content_id)
  con.commit()
  messagebox.showinfo('Deleted ', f'This Id {content_id} is deleted succesfully')
  query='select * from students'
  mycursor.execute(query)
  fetched_data=mycursor.fetchall()
  StudentTable.delete(*StudentTable.get_children())
  for data in fetched_data:
    StudentTable.insert('',END,values=data)
  
# search student 
def search_student():
  
  def search_data():
    mycursor = con.cursor()
    query = '''SELECT * FROM students 
               WHERE Id=%s OR Student_Name=%s OR Mobile_No=%s OR Email=%s OR Address=%s OR Gender=%s'''
    mycursor.execute(query, (idEntry.get(), nameEntry.get(), mobileEntry.get(), emailEntry.get(), addressEntry.get(), genderEntry.get()))
    StudentTable.delete(*StudentTable.get_children())
    fetched_data = mycursor.fetchall()
    for data in fetched_data:
        StudentTable.insert('', END, values=data)
        search_window.destroy()

    
    
    
  search_window=Toplevel()
  #search_window.destroy()
  search_window.resizable(False,False)
  search_window.grab_set()
  idLable=Label(search_window,text='Id',font=('time new roman',20,'bold'))
  idLable.grid(row=0,column=0,padx=30,pady=15 )
  idEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
  idEntry.grid(row=0,column=1,pady=30,padx=30)
  
  nameLable=Label(search_window,text='Name',font=('time new roman',20,'bold'))
  nameLable.grid(row=1,column=0,padx=30,pady=15 )
  nameEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
  nameEntry.grid(row=1,column=1,pady=15,padx=10)
  
  mobileLable=Label(search_window,text='Mobile_NO',font=('time new roman',20,'bold'))
  mobileLable.grid(row=2,column=0,padx=30,pady=15 )
  mobileEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
  mobileEntry.grid(row=2,column=1,pady=15,padx=10)
  
  emailLable=Label(search_window,text='Email',font=('time new roman',20,'bold'))
  emailLable.grid(row=3,column=0,padx=30,pady=15 )
  emailEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
  emailEntry.grid(row=3,column=1,pady=15,padx=10)
  
  addressLable=Label(search_window,text='Address',font=('time new roman',20,'bold'))
  addressLable.grid(row=4,column=0,padx=30,pady=15 )
  addressEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
  addressEntry.grid(row=4,column=1,pady=15,padx=10)
  
  genderLable=Label(search_window,text='Gender',font=('time new roman',20,'bold'))
  genderLable.grid(row=5,column=0,padx=30,pady=15 )
  genderEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
  genderEntry.grid(row=5,column=1,pady=15,padx=10)
  
  dobLable=Label(search_window,text='D.O.B',font=('time new roman',20,'bold'))
  dobLable.grid(row=6,column=0,padx=30,pady=15 )
  dobEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
  dobEntry.grid(row=6,column=1,pady=15,padx=10)
  
  
  search_student_button=ttk.Button(search_window,text='Search Student',command=search_data )
  search_student_button.grid(row=7,columnspan=2,padx=20)
 
  
# add student part
def addStudent():
  def add_data():
    if idEntry.get()==''or nameEntry.get()==''or mobileEntry.get()=='' or emailEntry.get()==''or addressEntry.get()==''or genderEntry.get()==''or dobEntry.get()=='':
      messagebox.showerror('error','all fields are required',parent=add_Window)
    else:
       
      try:
        query = "INSERT INTO  students (Id, Student_Name, Mobile_No, Email, Address, Gender, D_O_B, Added_Date, Added_Time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (idEntry.get(), nameEntry.get(), mobileEntry.get(), emailEntry.get(), addressEntry.get(), genderEntry.get(), dobEntry.get(), date, currenttime)

        mycursor.execute(query,values)
        con.commit()
        result=messagebox.askyesno('Confirm','Data added successfully. Doyou want to clean the form?' )
        if result:
          idEntry.delete(0,END)
          nameEntry.delete(0,END)
          mobileEntry.delete(0,END)
          emailEntry.delete(0,END)
          addressEntry.delete(0,END)
          genderEntry.delete(0,END)
          dobEntry.delete(0,END) 
        else:
          pass
      except:
        messagebox.showerror('erroe','id can not be repeqted',parent=add_Window)
        return
        
    
      query='select * from  students'
      mycursor.execute(query)
      fetched_data=mycursor.fetchall()
      StudentTable.delete(*StudentTable.get_children())
      for data in fetched_data:
       # dataList=list(data)
        StudentTable.insert('',END,values=data)

        
  add_Window=Toplevel()
  add_Window.resizable(False,False)
  add_Window.grab_set()
  idLable=Label(add_Window,text='Id',font=('time new roman',20,'bold'))
  idLable.grid(row=0,column=0,padx=30,pady=15 )
  idEntry=Entry(add_Window,font=('roman',15,'bold'),width=24)
  idEntry.grid(row=0,column=1,pady=30,padx=30)
  
  nameLable=Label(add_Window,text='Name',font=('time new roman',20,'bold'))
  nameLable.grid(row=1,column=0,padx=30,pady=15 )
  nameEntry=Entry(add_Window,font=('roman',15,'bold'),width=24)
  nameEntry.grid(row=1,column=1,pady=15,padx=10)
  
  mobileLable=Label(add_Window,text='Mobile_NO',font=('time new roman',20,'bold'))
  mobileLable.grid(row=2,column=0,padx=30,pady=15 )
  mobileEntry=Entry(add_Window,font=('roman',15,'bold'),width=24)
  mobileEntry.grid(row=2,column=1,pady=15,padx=10)
  
  emailLable=Label(add_Window,text='Email',font=('time new roman',20,'bold'))
  emailLable.grid(row=3,column=0,padx=30,pady=15 )
  emailEntry=Entry(add_Window,font=('roman',15,'bold'),width=24)
  emailEntry.grid(row=3,column=1,pady=15,padx=10)
  
  addressLable=Label(add_Window,text='Address',font=('time new roman',20,'bold'))
  addressLable.grid(row=4,column=0,padx=30,pady=15 )
  addressEntry=Entry(add_Window,font=('roman',15,'bold'),width=24)
  addressEntry.grid(row=4,column=1,pady=15,padx=10)
  
  genderLable=Label(add_Window,text='Gender',font=('time new roman',20,'bold'))
  genderLable.grid(row=5,column=0,padx=30,pady=15 )
  genderEntry=Entry(add_Window,font=('roman',15,'bold'),width=24)
  genderEntry.grid(row=5,column=1,pady=15,padx=10)
  
  dobLable=Label(add_Window,text='D.O.B',font=('time new roman',20,'bold'))
  dobLable.grid(row=6,column=0,padx=30,pady=15 )
  dobEntry=Entry(add_Window,font=('roman',15,'bold'),width=24)
  dobEntry.grid(row=6,column=1,pady=15,padx=10)
  
  
  add_student_button=ttk.Button(add_Window,text='Add Student',command=add_data)
  add_student_button.grid(row=7,columnspan=2,padx=20)
  
   
  

#database partfunction
def connect_database():
  
  
  def connect():
    global mycursor
    global con 
    try:
      con=pymysql.connect(host='localhost',user= 'root',password= 'root')
      mycursor=con.cursor()
       
    except:
      messagebox.showerror('Erroe','invalid details',parent=connectWindow)
      return
    try:
      query='create database studentmanagementsystem'
      mycursor.execute(query)
      query='use studentmanagementsystem'
      mycursor.execute(query)
      query='CREATE TABLE students (Id INT AUTO_INCREMENT PRIMARY KEY,Student_Name VARCHAR(255),Mobile_No VARCHAR(15),Email VARCHAR(255),Address VARCHAR(255),Gender VARCHAR(12) ,D_O_B VARCHAR(25) ,Added_Date VARCHAR(25),Added_Time VARCHAR(25))'
      mycursor.execute(query)
    except:
      query='use studentmanagementsystem '
      mycursor.execute(query)
    messagebox.showinfo('success', 'databases connection is successfull')
    connectWindow.destroy()
    addstudentButton.config(state=NORMAL)
    searchstudentButton.config(state=NORMAL)
    updatestudentButton.config(state=NORMAL)
    showstudentButton.config(state=NORMAL)
    exitstudentButton.config(state=NORMAL)
    deletestudentButton.config(state=NORMAL)
    exitstudentButton.config(state=NORMAL)
  
  
  connectWindow=Toplevel()
  connectWindow.grab_set()
  connectWindow.geometry('470x250+730+230')
  connectWindow.title('Database connection')
  root.resizable(0,0)
  
  
  hostNmaeLabel=Label(connectWindow,text='Host name',font=('arial',20,'bold'))
  hostNmaeLabel.grid(row=0,column=0)
  hostEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
  hostEntry.grid(row=0,column=1,padx=40,pady=20)
  
  userLabel=Label(connectWindow,text='User Name',font=('arial',20,'bold'))
  userLabel.grid(row=1,column=0)
  userEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
  userEntry.grid(row=1,column=1,padx=40,pady=20)
  
  passwordLabel=Label(connectWindow,text='Password',font=('arial',20,'bold'))
  passwordLabel.grid(row=3,column=0)
  passwordEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
  passwordEntry.grid(row=3,column=1,padx=40,pady=20)
  
  connectButton=ttk.Button(connectWindow,text='Connect',command=connect)
  connectButton.grid(row=4,columnspan=2)
  
  
  
  

count = 0
text = ''

# slider function
def slider():
    global text, count
    if count == len(s):
        count = 0
        text = ''
    text = text + s[count]
    sliderLable.config(text=text)
    count += 1
    sliderLable.after(300, slider)

# clock function
def clock():
    global date,currenttime
    date = time.strftime('%d/%m/%Y')
    currenttime = time.strftime('%H:%M:%S')
    datetimeLable.config(text=f'    Date:{date}\n Time:{currenttime}')
    datetimeLable.after(1000, clock)

# gui part
root = ThemedTk()
root.get_themes()
root.set_theme('radiance')

root.geometry('1280x700+50+20')
root.resizable(0, 0)
root.title('Student Management System')

# clock
datetimeLable = Label(root, text='hello', font=('time new roman', 18, 'bold'))
datetimeLable.place(x=5, y=5)
clock()

# slider of student management system
s = 'Student Management System'
sliderLable = Label(root, font=('Arial', 28, 'italic bold'), width=40)
sliderLable.place(x=200, y=0)
slider()

# connect button of database
connectButton = ttk.Button(root, text='connect database',command=connect_database)
connectButton.place(x=980, y=0)

# left frame logo
leftFrame = Frame(root)
leftFrame.place(x=50, y=80, width=300, height=600)
logo_image = PhotoImage(file='img/student.png')
logo_Lable = Label(leftFrame, image=logo_image)
logo_Lable.grid(row=0, column=0)

# left frame buttons
addstudentButton = ttk.Button(leftFrame, text='Add Student', width=25  , command=addStudent)
addstudentButton.grid(row=1, column=0, pady=20)

searchstudentButton = ttk.Button(leftFrame, text='Search Student', width=25 ,command=search_student)
searchstudentButton.grid(row=2, column=0, pady=20)

deletestudentButton = ttk.Button(leftFrame, text='delete Student', width=25,command=delete_student )
deletestudentButton.grid(row=3, column=0, pady=20)

updatestudentButton = ttk.Button(leftFrame, text='update Student', width=25 ,command=update_student)
updatestudentButton.grid(row=4, column=0, pady=20)

showstudentButton = ttk.Button(leftFrame, text='Show Student', width=25 ,command=show_student)
showstudentButton.grid(row=5, column=0, pady=20)

exportstudentButton = ttk.Button(leftFrame, text='Export Data', width=25 ,command=export_data)
exportstudentButton.grid(row=6, column=0, pady=20)

exitstudentButton = ttk.Button(leftFrame, text='Exit', width=25,command=iexit)
exitstudentButton.grid(row=7, column=0, pady=20)

# right frame
rightFrame = Frame(root,)
rightFrame.place(x=350, y=80, width=820, height=600)
ScrollbarX=Scrollbar(rightFrame,orient=HORIZONTAL)
Scrollbary=Scrollbar(rightFrame,orient=VERTICAL)

StudentTable = ttk.Treeview(rightFrame, columns=('Id', 'Name', 'Mobile No', 'Email', 'Address', 'Gender',
                                                  'D.O.B', 'Added Date', 'Added Time')
                           , xscrollcommand=ScrollbarX.set,yscrollcommand=Scrollbary.set)
ScrollbarX.config(command=StudentTable.xview)
Scrollbary.config(command=StudentTable.yview)

ScrollbarX.pack(side=BOTTOM,fill=X)
Scrollbary.pack(side=RIGHT,fill=Y)
StudentTable.pack(fill=BOTH, expand=1)
StudentTable.heading('Id', text='Id')
StudentTable.heading('Name', text='Name')
StudentTable.heading('Mobile No', text='Mobile No')
StudentTable.heading('Email', text='Email')
StudentTable.heading('Address', text='Address')
StudentTable.heading('Gender', text='Gender')
StudentTable.heading('D.O.B', text='D.O.B')
StudentTable.heading('Added Date', text='Added Date')
StudentTable.heading('Added Time', text='Added Time')

StudentTable.column('Id',width=50,anchor='center')
StudentTable.column('Name',width=200,anchor='center')
StudentTable.column('Mobile No',width=200,anchor='center')
StudentTable.column('Email',width=200,anchor='center')
StudentTable.column('Address',width=300,anchor='center')
StudentTable.column('Gender',width=200,anchor='center')
StudentTable.column('D.O.B',width=200,anchor='center')
StudentTable.column('Added Date',width=200,anchor='center')
StudentTable.column('Added Time',width=200,anchor='center')

style=ttk.Style()
style.configure('Treeview',rowheight=40,font=('arial,',15,'bold'),foreground='red4',background='white',fieldbackground='white')



StudentTable.config(show='headings')


root.mainloop()
