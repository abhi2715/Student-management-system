from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox, ttk
import sqlite3
import os


class Login:
    def __init__(self, home):
        self.home = home
        self.home.title("Login System")
        self.home.geometry("1400x700+0+0")


        self.bg = ImageTk.PhotoImage(file="images/6.1.jpg")
        self.bg_image = Label(self.home, image=self.bg)
        self.bg_image.place(x=0, y=0, relwidth=1, relheight=1)
        footer=Label(self.home,text="©Abhishek KS, 2024",font=("Calibri",13,"bold"),fg="black").pack(side=BOTTOM)


        Frame_login = Frame(self.home, bg="#172E36")
        Frame_login.place(x=530, y=100, height=600, width=500)

        title = Label(Frame_login, text="User Login", font=("Calibri", 25, "bold"), bg="#172E36", fg="#D0A85B" )
        title.place(x=180, y=90)

        lbl_user = Label(Frame_login, text="User Name", font=("Calibri", 15, "bold"), bg="#172E36", fg="#D0A85B")
        lbl_user.place(x=45, y=200)
        self.txt_user = Entry(Frame_login, font=("Calibri", 15), bg="white")
        self.txt_user.place(x=45, y=230, width=300, height=35)

        lbl_pass = Label(Frame_login, text="Password", font=("Calibri", 15, "bold"), bg="#172E36", fg="#D0A85B")
        lbl_pass.place(x=45, y=300)
        self.txt_pass = Entry(Frame_login, font=("Calibri", 15), bg="white", show=".")
        self.txt_pass.place(x=45, y=330, width=300, height=35)

        forget = Button(Frame_login, text="Forget Password?", cursor="hand2", command=self.forget_passwd, bg="#172E36", fg="#D0A85B"
                        , font=("Calibri", 15, "bold"))
        forget.place(x=320, y=440)

        self.icon = ImageTk.PhotoImage(file="Images/logo2.png")  # replace with your image path
        icon_label = Label(Frame_login, image=self.icon, bg="#172E36")
        icon_label.place(x=320, y=30, width=150, height=50)  # adjust x and y coordinates as needed

        self.icon2 = ImageTk.PhotoImage(file="Images/logo.png")  # replace with your image path
        icon_label2 = Label(Frame_login, image=self.icon2, bg="#172E36")
        icon_label2.place(x=0, y=-0, width=250, height=100)  # adjust x and y coordinates as needed

        signup = Button(Frame_login, text="Sign Up", cursor="hand2", command=self.register_window, bg="#D0A85B",
                       fg="white", font=("Calibri", 20, "bold"))
        signup.place(x=200, y=540, width=100, height=50)

        login = Button(Frame_login, command=self.login_function, text="Login", cursor="hand2", bg="#D0A85B",
                       fg="white", font=("Calibri", 20, "bold"))
        login.place(x=200, y=370, width=100, height=50)

        lbl_create = Label(Frame_login, text="Do not have an account?", font=("Calibri", 15, "bold"), bg="#172E36", fg="#D0A85B")
        lbl_create.place(x=140, y=510)

        UserType = Label(Frame_login, text="User : ", font=("times new roman", 15, "bold"), bg="#172E36", fg="#D0A85B")
        UserType.place(x=45, y=145)
        self.txt_UserType = ttk.Combobox(Frame_login, font=("times new roman", 13), state="readonly", justify=CENTER)
        self.txt_UserType['values'] = ("Select", "Student", "Admin")
        self.txt_UserType.place(x=120, y=145, width=120, height=30)
        self.txt_UserType.current(0)

    def reset(self):
        self.txt_pass.delete(0, END)
        self.txt_user.delete(0, END)

    def forget_passwd(self):
        if self.txt_user.get() == "":
            messagebox.showerror("Error", "Please enter email to retrieve your password", parent=self.home)
        else:
            try:
                conn = sqlite3.connect(database="ResultManagementSystem.db")
                cur = conn.cursor()
                cur.execute("Select * from AllUsers where email=?", (self.txt_user.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Please enter a valid email address to retrieve your password",
                                         parent=self.home)
                else:
                    password = row[1]  # Assuming the password is in the second column
                    messagebox.showinfo("Password Retrieved", f"Your password is: {password}", parent=self.home)
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.home)

    def register_window(self):
        self.home.destroy()
        import Register

    def login_function(self):
        if self.txt_pass.get() == "" or self.txt_user.get() == "" or self.txt_UserType.get() == "Select":
            messagebox.showerror("Error", "All fields are required", parent=self.home)
        else:
            try:
                conn = sqlite3.connect(database="ResultManagementSystem.db")
                cur = conn.cursor()
                cur.execute("Select * from AllUsers where email=? and password=? and u_name=?",
                            (self.txt_user.get(), self.txt_pass.get(), self.txt_UserType.get()))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Username or Password or UserType", parent=self.home)
                else:
                    if self.txt_UserType.get() == "Student":
                        messagebox.showinfo("Success", f"Welcome :- {self.txt_user.get()}", parent=self.home)
                        self.home.destroy()
                        os.system("python dashboardStudent.py")
                    else:
                        messagebox.showinfo("Success", f"Welcome :- {self.txt_user.get()}", parent=self.home)
                        self.home.destroy()
                        os.system("python dashboard.py")
                    conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.home)


home = Tk()
obj = Login(home)
home.mainloop()
