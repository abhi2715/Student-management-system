from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

class StudentClass:
    def __init__(self, home):
        self.home = home
        self.home.title("Student Result Management System")
        self.home.geometry("1200x500+80+170")
        self.home.config(bg="#172E36")
        self.home.focus_force()
        footer=Label(self.home,text="©Abhishek KS, 2024",font=("Calibri",13,"bold"),bg="#172E36",fg="white").pack(side=BOTTOM,fill=X)


        # Title of Course
        title = Label(self.home, text="Manage Student Details", font=("Calibri", 20, "bold"), bg="#172E36", fg="#D0A85B").place(x=0, y=0, relwidth=1, height=40)

        # Variables
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()
        self.var_adm_date = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()

        # Categories of student details 1 side
        rollno = Label(self.home, text="Roll No.", font=("Calibri", 15, "bold"), bg="#172E36", fg="#D0A85B").place(x=10, y=60)
        name = Label(self.home, text="Name", font=("Calibri", 15, "bold"), bg="#172E36", fg="#D0A85B").place(x=10, y=100)
        email = Label(self.home, text="Email", font=("Calibri", 15, "bold"), bg="#172E36", fg="#D0A85B").place(x=10, y=140)
        gender = Label(self.home, text="Gender", font=("Calibri", 15, "bold"), bg="#172E36", fg="#D0A85B").place(x=10, y=180)

        state = Label(self.home, text="State", font=("Calibri", 15, "bold"), bg="#172E36", fg="#D0A85B").place(x=10, y=220)
        self.state1 = Entry(self.home, textvariable=self.var_state, font=("Calibri", 15, "bold"), bg="White")
        self.state1.place(x=150, y=220, width=150)

        city = Label(self.home, text="City", font=("Calibri", 15, "bold"), bg="#172E36", fg="#D0A85B").place(x=330, y=220)
        self.city1 = Entry(self.home, textvariable=self.var_city, font=("Calibri", 15, "bold"), bg="White")
        self.city1.place(x=380, y=220, width=110)

        pin = Label(self.home, text="Pin", font=("Calibri", 15, "bold"), bg="#172E36", fg="#D0A85B").place(x=510, y=220)
        self.pin1 = Entry(self.home, textvariable=self.var_pin, font=("Calibri", 15, "bold"), bg="White")
        self.pin1.place(x=560, y=220, width=120)

        address = Label(self.home, text="Address", font=("Calibri", 15, "bold"), bg="#172E36", fg="#D0A85B").place(x=10, y=260)

        # Entry Fields 1
        self.rollno1 = Entry(self.home, textvariable=self.var_roll, font=("Calibri", 15, "bold"), bg="White")
        self.rollno1.place(x=150, y=60, width=200)

        name1 = Entry(self.home, textvariable=self.var_name, font=("Calibri", 15, "bold"), bg="White").place(x=150, y=100, width=200)
        email1 = Entry(self.home, textvariable=self.var_email, font=("Calibri", 15, "bold"), bg="White").place(x=150, y=140, width=200)

        self.gender1 = ttk.Combobox(self.home, textvariable=self.var_gender, values=("Select", "Male", "Female", "Other"), font=("Calibri", 15, "bold"), state="readonly", justify=CENTER)
        self.gender1.place(x=150, y=180, width=200)
        self.gender1.current(0)

        # Address
        self.address = Text(self.home, font=("Calibri", 15, "bold"), bg="White")
        self.address.place(x=150, y=260, width=540, height=100)

        # Categories of student details 2 side
        dob = Label(self.home, text="D.O.B", font=("Calibri", 15, "bold"), bg="#172E36", fg="#D0A85B").place(x=360, y=60)
        contact = Label(self.home, text="Contact", font=("Calibri", 15, "bold"), bg="#172E36", fg="#D0A85B").place(x=360, y=100)
        admission = Label(self.home, text="Admission", font=("Calibri", 15, "bold"), bg="#172E36", fg="#D0A85B").place(x=360, y=140)
        course = Label(self.home, text="Course", font=("Calibri", 15, "bold"), bg="#172E36", fg="#D0A85B").place(x=360, y=180)

        # Entry Fields 2
        self.course_list = []
        # Function call to update list
        self.fetch_course()

        self.dob1 = Entry(self.home, textvariable=self.var_dob, font=("Calibri", 15, "bold"), bg="White")
        self.dob1.place(x=480, y=60, width=200)

        contact1 = Entry(self.home, textvariable=self.var_contact, font=("Calibri", 15, "bold"), bg="White").place(x=480, y=100, width=200)
        admission1 = Entry(self.home, textvariable=self.var_adm_date, font=("Calibri", 15, "bold"), bg="White").place(x=480, y=140, width=200)

        self.course1 = ttk.Combobox(self.home, textvariable=self.var_course, values=self.course_list, font=("Calibri", 15, "bold"), state="readonly", justify=CENTER)
        self.course1.place(x=480, y=180, width=200)
        self.course1.set("Select")

        # Buttons
        self.add_btn = Button(self.home, text="Save", font=("Calibri", 15, "bold"), bg="#D0A85B", fg="white", cursor="hand2", command=self.add)
        self.add_btn.place(x=720, y=60, width=120, height=50)
        self.update_btn = Button(self.home, text="Update", font=("Calibri", 15, "bold"), bg="#D0A85B", fg="white", cursor="hand2", command=self.update)
        self.update_btn.place(x=720, y=120, width=120, height=50)
        self.delete_btn = Button(self.home, text="Delete", font=("Calibri", 15, "bold"), bg="#D0A85B", fg="white", cursor="hand2", command=self.delete)
        self.delete_btn.place(x=720, y=180, width=120, height=50)
        self.clear_btn = Button(self.home, text="Clear", font=("Calibri", 15, "bold"), bg="#D0A85B", fg="white", cursor="hand2", command=self.clear)
        self.clear_btn.place(x=720, y=240, width=120, height=50)

        # Search Panel
        self.var_search = StringVar()
        search_rollno = Label(self.home, text="Search By Roll No. ", font=("Calibri", 15, "bold"), bg="#172E36", fg="#D0A85B").place(x=150, y=400)
        search_rollno1 = Entry(self.home, textvariable=self.var_search, font=("Calibri", 15, "bold"), bg="White").place(x=330, y=400, width=160, height=30)
        btn_search = Button(self.home, text="Search", font=("Calibri", 15, "bold"), bg="#D0A85B", fg="white", cursor="hand2", command=self.search).place(x=530, y=400, width=100, height=30)

        # Content
        self.C_Frame = Frame(self.home, bd=2, relief=RIDGE)
        self.C_Frame.place(x=20, y=440, width=1500, height=360)

        # Table
        self.CourseTable = ttk.Treeview(self.C_Frame, columns=(
            "roll", "name", "email", "gender", "dob", "contact", "admission", "course", "state", "city", "pin", "address"))

        # Defining the headings for each column
        self.CourseTable.heading("roll", text="Roll No")
        self.CourseTable.heading("name", text="Name")
        self.CourseTable.heading("email", text="Email")
        self.CourseTable.heading("gender", text="Gender")
        self.CourseTable.heading("dob", text="D.O.B")
        self.CourseTable.heading("contact", text="Contact")
        self.CourseTable.heading("admission", text="Admission")
        self.CourseTable.heading("course", text="Course")
        self.CourseTable.heading("state", text="State")
        self.CourseTable.heading("city", text="City")
        self.CourseTable.heading("pin", text="Pin")
        self.CourseTable.heading("address", text="Address")

        self.CourseTable["show"] = "headings"

        # Adjusting the width of each column
        self.CourseTable.column("roll", width=100)
        self.CourseTable.column("name", width=100)
        self.CourseTable.column("email", width=100)
        self.CourseTable.column("gender", width=100)
        self.CourseTable.column("dob", width=100)
        self.CourseTable.column("contact", width=100)
        self.CourseTable.column("admission", width=100)
        self.CourseTable.column("course", width=100)
        self.CourseTable.column("state", width=100)
        self.CourseTable.column("city", width=100)
        self.CourseTable.column("pin", width=100)
        self.CourseTable.column("address", width=150)

        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()

    # Fetching the courses from the database
    def fetch_course(self):
        self.course_list.append("Empty")

    # Saving the details in the database
    def add(self):
        con = sqlite3.connect('ResultManagementSystem.db')
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll Number should be required", parent=self.home)
            else:
                cur.execute("select * from student where roll=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Roll Number already present", parent=self.home)
                else:
                    cur.execute("INSERT INTO student (roll, name, email, gender, dob, contact, admission, course, state, city, pin, address) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", (
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_adm_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.address.get('1.0', END),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Student added successfully", parent=self.home)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.home)

    # Displaying the details
    def show(self):
        con = sqlite3.connect('ResultManagementSystem.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM student")
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.home)

    # Getting the data from the selected row
    def get_data(self, ev):
        f = self.CourseTable.focus()
        content = self.CourseTable.item(f)
        row = content['values']
        self.var_roll.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_dob.set(row[4])
        self.var_contact.set(row[5])
        self.var_adm_date.set(row[6])
        self.var_course.set(row[7])
        self.var_state.set(row[8])
        self.var_city.set(row[9])
        self.var_pin.set(row[10])
        self.address.delete('1.0', END)
        self.address.insert(END, row[11])

    # Updating the details
    def update(self):
        con = sqlite3.connect(database='ResultManagementSystem.db')
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll Number should be required", parent=self.home)
            else:
                cur.execute("select * from student where roll=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Select Student from the list", parent=self.home)
                else:
                    cur.execute("UPDATE student set name=?, email=?, gender=?, dob=?, contact=?, admission=?, course=?, state=?, city=?, pin=?, address=? where roll=?", (
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_adm_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.address.get('1.0', END),
                        self.var_roll.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Student Update successfully", parent=self.home)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.home)

    # Deleting the details
    def delete(self):
        con = sqlite3.connect(database='ResultManagementSystem.db')
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll Number should be required", parent=self.home)
            else:
                cur.execute("select * from student where roll=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Student Roll Number", parent=self.home)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.home)
                    if op == True:
                        cur.execute("delete from student where roll=?", (self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Student deleted successfully", parent=self.home)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.home)

    # Clearing the fields
    def clear(self):
        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_adm_date.set("")
        self.var_course.set("Select")
        self.var_state.set("")
        self.var_city.set("")
        self.var_pin.set("")
        self.address.delete('1.0', END)
        self.var_search.set("")
        self.show()

    # Searching the details
    def search(self):
        con = sqlite3.connect(database='ResultManagementSystem.db')
        cur = con.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Roll Number should be required", parent=self.home)
            else:
                cur.execute("select * from student where roll=?", (self.var_search.get(),))
                row = cur.fetchone()
                if row != None:
                    self.CourseTable.delete(*self.CourseTable.get_children())
                    self.CourseTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found", parent=self.home)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.home)

if __name__ == "__main__":
    home = Tk()
    obj = StudentClass(home)
    home.mainloop()
