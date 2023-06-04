import tkinter as tk
from PIL import ImageTk, Image
import webbrowser

root = tk.Tk()
root.geometry("500x500")
root.title('Melody-Music Player')

img = Image.open("melo.png")
background_image = ImageTk.PhotoImage(img)

background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


def home_page(main_frame=None):
    home_frame = tk.Frame(main_frame)


    lb = tk.Label(home_frame, text='\n\n MELODY   \n\nThe Next Level in music Streaming!!\n\nDo not let the music stop!\n', font=('Poppins', 30),fg='#6A0DAD',bd=0,bg='#fff')
    lb.place(x=20000,y=20)

    lb.pack()

    home_frame.pack(pady=10)

def menu_page(main_frame=None):
    menu_frame = tk.Frame(main_frame)

    lb = tk.Label(menu_frame, text='Get ready to listen\n Top Songs of your favourite Artists!', font=('Poppins', 30),fg='#6A0DAD',bd=0,bg='#fff')

    def open_linked_page():
        linked_page = tk.Toplevel(root)
        linked_page.geometry("500x500")
        import app
        import Rainy


    def open_url(url):
        webbrowser.open_new(url)

    link_label = tk.Label(root, text="Listen Now!", font=('Poppins',30),fg='#6A0DAD',bd=0,bg='#D8BFD8', cursor="hand2")
    link_label.pack()
    link_label.bind("<Button-1>", lambda e: open_url("http://localhost:8501"))

    lb.pack()

    menu_frame.pack(pady=20)

def contact_page(main_frame=None):

    facebook_img = Image.open("facebook.png")
    twitter_img = Image.open("twitter.png")
    instagram_img = Image.open("insta.jpg")

    # Resize the images to fit in the window
    size = (50, 50)
    facebook_img = facebook_img.resize(size)
    twitter_img = twitter_img.resize(size)
    instagram_img = instagram_img.resize(size)

    # Convert the images to Tkinter-compatible format
    facebook_photo = ImageTk.PhotoImage(facebook_img)
    twitter_photo = ImageTk.PhotoImage(twitter_img)
    instagram_photo = ImageTk.PhotoImage(instagram_img)

    # Create a frame to hold the images
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=10)

    # Add the images to the frame
    facebook_label = tk.Label(frame, image=facebook_photo)
    facebook_label.grid(row=0, column=0, padx=10, pady=10)

    twitter_label = tk.Label(frame, image=twitter_photo)
    twitter_label.grid(row=0, column=1, padx=10, pady=10)

    instagram_label = tk.Label(frame, image=instagram_photo)
    instagram_label.grid(row=0, column=2, padx=10, pady=10)

    lb.place(x=20000,y=20)
    lb.pack()

    contact_frame.pack(pady=20)

def login_page(main_frame=None):
    login_frame = tk.Frame(main_frame)

    lb = tk.Label(login_frame, text='\n\n \nLogin Now ', font=('Poppins', 30),fg='#6A0DAD',bd=0,bg='#fff')
    lb.place(x=20000,y=20)
    lb.pack()

    login_frame.pack(pady=10)

def hide_indicators():
    home_indicate.config(bg='#c3c3c3')
    menu_indicate.config(bg='#c3c3c3')
    contact_indicate.config(bg='#fff')
    login_indicate.config(bg='#c3c3c3')



def indicate(lb, page):
    hide_indicators()
    lb.config(bg='#6A0DAD')

    page()

options_frame = tk.Frame(root, bg='#D8BFD8')

home_btn = tk.Button(options_frame,text='Home',font=('Poppins',20),fg='#6A0DAD',bd=0,bg='#c3c3c3',
                     command=lambda :indicate(home_indicate, home_page))
home_btn.place(x=10,y=50)

home_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
home_indicate.place(x=3, y=100, width=10, height=50)

menu_btn = tk.Button(options_frame,text='Menu',font=('Poppins',20),fg='#6A0DAD',bd=0,bg='#D8BFD8',
                     command=lambda :indicate(menu_indicate, menu_page))
menu_btn.place(x=10,y=100)

menu_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
menu_indicate.place(x=3,y=100, width=5, height=40)

contact_btn = tk.Button(options_frame,text='Contact',font=('Poppins',20),fg='#6A0DAD',bd=0,bg='#c3c3c3',
                        command=lambda :indicate(contact_indicate, contact_page))
contact_btn.place(x=10,y=150)

contact_indicate = tk.Label(options_frame, text='', bg='#fff')
contact_indicate.place(x=3,y=150, width=5, height=40)

login_btn = tk.Button(options_frame,text='Login',font=('Poppins',20),fg='#6A0DAD',bd=0,bg='#D8BFD8',
                      command=lambda :indicate(login_indicate, login_page))
login_btn.place(x=10,y=200)

login_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
login_indicate.place(x=3,y=200, width=5, height=40)

options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=150, height =400)
root.mainloop()