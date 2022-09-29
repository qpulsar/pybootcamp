from tkinter import *
from PIL import Image, ImageTk


def login():
    global savedpassword, savedusername
    if username.get() == savedusername and password.get() == savedpassword:
        print("Hoşgeldin patron")
    else:
        print("Bu mekan size göre değil")

def signup():
    global savedpassword, savedusername
    savedusername = username.get()
    savedpassword = password.get()



root = Tk()
root.title("Login")
root.geometry("-50+100")

savedusername = "foo"
savedpassword = "bar"
f = ("Tahoma", 18)
username = StringVar()
password = StringVar()
_imguser = Image.open("user.png")
_imgpass = Image.open("password.png")
_imguser = _imguser.resize((48, 48))
_imgpass = _imgpass.resize((48, 48))

imguser = ImageTk.PhotoImage(_imguser)  # PhotoImage(file="user.png")
imgpass = ImageTk.PhotoImage(_imgpass)  # PhotoImage(file="password.png")

Label(root, image=imguser, width=48, height=48, font=f).grid(row=0, column=0)
Label(root, image=imgpass, width=48, height=48, font=f).grid(row=1, column=0)
Entry(root, textvariable=username, font=f).grid(row=0, column=1, columnspan=3)
Entry(root, show="*", textvariable=password, font=f).grid(row=1, column=1, columnspan=3)
Button(root, command=signup, text="SignUp", font=f).grid(row=2, column=0, columnspan=2)
Button(root, command=login, text="Login", font=f).grid(row=2, column=2, columnspan=2)
root.mainloop()
