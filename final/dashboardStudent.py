#Student Dashboard
from tkinter import*
from tkinter import messagebox,ttk
from PIL import Image,ImageTk
from course import CourseClass
from student import StudentClass
from result import ResultClass
from ViewResult import ViewClass
import sqlite3 
import os
class studentSystem:
    def __init__(self,home):
        self.home=home
        self.home.title("Student Page")
        self.home.geometry("1450x700+0+0")
        self.home.config(bg="#172E36")
        footer=Label(self.home,text="©Abhishek KS, 2024",font=("Calibri",13,"bold"),bg="#172E36",fg="white").pack(side=BOTTOM,fill=X)


        #Title of Student Page
        title=Label(self.home,text="Student Result",font=("Calibri",30,"bold"),bg="#172E36", fg="#D0A85B").place(x=0,y=0,relwidth=1,height=50)

        #Searching Button
        self.var_search=StringVar()
        lbl_rollno = Label(self.home,text="Enter Roll No. ",font=("Calibri",30,"bold"),bg="#172E36", fg="#D0A85B").place(x=400,y=90)
        txt_rollno1 = Entry(self.home,textvariable=self.var_search,font=("Calibri",15,"bold"),bg="white").place(x=650,y=100,width=180,height=35)
        btn_search=Button(self.home,text="Search",font=("Calibri",15,"bold"),bg="#D0A85B",fg="white",cursor="hand2",command=self.search).place(x=880,y=100,width=100,height=35)
        btn_clear=Button(self.home,text="Clear",font=("Calibri",15,"bold"),bg="#D0A85B",fg="white",cursor="hand2",command=self.clear).place(x=1000,y=100,width=100,height=35)

        button_Logout=Button(text="Logout",font=("Calibri",15,"bold"),bg="#D0A85B",fg="white",cursor="hand2",command=self.logout).place(x=1170,y=100,width=100,height=35)

        #Result Of Student and content to show
        lbl_roll = Label(self.home,text="Roll No.",font=("Calibri",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=200,y=310,width=190,height=90)
        lbl_name = Label(self.home,text="Name",font=("Calibri",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=390,y=310,width=190,height=90)
        lbl_course = Label(self.home,text="Course Name",font=("Calibri",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=580,y=310,width=190,height=90)
        lbl_marks = Label(self.home,text="Marks Obtained",font=("Calibri",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=770,y=310,width=190,height=90)
        lbl_full = Label(self.home,text="Total Marks",font=("Calibri",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=960,y=310,width=190,height=90)
        lbl_percentage = Label(self.home,text="Percentage",font=("Calibri",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=1150,y=310,width=190,height=90)

        self.roll = Label(self.home,font=("Calibri",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.roll.place(x=200,y=400,width=190,height=90)
        self.name = Label(self.home,font=("Calibri",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.name.place(x=390,y=400,width=190,height=90)
        self.course = Label(self.home,font=("Calibri",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.course.place(x=580,y=400,width=190,height=90)
        self.full = Label(self.home,font=("Calibri",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.full.place(x=770,y=400,width=190,height=90)
        self.marks = Label(self.home,font=("Calibri",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.marks.place(x=960,y=400,width=190,height=90)
        self.percentage = Label(self.home,font=("Calibri",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.percentage.place(x=1150,y=400,width=190,height=90)

#Functions
    def search(self):
        conn=sqlite3.connect(database="ResultManagementSystem.db")
        cur=conn.cursor()     
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Roll No. should be required",parent=self.home)
            else:
                cur.execute("Select * from result where roll=?",(self.var_search.get(),))
                row=cur.fetchone()
                if row !=None:
                    self.var_id=row[0]
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.marks.config(text=row[4])
                    self.full.config(text=row[5])
                    self.percentage.config(text=row[6])
                else:
                    messagebox.showerror("Error","No record Found",parent=self.home) 
               
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def clear(self):
        self.var_id=""
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks.config(text="")
        self.full.config(text="")
        self.percentage.config(text="")
        self.var_search.set("")
    
    def logout(self):
        op=messagebox.askyesno("Confirm Again","Do You really Want to Logout ?",parent=self.home)
        if op==True:
            self.home.destroy()
            os.system("Python Login.py")
    
        



if __name__=="__main__":
    home=Tk()
    obj=studentSystem(home)
    home.mainloop()