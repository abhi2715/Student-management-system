#Admin Dashboard
from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk 
from course import CourseClass
from student import StudentClass
from result import ResultClass
from ViewResult import ViewClass
import sqlite3 
import os
class ResultManagementSystem:
    def __init__(self,home):
        self.home=home
        self.home.title("Student Result Management System")
        self.home.geometry("1450x700+0+0")
        self.home.config(bg="#172E36")


        #Importing image logo (icons)
        self.logo = ImageTk.PhotoImage(file="Images/logo2.png")  # replace with your image path
        logo = Label(self.home, image=self.logo, bg="#172E36")
        logo.place(x=780, y=75)


        #Title of project
        title=Label(self.home,text="University Student Details Management System",padx=10,compound=LEFT,font=("Calibri",30,"bold"),bg="#172E36",fg="#D0A85B").place(x=30,y=0,relwidth=1,height=50)

        # Menu 
        Frame = LabelFrame(self.home,text="Menu",font=("Calibri",15,"bold"),bg="#172E36", fg="#D0A85B")
        Frame.place(x=10,y=70,width=250,height=500)

        #SubMenu
        button_Course=Button(Frame,text="Course Details",font=("Calibri",15,"bold"),bg="#D0A85B",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)

        button_Student=Button(Frame,text="Student Details",font=("Calibri",15,"bold"),bg="#D0A85B",fg="white",cursor="hand2",command=self.add_student).place(x=20,y=70,width=200,height=40)

        button_Result=Button(Frame,text="Result Details",font=("Calibri",15,"bold"),bg="#D0A85B",fg="white",cursor="hand2",command=self.add_result).place(x=20,y=135,width=200,height=40)

        button_View=Button(Frame,text="View Student Result",font=("Calibri",15,"bold"),bg="#D0A85B",fg="white",cursor="hand2",command=self.add_view).place(x=20,y=200,width=200,height=40)

        button_Logout=Button(Frame,text="Logout",font=("Calibri",15,"bold"),bg="#D0A85B",fg="white",cursor="hand2",command=self.logout).place(x=20,y=265,width=200,height=40)

        button_Exit=Button(Frame,text="Exit",font=("Calibri",15,"bold"),bg="#D0A85B",fg="white",cursor="hand2",command=self.exit).place(x=20,y=330,width=200,height=40)

        # Content Window
        self.bgImage=Image.open("Images/6.jpg")
        self.bgImage=self.bgImage.resize((200,100),Image.Resampling.LANCZOS)
        self.bgImage=ImageTk.PhotoImage(self.bgImage)
        self.lbl_bg=Label(self.home,image=self.bgImage, bg="#172E36").place(x=600,y=50)

        self.logo2 = ImageTk.PhotoImage(file="Images/9.jpeg")  # replace with your image path
        logo2 = Label(self.home, image=self.logo2, bg="#172E36")
        logo2.place(x=325, y=160, height=400, width=900)

        # Update Details
        self.totalCourse=Label(self.home,text="Total Courses \n 0 ",font=("Calibri",20),bg="#D0A85B",fg="white")
        self.totalCourse.place(x=320,y=680,width=300,height=80)
        self.totalstudent=Label(self.home,text="Total Student \n 0 ",font=("Calibri",20),bg="#D0A85B",fg="white")
        self.totalstudent.place(x=630,y=680,width=300,height=80)
        self.totalresults=Label(self.home,text="Total Results \n 0 ",font=("Calibri",20),bg="#D0A85B",fg="white")
        self.totalresults.place(x=940,y=680,width=300,height=80)

        self.slogan=Label(self.home, text="Go, Change The World", font=("Monotype Corsiva",40), bg="#172E36", fg="White")
        self.slogan.place(x=580,y=575)

        #Footer
        footer=Label(self.home,text="©Abhishek KS, 2024\n  Created by Abhishek KS (1RVU23CSE017) , Gayan G (1RVU23CSE166), Bhuvan M (1RVU23CSE115) ssfor Semester End Examinations of SEM 2 AY-2023/24 ",font=("Calibri",13,"bold"),bg="#172E36",fg="white").pack(side=BOTTOM,fill=X)

        self.update_details()

    #Adding function for bottom buttons(Total corses,students,results)
    def update_details(self):
        conn=sqlite3.connect(database="ResultManagementSystem.db")
        cur=conn.cursor()     
        try:
            cur.execute("Select * from course")
            cr=cur.fetchall()
            self.totalCourse.config(text=f"Total Course\n[{str(len(cr))}]")
            self.totalCourse.after(200,self.update_details)

            cur.execute("Select * from student")
            cr=cur.fetchall()
            self.totalstudent.config(text=f"Total Students\n[{str(len(cr))}]")
                
            cur.execute("Select * from result")
            cr=cur.fetchall()
            self.totalresults.config(text=f"Total Results\n[{str(len(cr))}]")

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    #Adding Sub-Menus for Functioning 
    def add_course(self):
        self.window1=Toplevel(self.home)
        self.obj1=CourseClass(self.window1)

    def add_student(self):
        self.window1=Toplevel(self.home)
        self.obj1=StudentClass(self.window1)

    def add_result(self):
        self.window1=Toplevel(self.home)
        self.obj1=ResultClass(self.window1)

    def add_view(self):
        self.window1=Toplevel(self.home)
        self.obj1=ViewClass(self.window1)

#Functioning of Exit and Logout Button
    def logout(self):
        op=messagebox.askyesno("Confirm Again","Do You really Want to Logout ?",parent=self.home)
        if op==True:
            self.home.destroy()
            os.system("Python Login.py")

    def exit(self):
        op=messagebox.askyesno("Confirm Again","Do You really Want to Exit ?",parent=self.home)
        if op==True:
            self.home.destroy()


if __name__=="__main__":
    home=Tk()
    obj=ResultManagementSystem(home)
    home.mainloop()