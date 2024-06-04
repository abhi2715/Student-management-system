from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3
import os

class Register:
    def __init__(self, home):
        self.home = home
        self.home.title("Registration Window")
        self.home.geometry("1350x900+0+0")
        self.home.config(bg="white")

        # Background Image
        self.bg = ImageTk.PhotoImage(file="Images/6.1.jpg")
        bg = Label(self.home, image=self.bg)
        bg.place(x=0, y=0, relwidth=1, relheight=1)
        footer=Label(self.home,text="©Abhishek KS, 2024",font=("Calibri",13,"bold"),fg="black").pack(side=BOTTOM)


        # Register Frame
        frame1 = Frame(self.home, bg="#172E36", bd=2, relief=SOLID)
        frame1.place(x=430, y=120, width=700, height=500)

        # Load and place the image beside the title
        self.icon = ImageTk.PhotoImage(file="Images/logo.png")  # replace with your image path
        icon_label = Label(frame1, image=self.icon, bg="#172E36")
        icon_label.place(x=10, y=-200, relheight=1, relwidth=1)  # adjust x and y coordinates as needed

        # First Name
        self.var_fname = StringVar()
        f_name = Label(frame1, text="Name", font=("Calibri", 15, "bold"), bg="#172E36", fg="#D0A85B")
        f_name.place(x=50, y=100)
        self.txt_fname = Entry(frame1, font=("Calibri", 15), bg="white", relief=GROOVE)
        self.txt_fname.place(x=50, y=130, width=250)

        # Contact No.
        contact = Label(frame1, text="Contact No.", font=("Calibri", 15, "bold"), bg="#172E36", fg="#D0A85B")
        contact.place(x=50, y=170)
        self.txt_contact = Entry(frame1, font=("Calibri", 15), bg="white", relief=GROOVE)
        self.txt_contact.place(x=50, y=200, width=250)

        # Email
        email = Label(frame1, text="Email", font=("Calibri", 15, "bold"), bg="#172E36", fg="#D0A85B")
        email.place(x=370, y=170)
        self.txt_email = Entry(frame1, font=("Calibri", 15), bg="white", relief=GROOVE)
        self.txt_email.place(x=370, y=200, width=250)

        # Password
        password = Label(frame1, text="Password", font=("Calibri", 15, "bold"), bg="#172E36", fg="#D0A85B")
        password.place(x=50, y=240)
        self.txt_password = Entry(frame1, font=("Calibri", 15), bg="white",  relief=GROOVE)
        self.txt_password.place(x=50, y=270, width=250)

        # Confirm Password
        cpassword = Label(frame1, text="Confirm Password", font=("Calibri", 15, "bold"),bg="#172E36", fg="#D0A85B")
        cpassword.place(x=370, y=240)
        self.txt_cpassword = Entry(frame1, font=("Calibri", 15), bg="white", relief=GROOVE)
        self.txt_cpassword.place(x=370, y=270, width=250)

        # User Type
        UserType = Label(frame1, text="User", font=("Calibri", 15, "bold"), bg="#172E36", fg="#D0A85B")
        UserType.place(x=220, y=310)
        self.txt_UserType = ttk.Combobox(frame1, font=("Calibri", 13), state="readonly", justify=CENTER)
        self.txt_UserType['values'] = ("Select", "Student", "Admin")
        self.txt_UserType.place(x=270, y=310, width=100)
        self.txt_UserType.current(0)

        # Terms and Conditions
        self.var_chk = IntVar()
        chk = Checkbutton(frame1, text="I agree To follow the rules and regulations of the university", variable=self.var_chk, onvalue=1, offvalue=0,font=("Calibri", 12))
        chk.place(x=50, y=360)

        # Sign Up Button
        btn_register = Button(frame1, text="Sign Up", command=self.register_data, font=("Calibri", 20, "bold"),
                              bg="#D0A85B", fg="white", relief=RAISED)
        btn_register.place(x=150, y=430)

        # Already Registered Label
        lbl_already_registered = Label(frame1, text="Already Registered?", font=("Calibri", 15), bg="#172E36", fg="#D0A85B")
        lbl_already_registered.place(x=430, y=400)

        # Sign In Button
        btn_login = Button(frame1, text="Sign In", command=self.login_window, font=("Calibri", 20, "bold"),
                           bg="#D0A85B", fg="white", bd=2, relief=RAISED)
        btn_login.place(x=430, y=430)

    def login_window(self):
        self.home.destroy()
        os.system("python login.py")

    def clear(self):
        self.txt_fname.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0,END)
        self.txt_password.delete(0, END)
        self.txt_cpassword.delete(0, END)
        self.txt_UserType.current(0)

    # Register Function
    def register_data(self):
        # Check if first name or last name contains non-alphabetic characters
        if (not self.txt_fname.get().isalpha()):
            messagebox.showerror("Error", "Name should only contain alphabets",
                                 parent=self.home)
        # Check if contact number is not a 10-digit number
        elif not self.txt_contact.get().isdigit() or len(self.txt_contact.get()) != 10:
            messagebox.showerror("Error", "Please enter a 10-digit valid Contact Number", parent=self.home)
        # Check if password and confirm password do not match
        elif self.txt_password.get() != self.txt_cpassword.get():
            messagebox.showerror("Error", "Password & Confirm Password should be the same", parent=self.home)
        # Check if the checkbox is unchecked
        elif self.var_chk.get() == 0:
            messagebox.showerror("Error", "Kindly check the box to agree to the terms and conditions",
                                 parent=self.home)
        else:
            try:
                # Connection with database
                conn = sqlite3.connect(database="ResultManagementSystem.db")
                cur = conn.cursor()
                # Check if the user already exists with the given email
                cur.execute("select * from AllUsers where email=?", (self.txt_email.get(),))
                row = cur.fetchone()

                if row:
                    messagebox.showerror("Error", "User already exists. Please try with another email",
                                         parent=self.home)
                else:
                    # Insert new user data into the database
                    cur.execute(
                        "insert into AllUsers (f_name, contact, email, password, u_name) values(?,?,?,?,?)",
                        (self.txt_fname.get(),
                         self.txt_contact.get(),
                         self.txt_email.get(),
                         self.txt_password.get(),
                         self.txt_UserType.get()
                         ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Registration Successful", parent=self.home)
                    self.clear()
                    self.login_window()
            except Exception as es:
                messagebox.showerror("Error", f"Error occurred: {str(es)}", parent=self.home)


home = Tk()
obj = Register(home)
home.mainloop()
