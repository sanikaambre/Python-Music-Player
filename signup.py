from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql


def home_page():
    signup.destroy()
    import homepage
def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmEntry.delete(0,END)
    check.set(0)



def connect_database():
    if emailEntry.get() == '' or usernameEntry.get() == '' or passwordEntry.get() == '' or confirmEntry.get() == '':
        messagebox.showerror('Error', 'All fields are required')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error', 'Password Mismatch')
    elif check.get() == 0:
        messagebox.showerror('Error', 'Please accept Terms & Conditions')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='root3110')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity Issue,Please Try Again')
            return

        try:
            query = 'create database userdata'
            mycursor.execute(query)
            query = 'use userdata'
            mycursor.execute(query)
            query = 'create table Data(Email varchar(50),Username varchar(50),Password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')

        query = 'select * from Data where username=%s'
        mycursor.execute(query, (usernameEntry.get()))
        row = mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error', 'Username already exists')

        else:
            query = 'Insert Into Data(Email,Username,Password) values(%s,%s,%s)'
            mycursor.execute(query, (emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Registration is Successful')
            clear()


signup=Tk()
signup.title('Signup Page')
signup.resizable(False,False)

background=ImageTk.PhotoImage(file='Bg.1.png')

bgLabel=Label(signup,image=background)
bgLabel.grid()

frame=Frame(signup,bg='white')
frame.place(x=640,y=96)

heading=Label(frame,text='CREATE AN ACCOUNT',font=('Poppins',30,'bold'),bg='white',fg='darkorchid')
heading.grid(row=0,column=0,padx=10,pady=10)

emailLabel=Label(frame,text='Email',font=('Poppins',13,'bold'),bg='white',fg='darkorchid')
emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))

emailEntry=Entry(frame,width=40,font=('Poppins',13,'bold'),fg='white',bg='darkorchid')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)

usernameLabel=Label(frame,text='Username',font=('Poppins',13,'bold'),bg='white',fg='darkorchid')
usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))

usernameEntry=Entry(frame,width=40,font=('Poppins',13,'bold'),fg='white',bg='darkorchid')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)

passwordLabel=Label(frame,text='Password',font=('Poppins',13,'bold'),bg='white',fg='darkorchid')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))

passwordEntry=Entry(frame,width=40,font=('Poppins',13,'bold'),fg='white',bg='darkorchid')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)

confirmLabel=Label(frame,text='Confirm Password',font=('Poppins',13,'bold'),bg='white',fg='darkorchid')
confirmLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))

confirmEntry=Entry(frame,width=40,font=('Poppins',13,'bold'),fg='white',bg='darkorchid')
confirmEntry.grid(row=8,column=0,sticky='w',padx=25)

check=IntVar()
termsandconditions=Checkbutton(frame,text='I agree to the Terms & Conditions',font=('Poppins',9,'bold'),
                               fg='darkorchid',bg='white',activebackground='white',activeforeground='darkorchid',cursor='hand2',variable=check)
termsandconditions.grid(row=9,column=0,pady=20,padx=10)

signupButton=Button(frame,text='Signup',font=('Poppins',16,'bold'),bd=0,bg='darkorchid',fg='white',activebackground='darkorchid',activeforeground='white',width=17,command=connect_database)
signupButton.grid(row=10,column=0,pady=10)

alreadyaccount=Label(frame,text='Ready for the music?',font=('Poppins',9,'bold'),bg='white',fg='darkorchid')
alreadyaccount.grid(row=11,column=0,sticky='w',padx=25,pady=10)

loginButton=Button(frame,text='Lets start',font=('Poppins',15,'bold underline'),bg='white',fg='darkorchid',bd=0,cursor='hand2',activebackground='white',activeforeground='darkorchid',command=home_page)
loginButton.place(x=170,y=434)

signup.mainloop()