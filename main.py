
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
globalUserId = "homeAutomation"
globalPass = "jyoti123"


class login_System:
    globalUserId = "homeAutomation"
    globalPass = "jyoti123"

    def __init__(self):
        self.logIn = Tk()
        self.logIn.title("LOGIN WINDOW")
        self.logIn.geometry("1000x663+300+50")
        self.logIn.resizable(False,False)

        self.load = Image.open("images/uwu.png")
        self.render = ImageTk.PhotoImage(self.load)
        self.img = Label(self.logIn, image = self.render)
        self.img.place(x=0,y=0)

        self.frameLogin = Frame(self.logIn, bg="white")
        self.frameLogin.place(x=25,y=230,height=340,width=480)

        self.title = Label(self.frameLogin, text="LOGIN HERE", font=("Impact",30,"bold"),fg="#1E8D89", bg="white").place(x=120,y=50)
        self.userNameLabel = Label(self.frameLogin, text="USERNAME",fg="#1E8D89",bg="white", font=("Goudy old style",15,"bold")).place(x=100,y=120)
        self.userName = StringVar()
        self.userNameEntry = Entry(self.frameLogin, width=30, borderwidth=3,font=(10), textvariable=self.userName, bg="#D0E2E4").place(x=100,y=150)

        self.passwordLabel=Label(self.frameLogin, text="PASSWORD",fg="#1E8D89",bg="white", font=("Goudy old style",15,"bold")).place(x=100,y=190)
        self.password = StringVar()
        self.passwordEntry= Entry(self.frameLogin, width=30, borderwidth=3,font=(10),show="*", textvariable=self.password, bg="#D0E2E4").place(x=100,y=220)

        self.loginButton = Button(self.frameLogin, text="Log In",bg="#1E8D89",fg="white",font=("Goudy old style",15,"bold"), command=self.validateLogin).place(x=150,y=260)

    def validateLogin(self):
        if self.userName.get()=="" or self.password.get()=="":
            messagebox.showerror("All fields are required!!",parent=self.logIn)
        elif self.userName.get()!="homejyoti" or self.password.get()=="jyoti1234":
            messagebox.showerror("Error","Invalid Username/Password",parent=self.logIn)
        else:
            messagebox.showinfo("Error","Welcome to your Home Automation System", parent = self.logIn)



    def run(self):
        self.logIn.mainloop()

logIn = login_System()
logIn.run()


