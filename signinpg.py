from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql


def forget_pass():
    def change_password():
        if user_entry.get() == '' or newpass_entry.get() == '' or confirmpass_entry.get() == '':
            messagebox.showerror('Error', 'All Fields Are Required', parent=window)
        elif newpass_entry.get() != confirmpass_entry.get():
            messagebox.showerror('Error', 'Password and Confirm Password are not matching', parent=window)
        else:
            con = pymysql.connect(host='localhost', user='root', password='root3110', database='userdata')
            mycursor = con.cursor()
            query = 'select * from Data where username=%s'
            mycursor.execute(query, (user_entry.get()))
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror('Error', 'Incorrect Username', parent=window)
            else:
                query = 'update data set password=%s where username=%s'
                mycursor.execute(query, (newpass_entry.get(), user_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Password is reset,please login with new password', parent=window)
                window.destroy()

    window = Toplevel()
    window.title('Change Password')

    bgPic = ImageTk.PhotoImage(file='Bg.1.png')
    bglabel = Label(window, image=bgPic)
    bglabel.grid()

    heading_label = Label(window, text='RESET PASSWORD', font=('poppins', '18', 'bold'), bg='white', fg='magenta2')
    heading_label.place(x=770, y=100)

    userLabel = Label(window, text='Username', font=('poppins', 15, 'bold'), bg='white', fg='orchid1')
    userLabel.place(x=680, y=180)

    user_entry = Entry(window, width=25, fg='magenta2', font=('poppins', 11, 'bold'), bd=0)
    user_entry.place(x=680, y=220)

    Frame(window, width=250, height=2, bg='orchid1').place(x=680, y=240)

    passwordLabel = Label(window, text=' New Password', font=('poppins', 15, 'bold'), bg='white', fg='orchid1')
    passwordLabel.place(x=680, y=280)

    newpass_entry = Entry(window, width=25, fg='magenta2', font=('poppins', 11, 'bold'), bd=0)
    newpass_entry.place(x=680, y=320)

    Frame(window, width=250, height=2, bg='orchid1').place(x=680, y=340)

    confirmpassLabel = Label(window, text=' Confirm Password', font=('poppins', 15, 'bold'), bg='white', fg='orchid1')
    confirmpassLabel.place(x=680, y=380)

    confirmpass_entry = Entry(window, width=25, fg='magenta2', font=('poppins', 11, 'bold'), bd=0)
    confirmpass_entry.place(x=680, y=420)

    Frame(window, width=250, height=2, bg='orchid1').place(x=680, y=440)

    submitButton = Button(window, text='Submit', bd=0, bg='magenta2', fg='white', font=('Poppins', '16', 'bold'),
                          width=19, cursor='hand2', activebackground='magenta2', activeforeground='white',command=change_password
                          )
    submitButton.place(x=680, y=490)

    window.mainloop()


def login_user():
 if usernameEntry.get()=='' or passwordEntry.get()=='':
     messagebox.showerror('Error','All Fields are required')

 else:
     try:
         con=pymysql.connect(host='localhost',user='root',password='root3110')
         mycursor=con.cursor()
     except:
         messagebox.showerror('Error','Connection is not established')
         return
     query = 'use userdata'
     mycursor.execute(query)
     query='select * from Data where username=%s and password=%s'
     mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
     row=mycursor.fetchone()
     if row==None:
         messagebox.showerror('Error','Invalid username or password')
     else:
         messagebox.showinfo('Welcome','Login is successful')


def signup_page():
    login.destroy()
    import signup



def hide():
    openeye.config(file='ceye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)


def show():
    openeye.config(file='open-eye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password_enter(event):
            if passwordEntry.get() == 'Password':
                passwordEntry.delete(0, END)

login=Tk()
login.geometry('1112x700+50+50')
login.resizable(0,0)
login.title('Login Page')
BgImage=ImageTk.PhotoImage(file='Bg.1.png')

BgLabel=Label(login,image=BgImage)
BgLabel.place(x=0,y=0)

heading=Label(login,text='USER LOGIN',font=('Poppins',23,'bold'),bg='white',fg='darkorchid')
heading.place(x=780,y=120)

usernameEntry=Entry(login,width=25,font=('Poppins',20,'bold'),bd=0,fg='darkorchid')
usernameEntry.place(x=700,y=200)
usernameEntry.insert(0,'Username')

usernameEntry.bind('<FocusIn>',user_enter)

frame1=Frame(login,width=315,height=2,bg='darkorchid').place(x=700,y=234)

passwordEntry=Entry(login,width=25,font=('Poppins',20,'bold'),bd=0,fg='darkorchid')
passwordEntry.place(x=700,y=300)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',password_enter)

frame2=Frame(login,width=315,height=2,bg='darkorchid').place(x=700,y=329)
openeye=PhotoImage(file='open-eye.png')
eyeButton=Button(login,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=990,y=290)

forgetButton=Button(login,text='Forgot password?',bd=0,bg='white',activebackground='white',cursor='hand2',font=('Poppins',10,'bold'),fg='darkorchid',command=forget_pass)
forgetButton.place(x=890,y=350)

loginButton=Button(login,text='Login',font=('Poppins',16,'bold')
                   ,fg='white',bg='darkorchid',activeforeground='white',activebackground='darkorchid',cursor='hand2',bd=0,width=28,command=login_user)
loginButton.place(x=700,y=420)

orLabel=Label(login,text='--------- OR ---------',font=('Poppins',16),fg='darkorchid',bg='white')
orLabel.place(x=793,y=500)

signupLabel=Label(login,text='Dont have an account?',font=('Poppins',10,'bold'),fg='darkorchid',bg='white')
signupLabel.place(x=700,y=580)

myButton=Button(login,text='SUCCCESSFULLY LOGGED IN',font=('Poppins',10,'bold underline')
                   ,fg='white',bg='white',activeforeground='white',activebackground='white',cursor='hand2',bd=0)
myButton.place(x=850,y=550)


newaccountButton=Button(login,text='Create new one',font=('Poppins',10,'bold underline')
                   ,fg='blue',bg='white',activeforeground='blue',activebackground='white',cursor='hand2',bd=0,command=signup_page)
newaccountButton.place(x=850,y=579)



login.mainloop()